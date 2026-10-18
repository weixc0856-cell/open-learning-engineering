#!/usr/bin/env python3
"""
scripts/verify_repo.py - 仓库完整性与实验测试全自动验证工具
"""
import os
import sys
import subprocess
import yaml

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def log_step(name: str):
    print(f"\n\033[1;34m==> [CHECK] {name}\033[0m")

def assert_file_exists(rel_path: str):
    p = os.path.join(REPO_ROOT, rel_path)
    if not os.path.isfile(p):
        print(f"\033[1;31m[FAIL] Missing required file: {rel_path}\033[0m")
        sys.exit(1)
    print(f"  ✓ {rel_path}")

def run_cmd(cmd: list, cwd: str):
    print(f"  Running: {' '.join(cmd)} in {cwd}")
    res = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"\033[1;31m[FAIL] Command failed with code {res.returncode}\033[0m")
        print("--- STDOUT ---")
        print(res.stdout)
        print("--- STDERR ---")
        print(res.stderr)
        sys.exit(res.returncode)
    print("  ✓ Success")

def main():
    print("\033[1;32mStarting Open Learning Engineering Repository Audit...\033[0m")

    log_step("Verifying Core Top-Level Files")
    required_top = [
        "README.md",
        "CONTRIBUTING.md",
        "CODE_OF_CONDUCT.md",
        "LICENSES.md",
        "LICENSE",
        "CITATION.cff",
        "mkdocs.yml",
        ".gitignore"
    ]
    for f in required_top:
        assert_file_exists(f)

    log_step("Verifying Docs & Seasons Layout")
    required_docs = [
        "docs/index.md",
        "docs/overview.md",
        "docs/principles.md",
        "docs/roadmap.md",
        "docs/quality-gates.md",
        "docs/licensing.md",
        "docs/seasons/01-computer-foundations/index.md",
        "docs/seasons/02-software-engineering/index.md",
        "docs/seasons/03-python-and-scientific-computing/index.md",
        "docs/seasons/04-computer-architecture-gpu/index.md",
        "docs/seasons/05-deep-learning-sciml/index.md",
        "docs/seasons/06-llm-and-agents/index.md",
        "docs/references/source-index.md",
        "docs/references/license-audit.md"
    ]
    for d in required_docs:
        assert_file_exists(d)

    log_step("Validating mkdocs.yml syntax")
    with open(os.path.join(REPO_ROOT, "mkdocs.yml"), encoding="utf-8") as f:
        config = yaml.safe_load(f)
        assert "site_name" in config, "mkdocs.yml missing site_name"
        assert "nav" in config, "mkdocs.yml missing nav"
    print("  ✓ mkdocs.yml parsed and verified successfully.")

    log_step("Running Lab 01 (Shell Log Pipeline) Tests")
    run_cmd(["bash", "test_pipeline.sh"], os.path.join(REPO_ROOT, "labs/01-shell-log-pipeline"))

    log_step("Running Lab 02 (Architecture & Service) Tests")
    run_cmd([sys.executable, "-m", "unittest", "discover", "-s", ".", "-p", "test_*.py"], os.path.join(REPO_ROOT, "labs/02-architecture-service-contract"))

    log_step("Running Lab 06 (Controlled Agent Workflow) Tests")
    run_cmd([sys.executable, "-m", "unittest", "discover", "-s", ".", "-p", "test_*.py"], os.path.join(REPO_ROOT, "labs/06-controlled-agent-workflow"))

    print("\n\033[1;32m=========================================================\033[0m")
    print("\033[1;32m  ALL AUDITS PASSED: REPOSITORY STRUCTURE IS 100% HEALTHY!\033[0m")
    print("\033[1;32m=========================================================\033[0m\n")

if __name__ == "__main__":
    main()
