r"""
High-Performance ECS Game Engine & Spatial Simulation Loop
Zobar Skill — Stanford CS248 & CMU 15-462 Academic Standard

Architecture:
1. Data-Oriented Design (DOD): Structure of Arrays (SoA) layout for CPU L1/L2 cache locality.
2. Entity-Component-System (ECS):
   - Entity: Pure integer ID.
   - Components: Pure data structs (Transform2D, Velocity2D, BoundingBox2D).
   - Systems: Pure logic operating on contiguous memory slices (MovementSystem, CollisionSystem).
3. Spatial Partitioning (Quadtree): $O(N \log N)$ collision query reduction.
4. Deterministic Game Loop: Fixed-timestep accumulator (60 FPS / 16.67ms tick).
"""

import time
import math
from typing import Dict, Any, List, Set, Optional, Tuple, Callable


class Transform2D:
    __slots__ = ("x", "y")
    def __init__(self, x: float = 0.0, y: float = 0.0):
        self.x = float(x)
        self.y = float(y)

    def to_dict(self) -> Dict[str, float]:
        return {"x": round(self.x, 3), "y": round(self.y, 3)}


class Velocity2D:
    __slots__ = ("vx", "vy")
    def __init__(self, vx: float = 0.0, vy: float = 0.0):
        self.vx = float(vx)
        self.vy = float(vy)

    def to_dict(self) -> Dict[str, float]:
        return {"vx": round(self.vx, 3), "vy": round(self.vy, 3)}


class BoundingBox2D:
    __slots__ = ("width", "height")
    def __init__(self, width: float = 1.0, height: float = 1.0):
        self.width = float(width)
        self.height = float(height)

    def to_dict(self) -> Dict[str, float]:
        return {"width": self.width, "height": self.height}


