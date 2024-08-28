import streamlit as st

st.title("위젯")


st.divider()  # 가로 긴 줄 구분선


# 클릭 시 if문을 실행
st.button('Reset', type='primary')    # 버튼 type='secondary' 가 기본값임.
if st.button('activate'):    # 버튼 클릭되면 True를 반환함.
    st.write('button activated')


st.divider()  # 가로 긴 줄 구분선


# checkbox
active = st.checkbox('I agree')

if active:
    st.text('Great!')


st.divider()  # 가로 긴 줄 구분선


# toggle
toggle = st.toggle(
    'Turn on the switch!', value=True
)

if toggle:
    st.text('Switch is turned on!')
else:
    st.text('Switch is turned off!')


st.divider()  # 가로 긴 줄 구분선


# selectbox
option = st.selectbox(
    label='your selection is',
    options=['Car', 'Airplane', 'Train', 'Ship'],
)
st.text('you selected: {}'.format(option))


st.divider()  # 가로 긴 줄 구분선


# selectbox placeholder 활용
option = st.selectbox(
    label='your selection is',
    options=['Car', 'Airplane', 'Train', 'Ship'],
    index=None,
    placeholder='select transportation'
)
st.text('you selected: {}'.format(option))


st.divider()  # 가로 긴 줄 구분선


# radio
option = st.radio(
    'What is your favorite movie genre',
    ["Comedy", "Drama", "Documentary"],
    captions = ['Laugh out loud', 'Get the popcorn', 'Never stop learning']
)

if option:
    st.text('You Selected {}'.format(option))


st.divider()  # 가로 긴 줄 구분선


# multiselect
option = st.multiselect(
    label='your selection is',
    options=['Car', 'Airplane', 'Train', 'Ship'],
    placeholder='select transportation'
)
st.text('you selected: {}'.format(option))


st.divider()  # 가로 긴 줄 구분선


# slider
score = st.slider('Your score is...', 0, 100, 1)    # 레이블, 최소값, 최대값, 간격
st.text('Score: {}'.format(score))


st.divider()  # 가로 긴 줄 구분선


# 날짜 및 시간 slider
from datetime import time

start_time, end_time = st.slider(
    'Working time is...',
    min_value=time(0), max_value=time(23),
    value=(time(8), time(18)),
    format='HH:mm'
)
st.text('Working time: {}, {}'.format(start_time, end_time))


st.divider()  # 가로 긴 줄 구분선


# text input
string = st.text_input(
    'Movie title', placeholder='write down the title of your favorite movie'
)

if string:
    st.text('Your answer is '+string)


st.divider()  # 가로 긴 줄 구분선


# password 인자 활용
string = st.text_input(
    'Movie title',
    placeholder='write down the title of your favorite movie',
    type='password'
)

if string:
    st.text('Your answer is '+string)


st.divider()  # 가로 긴 줄 구분선


# file uploader
import pandas as pd

file = st.file_uploader(
    'Choose a file', type='csv', accept_multiple_files=False
)
if file is not None:
    df = pd.read_csv(file)
    st.write(df)

