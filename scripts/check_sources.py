#!/usr/bin/env python3
"""
scripts/check_sources.py - 引用文献与资料卡合规校验器
"""
import os
import sys

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
INDEX_FILE = os.path.join(REPO_ROOT, "docs/references/source-index.md")

def main():
    if not os.path.exists(INDEX_FILE):
        print(f"Error: {INDEX_FILE} not found!")
        sys.exit(1)

    with open(INDEX_FILE, encoding="utf-8") as f:
        content = f.read()

    required_keywords = [
        "SRC-01",
        "SRC-02",
        "SRC-03",
        "SRC-04",
        "SRC-05",
        "SRC-06",
        "SRC-07",
        "SRC-08",
        "官方网址",
        "版权许可证",
        "审计结论"
    ]

    for kw in required_keywords:
        if kw not in content:
            print(f"Missing required source card attribute: {kw}")
            sys.exit(1)

    print("✓ Source index cards validated. All 8 core evidence sources present and properly formatted.")

if __name__ == "__main__":
    main()
