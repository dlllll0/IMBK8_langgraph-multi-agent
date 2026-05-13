import os

from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, END

from app.state import AgentState
from app.agents import extractor_agent, candidate_agent, answer_agent


# 1. 환경 설정
os.environ["OPENAI_API_KEY"] = "NA"


# 2. LLM 설정
llm = ChatOpenAI(
    model="ollama/llama3.2",
    base_url="http://localhost:11434"
)


# 3. LangGraph 정의
graph = StateGraph(AgentState)

graph.add_node("extractor", extractor_agent)
graph.add_node("candidate", candidate_agent)
graph.add_node("answer", answer_agent)

graph.set_entry_point("extractor")

graph.add_edge("extractor", "candidate")
graph.add_edge("candidate", "answer")
graph.add_edge("answer", END)

app = graph.compile()


# 4. 실행
if __name__ == "__main__":

    print("============================== LangGraph 구조:")
    app.get_graph().print_ascii()

    query = "체력이 안좋고, 살이 계속 찌는데 어떤 운동을 할까?"

    result = app.invoke({
        "query": query,
        "symptoms": "",
        "exercise_candidates": "",
        "result": "",
        "llm": llm
    })

    print("============================== 최종 응답:")
    print(result["result"])
