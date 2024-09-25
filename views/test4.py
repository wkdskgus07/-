import streamlit as st


st.title("체질량 지수 BMI를 확인해 보세요! 확인할 자신 있나봐?ㅋ")
st.divider()

height = st.text_input(
    '키(m)', placeholder='키를 입력하세요. (단위: m)'
)

weight = st.text_input(
    '몸무게(kg)', placeholder='몸무게를 입력하세요. (단위: kg)'
)

if st.button("BMI 계산하기") :
    if height == '' or weight == '':
        st.error('키와 몸무게를 입력해주세요!')
    else:
        height = float(height)
        weight = float(weight)

        # bmi = 몸무게 / 키*키
        bmi = round(weight / height**2, 1)
        bmi_icon = "■"
        
        # 고도 비만: 35 이상
        # 중도 비만(2단계 비만): 30 ~ 34.9
        # 경도 비만(1단계 비만): 25 ~ 29.9 (30 미만)
        # 정상: 18.5 ~ 24.9 (25 미만)
        # 저체중: 18.5 미만
        if bmi < 18.5 :
            st.header(bmi_icon)
            st.subheader("대벌레와 다름없는 저체중입니다!")
        elif bmi < 25 :
            st.header(bmi_icon * 2)
            st.subheader("정상입니다.")
        elif bmi < 30 :
            st.header(bmi_icon * 3)
            st.subheader("다이어트 살짝 한 돼지같은 경도 비만입니다!")
        elif bmi < 35 :
            st.header(bmi_icon * 4)
            st.subheader("돼지네. 중도 비만입니다!")
        else :
            st.header(bmi_icon * 5)
            st.subheader("죽기 직전인 고도 비만입니다! 딩징 살빼")


