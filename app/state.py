from typing import TypedDict, Any


class AgentState(TypedDict):
    query: str
    symptoms: str
    exercise_candidates: str
    result: str
    llm: Any