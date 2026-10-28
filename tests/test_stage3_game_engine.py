"""
Stage 3 Game Engine & Spatial Simulation Tests
Unit tests for ECSWorld, MovementSystem, SpatialQuadtree, CollisionSystem, and DeterministicGameLoop.
"""

import unittest
from scripts.ecs_game_engine import (
    ECSWorld,
    Transform2D,
    Velocity2D,
    BoundingBox2D,
    SpatialQuadtree,
    MovementSystem,
    CollisionSystem,
    DeterministicGameLoop,
)


class TestStage3GameEngine(unittest.TestCase):
    def setUp(self):
        self.world = ECSWorld()

    def test_ecs_world_entity_lifecycle(self):
        e1 = self.world.create_entity()
        e2 = self.world.create_entity()

        self.assertNotEqual(e1, e2)
        self.assertIn(e1, self.world.active_entities)
        self.assertIn(e2, self.world.active_entities)

        # Attach components
        t1 = self.world.add_transform(e1, x=10.0, y=20.0)
        v1 = self.world.add_velocity(e1, vx=5.0, vy=-2.0)
        c1 = self.world.add_collider(e1, width=15.0, height=15.0)

        self.assertEqual(self.world.transforms[e1].x, 10.0)
        self.assertEqual(self.world.velocities[e1].vx, 5.0)
        self.assertEqual(self.world.colliders[e1].width, 15.0)

        # Destroy entity
        self.world.destroy_entity(e1)
        self.assertNotIn(e1, self.world.active_entities)
        self.assertNotIn(e1, self.world.transforms)
        self.assertNotIn(e1, self.world.velocities)
        self.assertNotIn(e1, self.world.colliders)

    def test_movement_system_integration(self):
        e = self.world.create_entity()
        self.world.add_transform(e, x=100.0, y=200.0)
        self.world.add_velocity(e, vx=60.0, vy=-30.0)

        # 1 second delta time
        dt = 1.0
        MovementSystem.update(self.world, dt)

        self.assertEqual(self.world.transforms[e].x, 160.0)
        self.assertEqual(self.world.transforms[e].y, 170.0)

        # Half second delta time
        MovementSystem.update(self.world, 0.5)
        self.assertEqual(self.world.transforms[e].x, 190.0)
        self.assertEqual(self.world.transforms[e].y, 155.0)

    def test_spatial_quadtree_partitioning(self):
        tree = SpatialQuadtree(0.0, 0.0, 100.0, 100.0, max_objects=2, max_levels=3)
        
        # Insert 4 objects in different quadrants
        tree.insert(1, 10.0, 10.0, 5.0, 5.0)    # Top-Left
        tree.insert(2, 80.0, 10.0, 5.0, 5.0)    # Top-Right
        tree.insert(3, 10.0, 80.0, 5.0, 5.0)    # Bottom-Left
        tree.insert(4, 80.0, 80.0, 5.0, 5.0)    # Bottom-Right

        # Query around Top-Left
        candidates = tree.retrieve(12.0, 12.0, 5.0, 5.0)
        candidate_ids = [obj[0] for obj in candidates]
        self.assertIn(1, candidate_ids)
        # Should not include Bottom-Right entity (id 4)
        self.assertNotIn(4, candidate_ids)

    def test_collision_system_detection(self):
        col_sys = CollisionSystem(world_width=500.0, world_height=500.0)

        # Entity A and B overlap
        ea = self.world.create_entity()
        self.world.add_transform(ea, x=50.0, y=50.0)
        self.world.add_collider(ea, width=20.0, height=20.0)

        eb = self.world.create_entity()
        self.world.add_transform(eb, x=60.0, y=60.0)
        self.world.add_collider(eb, width=20.0, height=20.0)

        # Entity C is far away
        ec = self.world.create_entity()
        self.world.add_transform(ec, x=400.0, y=400.0)
        self.world.add_collider(ec, width=10.0, height=10.0)

        collisions = col_sys.update(self.world)
        self.assertEqual(len(collisions), 1)
        expected_pair = (min(ea, eb), max(ea, eb))
        self.assertIn(expected_pair, collisions)

    def test_deterministic_game_loop_execution(self):
        e = self.world.create_entity()
        self.world.add_transform(e, x=0.0, y=0.0)
        self.world.add_velocity(e, vx=10.0, vy=0.0)
        self.world.add_collider(e, width=5.0, height=5.0)

        loop = DeterministicGameLoop(self.world, target_fps=60)
        stats = loop.step_fixed_ticks(60)  # Exactly 1 simulated second

        self.assertEqual(stats["ticks_simulated"], 60)
        self.assertEqual(stats["total_ticks"], 60)
        self.assertAlmostEqual(stats["simulated_time_seconds"], 1.0, places=2)
        # Final position after 1 second of moving at 10.0 units/sec
        self.assertAlmostEqual(self.world.transforms[e].x, 10.0, places=1)
        self.assertGreater(stats["effective_fps_capacity"], 100.0)


if __name__ == "__main__":
    unittest.main()
