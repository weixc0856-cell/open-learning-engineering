# test_service.py
import unittest
from domain_models import SimulationConfig, TaskStatus, InvalidConfigError, InvalidStateTransitionError
from service import SimulationService, InMemoryTaskRepository, TaskNotFoundError

class TestSimulationDomainAndService(unittest.TestCase):
    def setUp(self):
        self.repo = InMemoryTaskRepository()
        self.service = SimulationService(self.repo)

    def test_config_invariants_valid(self):
        cfg = SimulationConfig(solver_name="OpenFOAM", grid_resolution=50000, tolerance=1e-4, max_iterations=500)
        self.assertEqual(cfg.solver_name, "OpenFOAM")

    def test_config_invariants_invalid_tolerance(self):
        with self.assertRaises(InvalidConfigError):
            SimulationConfig(solver_name="OpenFOAM", grid_resolution=100, tolerance=1.5, max_iterations=100)

    def test_config_invariants_invalid_grid(self):
        with self.assertRaises(InvalidConfigError):
            SimulationConfig(solver_name="OpenFOAM", grid_resolution=0, tolerance=1e-4, max_iterations=100)

    def test_successful_task_lifecycle(self):
        task_id = self.service.create_task("Fluent", 10000, 1e-5, 200)
        task = self.service.execute_task(task_id, simulated_iterations=42)
        self.assertEqual(task.status, TaskStatus.COMPLETED)
        self.assertEqual(task.iteration_count, 42)

    def test_failed_task_lifecycle(self):
        task_id = self.service.create_task("OpenFOAM", 20000, 1e-4, 100)
        task = self.service.execute_task(task_id, 10, should_fail=True, fail_reason="Memory overflow")
        self.assertEqual(task.status, TaskStatus.FAILED)
        self.assertEqual(task.error_message, "Memory overflow")

    def test_execute_non_existent_task(self):
        with self.assertRaises(TaskNotFoundError):
            self.service.execute_task("invalid-uuid-1234", 10)

    def test_invalid_state_transition(self):
        task_id = self.service.create_task("Fluent", 10000, 1e-4, 50)
        raw_task = self.repo.get(task_id)
        # Attempting to complete without running must fail
        with self.assertRaises(InvalidStateTransitionError):
            raw_task.mark_completed(10)

if __name__ == "__main__":
    unittest.main()
