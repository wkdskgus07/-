import streamlit as st
import random

#게임 결과 내는 함수. guessNum은 사람 추측값 0(앞면), 1(뒷면)
def playGame(guessNum):
 comNum = random.randint(0,1)
 if comNum == guessNum:
  st.write('정답이다.')
 else:
  st.write('풉ㅋ 이걸 틀리네. 이제 넌 살아서 나갈 수 없다.')

st.title("동전 던지기 게임")
st.divider()

st.image('assets/coin_head.png')
st.image('assets/coin_tail.png')

st.subheader('앞면과 뒷면 중 고르지 않는다면 넌 살아서 나갈 수 없다.')


if st.button('앞면'):
  playGame(0)
if st.button('뒷면'):
 playGame(1)


col1, col2 = st.columns(2)
col1.write('동전 앞면')
col2.write('동전 뒷면')

with col1:
    st.image('assets/coin_head.png')
with col2:
    st.image('assets/coin_tail.png')

st.header("동전 던지기 게임에 온 걸 환영한다. 게임을 시작하지.")
