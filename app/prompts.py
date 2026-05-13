from langchain.prompts import PromptTemplate


extractor_prompt = PromptTemplate.from_template("""
사용자의 질문에서 증상에 해당하는 단어 또는 구를 추출하세요.
결과는 쉼표로 구분된 문자열로 출력하세요.

질문: {query}
""")


candidate_prompt = PromptTemplate.from_template("""
다음 증상 목록을 바탕으로 도움이 될 수 있는 운동 리스트를 추천하세요.

증상: {symptoms}

조건:
- 현실적으로 할 수 있는 운동만 추천하세요.
- 운동 이름만 쉼표로 구분해서 출력하세요.
- 무리한 고강도 운동은 제외하세요.
- 한국어로 작성하세요.
""")


answer_prompt = PromptTemplate.from_template("""
사용자의 증상은 다음과 같습니다.

증상:
{symptoms}

추천 운동 리스트:
{exercise_candidates}

위 내용을 바탕으로 사용자에게 알기 쉽게 개조식으로 답변하세요.

출력 형식:

### 추출된 증상
- 증상 1
- 증상 2

### 추천 운동
- 운동명: 추천 이유
- 운동명: 추천 이유

### 운동 시 주의사항
- 주의사항 1
- 주의사항 2

반드시 한국어로 작성하세요.
""")