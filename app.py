import streamlit as st
import random
import urllib.parse

# 1. 페이지 설정
st.set_page_config(page_title="건대 점심 추천기", page_icon="🍴")

# 2. 식당 데이터베이스
menu_data = {
    "한식": ["돋음제", "개미집", "건대우동집", "이이요", "무대륙", "딸기공주", "원조할머니보쌈", "자양식당", "시골집", "순복이네", "할머니순대국", "고기굽는놈", "화기애애", "궁동칼국수"],
    "중식": ["송화산시도삭면", "매운향솥", "라화쿵부", "해룡마라소룡포", "복만루", "쿵푸소롱포", "백로식당", "차이니스퀴진", "시홍쓰", "홍매반점", "보배반점", "하이디라오"],
    "카레": ["아비꼬", "우츠와", "고메당", "호랭이카레", "옐로우스푼", "카레나이", "로얄인디아"],
    "기타": ["엘루이피자", "최가커피", "우화등선", "페스타마레", "미즈컨테이너", "바른면집", "감성타코", "포비", "핵밥", "스테이터", "민들레초밥", "호야초밥", "마실리아"]
}

st.title("🏫 건대 주변 오늘 뭐 먹지?")
st.write("메뉴 고민 끝! 버튼 하나로 점심 메뉴를 정해보세요.")

# 3. 사이드바 설정 (카테고리 및 예외 식당)
with st.sidebar:
    st.header("⚙️ 설정")
    category = st.selectbox("카테고리 선택", ["전체"] + list(menu_data.keys()))
    exclude_input = st.text_input("제외할 식당 (쉼표 구분)", "")
    exclude_list = [x.strip() for x in exclude_input.split(",") if x.strip()]

# 4. 필터링 로직
candidates = []
if category == "전체":
    for items in menu_data.values():
        candidates.extend(items)
else:
    candidates = menu_data[category]

final_list = [res for res in candidates if res not in exclude_list]

# 5. 메인 화면 추첨 버튼
if st.button("🍴 식당 추천받기!"):
    if not final_list:
        st.error("조건에 맞는 식당이 없습니다. 설정을 확인해 주세요!")
    else:
        selected = random.choice(final_list)
        st.balloons() # 축하 효과
        
        st.success(f"오늘의 추천 메뉴는? **[{selected}]** 입니다!")
        
        # 네이버 지도 링크 생성
        search_query = f"건대 {selected}"
        naver_url = f"https://map.naver.com/v5/search/{urllib.parse.quote(search_query)}"
        
        # 버튼 및 링크 제공
        st.link_button("📍 네이버 지도에서 보기", naver_url)
        
        # (선택 사항) 지도 하단에 표시
        st.info("링크를 클릭하면 네이버 지도로 연결됩니다.")

# 6. 하단 정보
st.markdown("---")
st.caption("건국대 언어교육원 식구들을 위한 맛집 랜덤 추천기 v1.0")