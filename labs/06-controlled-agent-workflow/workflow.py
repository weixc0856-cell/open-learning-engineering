# workflow.py
import json
from enum import Enum
from typing import Dict, Any, List, Optional
import datetime

class WorkflowState(Enum):
    PENDING = "PENDING"
    VALIDATING = "VALIDATING"
    EXECUTING = "EXECUTING"
    RECOVERING = "RECOVERING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"

class SchemaValidationError(Exception):
    pass

class IllegalStateTransition(Exception):
    pass

class ControlledAgentWorkflow:
    """A resilient deterministic state machine wrapping LLM agent actions."""
    
    # Strictly declared schema for valid tool action
    ALLOWED_ACTIONS = {"generate_mesh", "run_solver", "render_report"}

    def __init__(self, max_retries: int = 2):
        self.state = WorkflowState.PENDING
        self.max_retries = max_retries
        self.retry_count = 0
        self.audit_log: List[Dict[str, Any]] = []
        self._record_event("WORKFLOW_INITIALIZED", {"state": self.state.value})

    def _record_event(self, event_type: str, details: Dict[str, Any]):
        self.audit_log.append({
            "timestamp": datetime.datetime.utcnow().isoformat(),
            "event": event_type,
            "state": self.state.value,
            "details": details
        })

    def validate_agent_action(self, raw_action_json: str) -> Dict[str, Any]:
        self.state = WorkflowState.VALIDATING
        self._record_event("VALIDATION_STARTED", {"raw_input": raw_action_json})

        try:
            payload = json.loads(raw_action_json)
        except Exception as e:
            self._handle_failure(f"JSON Parse Error: {str(e)}")
            raise SchemaValidationError(f"Invalid JSON format: {str(e)}")

        # Validate Schema contract
        action = payload.get("action")
        params = payload.get("parameters")

        if not action or action not in self.ALLOWED_ACTIONS:
            msg = f"Unknown action: '{action}'. Must be one of {self.ALLOWED_ACTIONS}"
            self._handle_failure(msg)
            raise SchemaValidationError(msg)

        if not isinstance(params, dict):
            msg = "Field 'parameters' must be a JSON dictionary."
            self._handle_failure(msg)
            raise SchemaValidationError(msg)

        self._record_event("VALIDATION_PASSED", {"action": action, "parameters": params})
        return payload

    def execute_action(self, validated_payload: Dict[str, Any]) -> Dict[str, Any]:
        if self.state != WorkflowState.VALIDATING:
            raise IllegalStateTransition(f"Must validate before executing. Current state: {self.state}")

        self.state = WorkflowState.EXECUTING
        action = validated_payload["action"]
        params = validated_payload["parameters"]
        self._record_event("EXECUTION_STARTED", {"action": action})

        # Mock Deterministic Execution
        result = {
            "status": "SUCCESS",
            "action": action,
            "output_reference": f"artifact_{action}_001.dat"
        }

        self.state = WorkflowState.COMPLETED
        self._record_event("WORKFLOW_COMPLETED", {"result": result})
        return result

    def _handle_failure(self, error_msg: str):
        self.retry_count += 1
        if self.retry_count <= self.max_retries:
            self.state = WorkflowState.RECOVERING
            self._record_event("ENTERING_RECOVERY", {"attempt": self.retry_count, "error": error_msg})
        else:
            self.state = WorkflowState.FAILED
            self._record_event("WORKFLOW_FAILED", {"final_error": error_msg})
