import streamlit as st

# 1. 데이터 정의 (리스트 활용)
department_list = [
    ["응급실(ER)", "빠른 대처", "중증도 분류 및 신속한 초기 응급처치"],
    ["중환자실(ICU)", "모니터링", "중증 환자 생명 유지 확인하며 관리"],
    ["수술실(OR)", "협동심", "수술 물품 전달 및 보조"],
    ["일반 병동(GW)", "배려와 소통", "투약 및 입원 환자 회복 관리"],
]


# 2. 맞춤형 추천 로직 함수 정의 (def, for, if-elif-else 활용)
def recommend_department(user_strength, user_interest):
    matched_dept = ""

    for dept in department_list:
        if dept[1] == user_strength:
            matched_dept = dept[0]
            break

    if matched_dept == user_interest:
        result_msg = f"장점('{user_strength}')과 관심 부서가 완벽히 일치합니다! **'{matched_dept}'**을(를) 강력 추천합니다."
        match_score = 100
    elif user_strength != "" and user_interest != "":
        result_msg = f"성향('{user_strength}')을 고려하면 **'{matched_dept}'**이 가장 잘 맞지만, 관심사인 **'{user_interest}'** 분야에서도 역량을 발휘할 수 있습니다."
        match_score = 85
    else:
        result_msg = "성향과 관심사를 모두 선택해주세요."
        match_score = 0

    return result_msg, match_score


# 3. Streamlit 웹 화면 구성
st.title("🏥 맞춤형 간호 부서 가이드")
st.write("자신의 성향(장점)과 관심 부서를 선택하면 가장 잘 맞는 간호 부서를 안내해 드립니다.")
st.markdown("---")

# (1) 자신의 장점 선택
strength_options = ["빠른 대처", "모니터링", "협동심", "배려와 소통"]
selected_strength = st.selectbox("(1) 자신의 장점 선택:", strength_options)

# (2) 관심 부서 입력
interest_options = ["응급실(ER)", "중환자실(ICU)", "수술실(OR)", "일반 병동(GW)"]
selected_interest = st.selectbox("(2) 관심 부서 입력:", interest_options)

# [ 버튼: 분석하기 ]
if st.button("분석하기"):
    st.markdown("---")
    st.subheader("📋 분석 결과")

    recommendation, score = recommend_department(selected_strength, selected_interest)
    st.success(recommendation)

    # 부서별 세부 목록 표 출력
    st.write("**부서별 세부 목록**")
    
    table_data = []
    for dept in department_list:
        table_data.append({
            "부서명": dept[0],
            "핵심 역량": dept[1],
            "주요 업무": dept[2]
        })
    
    st.table(table_data)

    # 한 줄 띄우고 부서 성향 맞춤 점수 출력
    st.write("")
    st.metric(label="부서 성향 맞춤 점수", value=f"{score}점")
