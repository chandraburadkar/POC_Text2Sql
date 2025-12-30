# app/main.py
from __future__ import annotations

import sys
from dotenv import load_dotenv
load_dotenv(override=True)

from app.graph.text2sql_graph import run_text2sql


def main():
    if len(sys.argv) < 2:
        print("Usage: python -m app.main \"<your question>\"")
        sys.exit(1)

    q = sys.argv[1]
    out = run_text2sql(q)

    print("\nFINAL SQL:\n", out.get("final_sql"))
    print("\nPREVIEW:\n", out.get("preview_markdown", ""))

    expl = out.get("explanation", {})
    if expl:
        print("\nEXPLANATION:\n", expl.get("summary", ""))


if __name__ == "__main__":
    main()