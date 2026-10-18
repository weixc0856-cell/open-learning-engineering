#!/usr/bin/env bash
# ==============================================================================
# test_pipeline.sh - Lab 01 自动化测试套件
# ==============================================================================
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PARSER="$SCRIPT_DIR/process_solver_log.sh"
SAMPLE_LOG="$SCRIPT_DIR/sample_solver.log"

echo "=== Running Lab 01 Tests ==="

# Test 1: 缺少参数应退出码 1
set +e
"$PARSER" >/dev/null 2>&1
CODE=$?
set -e
if [[ $CODE -ne 1 ]]; then
    echo "FAIL: Expected exit code 1 for missing arguments, got $CODE"
    exit 1
fi
echo "✓ Test 1: Missing argument exit code verified (1)"

# Test 2: 文件不存在应退出码 2
set +e
"$PARSER" "$SCRIPT_DIR/non_existent.log" >/dev/null 2>&1
CODE=$?
set -e
if [[ $CODE -ne 2 ]]; then
    echo "FAIL: Expected exit code 2 for missing file, got $CODE"
    exit 1
fi
echo "✓ Test 2: Missing file exit code verified (2)"

# Test 3: 正常文件解析结果与字段验证
OUTPUT=$("$PARSER" "$SAMPLE_LOG")
echo "$OUTPUT" | grep -q "TOTAL_ITERATIONS=7"
echo "$OUTPUT" | grep -q "INITIAL_RESIDUAL=1.000000e+00"
echo "$OUTPUT" | grep -q "FINAL_RESIDUAL=8.420000e-05"
echo "$OUTPUT" | grep -q "STATUS=CONVERGED"
echo "✓ Test 3: Log extraction accuracy and convergence verified"

echo "=== All Lab 01 Tests Passed Successfully! ==="
