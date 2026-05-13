# LangGraph Multi-Agent Exercise

## 1. Project Overview

본 프로젝트는 LangGraph 기반의 Multi-Agent Workflow를 활용하여  
사용자의 운동 관련 질문을 단계적으로 분석하고 답변을 생성하는 실습 프로젝트이다.

단일 LLM 호출 방식이 아닌,  
각 역할을 수행하는 여러 Agent를 그래프 구조로 연결하여  
증상 추출 → 운동 추천 → 최종 답변 생성 과정을 분리하였다.

사용자의 질문을 기반으로 다음과 같은 Agent들이 순차적으로 동작한다.

- 증상 추출 Agent
- 운동 후보 추천 Agent
- 최종 답변 생성 Agent

각 Agent는 상태(State)를 공유하며 Workflow를 수행한다.

---

# 2. Multi-Agent Structure

본 프로젝트는 총 3개의 Agent로 구성된다.

## 1) Extractor Agent

사용자의 질문에서 핵심 증상 및 상태를 추출한다.

예시:
- 체력 저하
- 체중 증가
- 피로감

---

## 2) Candidate Agent

추출된 증상을 기반으로  
적절한 운동 후보들을 추천한다.

예시:
- 걷기
- 러닝
- 자전거
- 홈트레이닝

---

## 3) Answer Agent

증상과 운동 후보 리스트를 기반으로  
최종 답변을 개조식 형태로 생성한다.

최종적으로:
- 증상 분석
- 운동 추천 이유
- 운동 시 주의사항

등을 사용자 친화적으로 출력한다.

---

# 3. Workflow

```text
User Query
    ↓
Extractor Agent
(증상 추출)
    ↓
Candidate Agent
(운동 후보 추천)
    ↓
Answer Agent
(최종 답변 생성)
```

---

# 4. Tech Stack

## Language

- Python

## LLM / AI

- Ollama
- Llama 3.2
- LangChain
- LangGraph

## Environment

- Jupyter Notebook
- VSCode

---

# 5. LangGraph Structure

LangGraph를 활용하여 각 Agent를 그래프 형태로 연결하였다.

- Extractor Node
- Candidate Node
- Answer Node

각 노드는 이전 Agent의 결과(State)를 전달받아 다음 작업을 수행한다.

## Graph Structure

![alt text](image-1.png)

```python
graph.add_edge("extractor", "candidate")
graph.add_edge("candidate", "answer")
graph.add_edge("answer", END)
```

---

# 6. State Management

LangGraph의 StateGraph를 활용하여  
Agent 간 상태(State)를 공유하였다.

```python
class AgentState(TypedDict):
    query: str
    symptoms: str
    exercise_candidates: str
    result: str
```

이를 통해 각 Agent는 다음 데이터를 공유한다.

- 사용자 질문
- 추출된 증상
- 운동 후보 리스트
- 최종 응답

State 기반 구조를 통해  
각 Agent가 이전 결과를 이어받아 단계적으로 작업을 수행하도록 설계하였다.

---

# 7. Prompt Engineering

각 Agent마다 역할별 Prompt를 분리하여 구성하였다.

## Extractor Prompt

사용자의 질문에서 핵심 증상 추출

## Candidate Prompt

증상 기반 운동 후보 추천

## Answer Prompt

최종 사용자 응답 생성

Prompt를 역할별로 분리함으로써  
단일 Prompt 대비 보다 구조적인 응답 생성을 수행하였다.

---

# 8. Result Example

## Input

```text
체력이 안좋고, 살이 계속 찌는데 어떤 운동을 할까?
```

## Output

```text
### 추출된 증상
- 체력 저하
- 체중 증가

### 추천 운동
- 걷기 : 초보자도 쉽게 시작 가능한 유산소 운동
- 수영 : 관절 부담이 적고 전신 운동 효과 제공
- 실내 자전거 : 체지방 감소와 심폐 기능 향상에 도움
- 가벼운 근력 운동 : 기초대사량 증가 및 체력 강화

### 운동 시 주의사항
- 운동 강도는 점진적으로 증가시키기
- 충분한 휴식과 수면 병행하기
```

## Result Image

![alt text](image.png)

---

# 9. What I Learned

본 실습을 통해 다음 내용을 학습하였다.

- LangGraph 기반 Multi-Agent Workflow 구성
- State 기반 Agent 간 데이터 전달
- LangChain Prompt Chain 구성
- Ollama 기반 로컬 LLM 활용
- Multi-Step Reasoning 구조 설계

특히 단일 LLM 호출 방식이 아닌  
역할 기반 Agent 분리를 통해  
보다 구조적인 응답 생성 방식을 경험할 수 있었다.

---

# 10. Future Improvements

향후 개선 방향은 다음과 같다.

- 운동 추천 데이터셋 기반 RAG 적용
- 사용자 건강 상태 기반 개인화 추천
- 운동 강도 및 운동 시간 추천 기능 추가
- FastAPI 기반 웹 챗봇 구현
- Streamlit UI 연동
- Memory 기반 대화형 Agent 구현