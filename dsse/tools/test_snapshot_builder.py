#!/usr/bin/env python3
"""Minimal test for dsse_snapshot_builder --max off-by-one fix."""
import json, os, subprocess, sys, tempfile
from pathlib import Path

SCRIPT = Path(__file__).parent / "dsse_snapshot_builder.py"

def make_input(path, n):
    with open(path, "w") as f:
        for i in range(n):
            f.write(json.dumps({"schema": "x", "license": "ok", "i": i}) + "\n")

def run(inp, out, max_n):
    subprocess.run([sys.executable, str(SCRIPT), "--in", inp, "--out", out, "--max", str(max_n)], check=True)
    return json.loads(Path(out).read_text())

def test_max_2():
    inp, out = "dsse_test_tmp.jsonl", "dsse_out_tmp.json"
    make_input(inp, 3)
    r = run(inp, out, 2)
    assert r["records_seen"] == 2, f"FAIL max=2: got {r['records_seen']}"
    print(f"[OK] --max 2 -> records_seen = {r['records_seen']}")

def test_max_1():
    inp, out = "dsse_test_tmp.jsonl", "dsse_out_tmp.json"
    make_input(inp, 3)
    r = run(inp, out, 1)
    assert r["records_seen"] == 1, f"FAIL max=1: got {r['records_seen']}"
    print(f"[OK] --max 1 -> records_seen = {r['records_seen']}")

def test_no_max():
    inp, out = "dsse_test_tmp.jsonl", "dsse_out_tmp.json"
    make_input(inp, 5)
    r = run(inp, out, 0)
    assert r["records_seen"] == 5, f"FAIL no max: got {r['records_seen']}"
    print(f"[OK] --max 0 (all) -> records_seen = {r['records_seen']}")

if __name__ == "__main__":
    try:
        test_max_2()
        test_max_1()
        test_no_max()
        print("\n[OK] All tests passed — off-by-one fix verified")
    finally:
        for f in ["dsse_test_tmp.jsonl", "dsse_out_tmp.json"]:
            if os.path.exists(f):
                os.remove(f)
