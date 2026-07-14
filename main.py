import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="MBTI 직업 & 포켓몬 추천",
    page_icon="🔮",
    layout="centered"
)

# MBTI 데이터 구축 (직업, 추천 포켓몬 이름, 포켓몬 번호, 매칭 이유)
# 이미지 URL은 공식 PokeAPI 기반 고화질 GitHub 이미지 주소를 사용합니다.
mbti_db = {
    "ISTJ": {
        "job": "회계사, 공무원, 분석가",
        "pokemon": "꼬부기 (Squirtle)",
        "img_id": "0007",
        "reason": "신중하고 책임감이 강하며 규칙을 잘 준수하는 성격이 ISTJ와 닮았습니다."
    },
    "ISFJ": {
        "job": "간호사, 초등교사, 사회복지사",
        "pokemon": "다부니 (Audino)",
        "img_id": "0531",
        "reason": "타인을 돌보고 헌신하며 따뜻한 마음을 가진 최고의 서포터입니다."
    },
    "INFJ": {
        "job": "심리상담사, 작가, 예술가",
        "pokemon": "가디안 (Gardevoir)",
        "img_id": "0282",
        "reason": "상대방의 마음을 잘 헤아리고 깊은 통찰력을 지닌 신비로운 포켓몬입니다."
    },
    "INTJ": {
        "job": "소프트웨어 개발자, 시스템 분석가, 전략가",
        "pokemon": "메타그로스 (Metagross)",
        "img_id": "0376",
        "reason": "네 개의 뇌가 결합되어 슈퍼컴퓨터 이상의 연산 능력을 자랑하는 이성적이고 철저한 전략가입니다."
    },
    "ISTP": {
        "job": "엔지니어, 카레이서, 정비사",
        "pokemon": "코일 (Magnemite)",
        "img_id": "0081",
        "reason": "기계적 원리에 관심이 많고 과묵하지만 실용적인 능력이 뛰어납니다."
    },
    "ISFP": {
        "job": "예술가, 작곡가, 패션 디자이너",
        "pokemon": "루브도 (Smeargle)",
        "img_id": "0235",
        "reason": "꼬리 끝의 액체로 그림을 그리며 예술적 감각과 개성이 넘치는 예술가입니다."
    },
    "INFP": {
        "job": "소설가, 일러스트레이터, 상담가",
        "pokemon": "이브이 (Eevee)",
        "img_id": "0133",
        "reason": "잠재력과 가능성이 무한하며, 평화롭고 상상력이 풍부한 성향을 가졌습니다."
    },
    "INTP": {
        "job": "연구원, 철학자, 프로그래머",
        "pokemon": "후딘 (Alakazam)",
        "img_id": "0065",
        "reason": "IQ 5000에 달하며 논리적 분석과 깊은 연구를 즐기는 두뇌형 포켓몬입니다."
    },
    "ESTP": {
        "job": "경찰관, 소방관, 사업가",
        "pokemon": "루카리오 (Lucario)",
        "img_id": "0448",
        "reason": "순발력이 뛰어나고 실전 전투에 강하며 활동적이고 역동적인 해결사입니다."
    },
    "ESFP": {
        "job": "연예인, 이벤트 기획자, 승무원",
        "pokemon": "피카츄 (Pikachu)",
        "img_id": "0025",
        "reason": "누구나 사랑하는 스타성을 지녔으며, 활기차고 사교적인 성격의 아이콘입니다."
    },
    "ENFP": {
        "job": "홍보 전문가, 마케터, 크리에이터",
        "pokemon": "뮤 (Mew)",
        "img_id": "0151",
        "reason": "호기심이 넘쳐나고 자유로운 영혼이며 언제나 새로운 재미를 추구합니다."
    },
    "ENTP": {
        "job": "발명가, 변호사, 기획자",
        "pokemon": "팬텀 (Gengar)",
        "img_id": "0094",
        "reason": "장난기 가득하고 창의적이며 기존의 틀을 깨는 기발한 아이디어를 자랑합니다."
    },
    "ESTJ": {
        "job": "프로젝트 매니저, 경영자, 경찰 간부",
        "pokemon": "윈디 (Arcanine)",
        "img_id": "0059",
        "reason": "위풍당당하고 리더십이 뛰어나며 체계적이고 약속을 철저히 지키는 듬직한 대장입니다."
    },
    "ESFJ": {
        "job": "초등교사, 비서, 홍보 담당자",
        "pokemon": "해피너스 (Blissey)",
        "img_id": "0242",
        "reason": "친절과 온정이 넘치며 주변 분위기를 조화롭고 행복하게 만들어줍니다."
    },
    "ENFJ": {
        "job": "정치인, 교사, 인적자원 전문가",
        "pokemon": "토게키스 (Togekiss)",
        "img_id": "0468",
        "reason": "은혜와 평화를 베풀며 주위 사람들을 이끌어 성장시키는 이타적인 리더입니다."
    },
    "ENTJ": {
        "job": "CEO, 경영 컨설턴트, 벤처 캐피탈리스트",
        "pokemon": "리자몽 (Charizard)",
        "img_id": "0006",
        "reason": "강한 의지와 열정, 그리고 주도적인 에너지로 목표를 향해 무섭게 돌진합니다."
    }
}

# 메인 타이틀
st.title("🔮 MBTI 맞춤형 직업 & 포켓몬 추천기")
st.write("나의 MBTI를 선택하고, 그에 어울리는 추천 직업과 소울메이트 포켓몬을 확인해 보세요!")

st.divider()

# 레이아웃 구성
col1, col2 = st.columns([1, 2])

with col1:
    # MBTI 드롭다운 선택
    mbti_list = sorted(list(mbti_db.keys()))
    selected_mbti = st.selectbox("당신의 MBTI를 선택하세요", mbti_list)

# 선택된 MBTI 정보 추출
info = mbti_db[selected_mbti]
img_url = f"https://raw.githubusercontent.com/HybridShivam/Pokemon/master/assets/images/{info['img_id']}.png"

with col2:
    st.subheader(f"✨ {selected_mbti}의 어울리는 직업")
    st.info(f"👉 **{info['job']}**")

st.divider()

# 결과 출력 영역
st.subheader(f"🐣 {selected_mbti}의 소울메이트 포켓몬")

# 이미지와 추천 이유를 좌우로 배치
col_img, col_text = st.columns([1, 1.5])

with col_img:
    st.image(img_url, caption=info['pokemon'], use_container_width=True)

with col_text:
    st.markdown(f"### **{info['pokemon']}**")
    st.success(f"**어울리는 이유:**\n\n{info['reason']}")