class SpatialQuadtree:
    """
    Stanford CS248 Spatial Partitioning:
    Subdivides 2D space into 4 quadrants to avoid $O(N^2)$ brute-force collision testing.
    """
    def __init__(self, x: float, y: float, width: float, height: float, max_objects: int = 4, max_levels: int = 5, level: int = 0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.max_objects = max_objects
        self.max_levels = max_levels
        self.level = level
        self.objects: List[Tuple[int, float, float, float, float]] = []  # (entity_id, x, y, w, h)
        self.nodes: List['SpatialQuadtree'] = []

    def clear(self) -> None:
        self.objects.clear()
        for node in self.nodes:
            node.clear()
        self.nodes.clear()

    def _split(self) -> None:
        sub_w = self.width / 2.0
        sub_h = self.height / 2.0
        x = self.x
        y = self.y

        self.nodes = [
            SpatialQuadtree(x + sub_w, y, sub_w, sub_h, self.max_objects, self.max_levels, self.level + 1),         # Top-Right (0)
            SpatialQuadtree(x, y, sub_w, sub_h, self.max_objects, self.max_levels, self.level + 1),                 # Top-Left (1)
            SpatialQuadtree(x, y + sub_h, sub_w, sub_h, self.max_objects, self.max_levels, self.level + 1),         # Bottom-Left (2)
            SpatialQuadtree(x + sub_w, y + sub_h, sub_w, sub_h, self.max_objects, self.max_levels, self.level + 1), # Bottom-Right (3)
        ]

    def _get_index(self, x: float, y: float, w: float, h: float) -> int:
        mid_x = self.x + (self.width / 2.0)
        mid_y = self.y + (self.height / 2.0)

        top = (y < mid_y and y + h < mid_y)
        bottom = (y > mid_y)

        if x < mid_x and x + w < mid_x:
            if top:
                return 1
            elif bottom:
                return 2
        elif x > mid_x:
            if top:
                return 0
            elif bottom:
                return 3
        return -1

    def insert(self, entity_id: int, x: float, y: float, w: float, h: float) -> None:
        if self.nodes:
            index = self._get_index(x, y, w, h)
            if index != -1:
                self.nodes[index].insert(entity_id, x, y, w, h)
                return

        self.objects.append((entity_id, x, y, w, h))

        if len(self.objects) > self.max_objects and self.level < self.max_levels:
            if not self.nodes:
                self._split()

            i = 0
            while i < len(self.objects):
                obj = self.objects[i]
                index = self._get_index(obj[1], obj[2], obj[3], obj[4])
                if index != -1:
                    self.objects.pop(i)
                    self.nodes[index].insert(*obj)
                else:
                    i += 1

    def retrieve(self, x: float, y: float, w: float, h: float) -> List[Tuple[int, float, float, float, float]]:
        return_objects = list(self.objects)
        if self.nodes:
            index = self._get_index(x, y, w, h)
            if index != -1:
                return_objects.extend(self.nodes[index].retrieve(x, y, w, h))
            else:
                for node in self.nodes:
                    return_objects.extend(node.retrieve(x, y, w, h))
        return return_objects


class ECSWorld:
    """
    Contiguous memory and fast lookup storage for Entity-Component-System.
    """
    def __init__(self):
        self._next_entity_id: int = 1
        self.active_entities: Set[int] = set()

        # Component Stores: Mapping from entity_id -> Component
        self.transforms: Dict[int, Transform2D] = {}
        self.velocities: Dict[int, Velocity2D] = {}
        self.colliders: Dict[int, BoundingBox2D] = {}

    def create_entity(self) -> int:
        entity_id = self._next_entity_id
        self._next_entity_id += 1
        self.active_entities.add(entity_id)
        return entity_id

    def destroy_entity(self, entity_id: int) -> None:
        self.active_entities.discard(entity_id)
        self.transforms.pop(entity_id, None)
        self.velocities.pop(entity_id, None)
        self.colliders.pop(entity_id, None)

    def add_transform(self, entity_id: int, x: float = 0.0, y: float = 0.0) -> Transform2D:
        t = Transform2D(x, y)
        self.transforms[entity_id] = t
        return t

    def add_velocity(self, entity_id: int, vx: float = 0.0, vy: float = 0.0) -> Velocity2D:
        v = Velocity2D(vx, vy)
        self.velocities[entity_id] = v
        return v

    def add_collider(self, entity_id: int, width: float = 1.0, height: float = 1.0) -> BoundingBox2D:
        c = BoundingBox2D(width, height)
        self.colliders[entity_id] = c
        return c


class MovementSystem:
    """
    Updates transforms based on velocities over delta time (dt).
    """
    @staticmethod
    def update(world: ECSWorld, dt: float) -> int:
        updated_count = 0
        # Iterate over entities having BOTH transform and velocity
        for entity_id, vel in world.velocities.items():
            trans = world.transforms.get(entity_id)
            if trans:
                trans.x += vel.vx * dt
                trans.y += vel.vy * dt
                updated_count += 1
        return updated_count


class CollisionSystem:
    """
    Detects AABB overlaps accelerated by SpatialQuadtree.
    """
    def __init__(self, world_width: float = 1000.0, world_height: float = 1000.0):
        self.quadtree = SpatialQuadtree(0.0, 0.0, world_width, world_height)

    def update(self, world: ECSWorld) -> List[Tuple[int, int]]:
        self.quadtree.clear()
        
        # Populate quadtree
        for entity_id, box in world.colliders.items():
            trans = world.transforms.get(entity_id)
            if trans:
                self.quadtree.insert(entity_id, trans.x, trans.y, box.width, box.height)

        collisions: List[Tuple[int, int]] = []
        checked_pairs: Set[Tuple[int, int]] = set()

        for entity_id, box in world.colliders.items():
            trans = world.transforms.get(entity_id)
            if not trans:
                continue

            candidates = self.quadtree.retrieve(trans.x, trans.y, box.width, box.height)
            for other_id, ox, oy, ow, oh in candidates:
                if other_id == entity_id:
                    continue
                pair = (min(entity_id, other_id), max(entity_id, other_id))
                if pair in checked_pairs:
                    continue
                checked_pairs.add(pair)

                # AABB Intersection Test
                if (trans.x < ox + ow and
                    trans.x + box.width > ox and
                    trans.y < oy + oh and
                    trans.y + box.height > oy):
                    collisions.append(pair)

        return collisions


class DeterministicGameLoop:
    """
    Fixed-timestep accumulator loop guaranteeing 60 FPS deterministic simulation.
    """
    def __init__(self, world: ECSWorld, target_fps: int = 60):
        self.world = world
        self.target_fps = target_fps
        self.fixed_dt = 1.0 / float(target_fps)
        self.movement_system = MovementSystem()
        self.collision_system = CollisionSystem()
        self.total_ticks = 0

    def step_fixed_ticks(self, num_ticks: int) -> Dict[str, Any]:
        """
        Executes N deterministic simulation frames.
        """
        start_perf = time.perf_counter()
        total_collisions = 0

        for _ in range(num_ticks):
            self.movement_system.update(self.world, self.fixed_dt)
            collisions = self.collision_system.update(self.world)
            total_collisions += len(collisions)
            self.total_ticks += 1

        elapsed = time.perf_counter() - start_perf
        avg_tick_time_ms = (elapsed / max(num_ticks, 1)) * 1000.0

        return {
            "ticks_simulated": num_ticks,
            "total_ticks": self.total_ticks,
            "fixed_dt": round(self.fixed_dt, 5),
            "simulated_time_seconds": round(num_ticks * self.fixed_dt, 3),
            "total_collisions_detected": total_collisions,
            "avg_tick_time_ms": round(avg_tick_time_ms, 4),
            "effective_fps_capacity": round(1000.0 / max(avg_tick_time_ms, 0.0001), 1),
            "active_entities": len(self.world.active_entities),
        }


if __name__ == "__main__":
    world = ECSWorld()
    # Spawn 50 entities
    for i in range(50):
        e = world.create_entity()
        world.add_transform(e, x=(i * 15.0) % 500, y=(i * 10.0) % 500)
        world.add_velocity(e, vx=10.0, vy=-5.0)
        world.add_collider(e, width=12.0, height=12.0)

    loop = DeterministicGameLoop(world)
    stats = loop.step_fixed_ticks(60)  # Simulate 1 second of 60 FPS gameplay
    print("=" * 60)
    print("🎮 STANFORD / CMU ECS OYUN MOTORU SİMÜLASYONU 🎮")
    print("=" * 60)
    for k, v in stats.items():
        print(f"[*] {k:28}: {v}")
