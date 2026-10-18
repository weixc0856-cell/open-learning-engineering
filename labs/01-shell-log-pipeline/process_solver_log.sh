#!/usr/bin/env bash
# ==============================================================================
# process_solver_log.sh - 工业求解器日志流式指标解析工具 (POSIX 兼容)
# ==============================================================================
set -euo pipefail

usage() {
    echo "Usage: $0 <path-to-solver-log>"
    exit 1
}

if [[ $# -ne 1 ]]; then
    echo "Error: Missing required log file path." >&2
    usage
fi

LOG_FILE="$1"

if [[ ! -f "$LOG_FILE" ]]; then
    echo "Error: File '$LOG_FILE' not found or is not a regular file." >&2
    exit 2
fi

awk '
BEGIN {
    iter = 0;
    initial_residual = "N/A";
    final_residual = "N/A";
    status = "IN_PROGRESS";
}

# 匹配并解析形如: "Iteration: 7, Residual: 8.420000e-05, Time: 0.84s"
$1 == "Iteration:" {
    current_iter = $2;
    gsub(/,/, "", current_iter);
    iter = current_iter;

    current_res = $4;
    gsub(/,/, "", current_res);

    if (initial_residual == "N/A") {
        initial_residual = current_res;
    }
    final_residual = current_res;
}

/SOLVER_STATUS: CONVERGED/ { status = "CONVERGED"; }
/SOLVER_STATUS: DIVERGED/  { status = "DIVERGED"; }

END {
    print "TOTAL_ITERATIONS=" iter;
    print "INITIAL_RESIDUAL=" initial_residual;
    print "FINAL_RESIDUAL=" final_residual;
    print "STATUS=" status;
}
' "$LOG_FILE"
