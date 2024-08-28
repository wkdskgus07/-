import streamlit as st

# --- PAGE SETUP ---
# https://fonts.google.com/icons
about_page = st.Page(
    page="views/about_me.py",
    title="About Me",
    icon=":material/account_circle:",
    default=True,
)
project_1_page = st.Page(
    page="views/sales_dashboard.py",
    title="Sales Dashboard",
    icon=":material/bar_chart:",
)
project_2_page = st.Page(
    page="views/chatbot.py",
    title="Chat Bot",
    icon=":material/smart_toy:",
)

test1_page = st.Page(
    page="views/test1.py",
    title="텍스트",
    icon=":material/sentiment_satisfied:",
)
test2_page = st.Page(
    page="views/test2.py",
    title="위젯",
    icon=":material/sentiment_satisfied:",
)
test3_page = st.Page(
    page="views/test3.py",
    title="스트림릿 테스트 3",
    icon=":material/sentiment_satisfied:",
)
test4_page = st.Page(
    page="views/test4.py",
    title="스트림릿 테스트 4",
    icon=":material/sentiment_satisfied:",
)
test5_page = st.Page(
    page="views/test5.py",
    title="스트림릿 테스트 5",
    icon=":material/sentiment_satisfied:",
)


# --- NAVIGATION SETUP [WITHOUT SECTIONS] ---
# pg = st.navigation(pages=[about_page, project_1_page, project_2_page])

# --- NAVIGATION SETUP [WITH SECTIONS] ---
pg = st.navigation({
    "Info": [about_page],
    "Projects": [project_1_page, project_2_page],
    "스트림릿 연습": [test1_page, test2_page, test3_page, test4_page, test5_page],
})

# --- SHARED ON ALL PAGES ---
st.logo("assets/myLogo.png")
st.sidebar.text("Made with ❤ by SW")

# --- RUN NAVIGATION ---
pg.run()
