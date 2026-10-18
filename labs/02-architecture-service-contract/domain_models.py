# domain_models.py
from dataclasses import dataclass
from enum import Enum
from typing import Optional
import uuid

class TaskStatus(Enum):
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"

class DomainError(Exception):
    """Base exception for domain rule violations."""
    pass

class InvalidConfigError(DomainError):
    pass

class InvalidStateTransitionError(DomainError):
    pass

@dataclass(frozen=True)
class SimulationConfig:
    """Immutable Value Object with domain invariant constraints."""
    solver_name: str
    grid_resolution: int
    tolerance: float
    max_iterations: int

    def __post_init__(self):
        if not self.solver_name or len(self.solver_name.strip()) == 0:
            raise InvalidConfigError("solver_name must not be empty.")
        if self.grid_resolution <= 0:
            raise InvalidConfigError("grid_resolution must be strictly positive.")
        if not (0.0 < self.tolerance < 1.0):
            raise InvalidConfigError("tolerance must be between 0.0 and 1.0.")
        if self.max_iterations < 10:
            raise InvalidConfigError("max_iterations must be at least 10.")

class SimulationTask:
    """Domain Entity managing execution lifecycle and state invariants."""
    def __init__(self, config: SimulationConfig, task_id: Optional[str] = None):
        self.id = task_id or str(uuid.uuid4())
        self.config = config
        self.status = TaskStatus.PENDING
        self.error_message: Optional[str] = None
        self.iteration_count: int = 0

    def start_running(self):
        if self.status != TaskStatus.PENDING:
            raise InvalidStateTransitionError(f"Cannot start task from status {self.status}")
        self.status = TaskStatus.RUNNING

    def mark_completed(self, total_iterations: int):
        if self.status != TaskStatus.RUNNING:
            raise InvalidStateTransitionError(f"Cannot complete task from status {self.status}")
        self.iteration_count = total_iterations
        self.status = TaskStatus.COMPLETED

    def mark_failed(self, reason: str):
        if self.status != TaskStatus.RUNNING:
            raise InvalidStateTransitionError(f"Cannot fail task from status {self.status}")
        self.error_message = reason
        self.status = TaskStatus.FAILED
