# test_workflow.py
import unittest
from workflow import ControlledAgentWorkflow, WorkflowState, SchemaValidationError, IllegalStateTransition

class TestControlledAgentWorkflow(unittest.TestCase):
    def test_successful_happy_path(self):
        wf = ControlledAgentWorkflow()
        raw_json = '{"action": "run_solver", "parameters": {"iterations": 100, "tolerance": 1e-4}}'
        
        validated = wf.validate_agent_action(raw_json)
        self.assertEqual(wf.state, WorkflowState.VALIDATING)
        
        result = wf.execute_action(validated)
        self.assertEqual(wf.state, WorkflowState.COMPLETED)
        self.assertEqual(result["status"], "SUCCESS")
        self.assertTrue(len(wf.audit_log) >= 4)

    def test_invalid_json_triggers_recovery(self):
        wf = ControlledAgentWorkflow(max_retries=1)
        with self.assertRaises(SchemaValidationError):
            wf.validate_agent_action("MALFORMED_NON_JSON")
        self.assertEqual(wf.state, WorkflowState.RECOVERING)

    def test_unauthorized_action_rejected(self):
        wf = ControlledAgentWorkflow(max_retries=0)
        raw_json = '{"action": "delete_database", "parameters": {}}'
        with self.assertRaises(SchemaValidationError):
            wf.validate_agent_action(raw_json)
        self.assertEqual(wf.state, WorkflowState.FAILED)

    def test_execution_without_validation_guard(self):
        wf = ControlledAgentWorkflow()
        with self.assertRaises(IllegalStateTransition):
            wf.execute_action({"action": "run_solver", "parameters": {}})

if __name__ == "__main__":
    unittest.main()
