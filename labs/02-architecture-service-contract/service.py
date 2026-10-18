# service.py
from abc import ABC, abstractmethod
from typing import Dict, Optional, List
from domain_models import SimulationTask, SimulationConfig, DomainError

class TaskNotFoundError(DomainError):
    pass

class ITaskRepository(ABC):
    @abstractmethod
    def save(self, task: SimulationTask) -> None:
        pass

    @abstractmethod
    def get(self, task_id: str) -> Optional[SimulationTask]:
        pass

    @abstractmethod
    def list_all(self) -> List[SimulationTask]:
        pass

class InMemoryTaskRepository(ITaskRepository):
    def __init__(self):
        self._store: Dict[str, SimulationTask] = {}

    def save(self, task: SimulationTask) -> None:
        self._store[task.id] = task

    def get(self, task_id: str) -> Optional[SimulationTask]:
        return self._store.get(task_id)

    def list_all(self) -> List[SimulationTask]:
        return list(self._store.values())

class SimulationService:
    """Service Layer orchestrating domain entities and persistence contracts."""
    def __init__(self, repository: ITaskRepository):
        self.repository = repository

    def create_task(self, solver_name: str, grid_resolution: int, tolerance: float, max_iterations: int) -> str:
        config = SimulationConfig(
            solver_name=solver_name,
            grid_resolution=grid_resolution,
            tolerance=tolerance,
            max_iterations=max_iterations
        )
        task = SimulationTask(config=config)
        self.repository.save(task)
        return task.id

    def execute_task(self, task_id: str, simulated_iterations: int, should_fail: bool = False, fail_reason: str = "") -> SimulationTask:
        task = self.repository.get(task_id)
        if not task:
            raise TaskNotFoundError(f"Task with ID {task_id} not found.")

        task.start_running()
        if should_fail:
            task.mark_failed(fail_reason or "Solver divergence.")
        else:
            task.mark_completed(simulated_iterations)
        
        self.repository.save(task)
        return task
