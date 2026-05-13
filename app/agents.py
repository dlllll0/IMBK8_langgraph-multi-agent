from app.state import AgentState
from app.prompts import extractor_prompt, candidate_prompt, answer_prompt


def extractor_agent(state: AgentState):
    chain = extractor_prompt | state["llm"]

    symptoms = chain.invoke({
        "query": state["query"]
    })

    return {
        **state,
        "symptoms": symptoms.strip()
    }


def candidate_agent(state: AgentState):
    chain = candidate_prompt | state["llm"]

    exercise_candidates = chain.invoke({
        "symptoms": state["symptoms"]
    })

    return {
        **state,
        "exercise_candidates": exercise_candidates.strip()
    }


def answer_agent(state: AgentState):
    chain = answer_prompt | state["llm"]

    answer = chain.invoke({
        "symptoms": state["symptoms"],
        "exercise_candidates": state["exercise_candidates"]
    })

    return {
        **state,
        "result": answer.strip()
    }