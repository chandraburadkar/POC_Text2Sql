# app/state/agent_state.py
from __future__ import annotations

from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field


class AgentState(BaseModel):
    # Inputs
    user_question: str = ""

    # Step 5 outputs
    rewritten_query: str = ""
    intent: str = "UNKNOWN"
    entities: Dict[str, Any] = Field(default_factory=dict)

    # Step 4 outputs (RAG)
    schema_context: str = ""
    retrieved_tables: List[str] = Field(default_factory=list)

    # Step 6/7 outputs
    candidate_sql: Dict[str, Any] = Field(default_factory=dict)  # from generate_sql()
    final_sql: str = ""
    validation_ok: bool = False
    fixed_by_llm: bool = False

    # Step 8 outputs
    dataframe: Dict[str, Any] = Field(default_factory=dict)  # {row_count, columns, df, preview_markdown}

    # Step 9 outputs
    explanation: Dict[str, Any] = Field(default_factory=dict)
    chart_path: Optional[str] = None

    # Debug
    debug: Dict[str, Any] = Field(default_factory=dict)