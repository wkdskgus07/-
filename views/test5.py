import streamlit as st

# 캐릭터와 배경 설정
characters = {
    "e": "은하",
    "j": "지수"
}

# 게임의 흐름을 관리하는 함수
def main():
    st.title("미연시 게임")

    if "step" not in st.session_state:
        st.session_state.step = 0

    if st.session_state.step == 0:
        st.write("안녕! 나의 이름은 은하야. 오늘은 너와 함께 시간을 보내고 싶어.")
        st.write("안녕! 나는 지수야. 너와 만나서 반가워!")

        if st.button("은하와 함께 시간을 보낸다."):
            st.session_state.step = 1
        if st.button("지수와 함께 시간을 보낸다."):
            st.session_state.step = 2

    elif st.session_state.step == 1:
        st.write("어디로 가고 싶어?")
        if st.button("카페에 가자."):
            st.session_state.step = 3
        if st.button("영화 보러 가자."):
            st.session_state.step = 4

    elif st.session_state.step == 2:
        st.write("어디에 가고 싶어?")
        if st.button("공원에 가자."):
            st.session_state.step = 5
        if st.button("쇼핑하러 가자."):
            st.session_state.step = 6

    elif st.session_state.step == 3:
        st.write("커피가 정말 맛있다!")
        st.button("다시 시작하기", on_click=reset_game)

    elif st.session_state.step == 4:
        st.write("이 영화 정말 재밌다!")
        st.button("다시 시작하기", on_click=reset_game)

    elif st.session_state.step == 5:
        st.write("공원이 정말 예쁘다!")
        st.button("다시 시작하기", on_click=reset_game)

    elif st.session_state.step == 6:
        st.write("여기에서 정말 많은 것을 살 수 있어!")
        st.button("다시 시작하기", on_click=reset_game)

# 게임 상태를 초기화하는 함수
def reset_game():
    st.session_state.step = 0

if __name__ == "__main__":
    main()
