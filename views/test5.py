import streamlit as st

# Declare characters
define e = Character("Eunha", color="#c8ffc8")
define j = Character("Jisoo", color="#ffc8c8")

# The game starts here.
label start:

    scene bg room
    show eunha happy

    e "안녕! 나의 이름은 은하야. 오늘은 너와 함께 시간을 보내고 싶어."

    j "안녕! 나는 지수야. 너와 만나서 반가워!"

    menu:
        "은하와 함께 시간을 보낸다.":
            jump hangout_eunha

        "지수와 함께 시간을 보낸다.":
            jump hangout_jisoo

label hangout_eunha:
    e "어디로 가고 싶어?"
    
    menu:
        "카페에 가자.":
            e "좋아! 카페에서 맛있는 커피를 마시자."
            jump cafe_scene

        "영화 보러 가자.":
            e "영화라니! 어떤 영화를 볼까?"
            jump movie_scene

label hangout_jisoo:
    j "어디에 가고 싶어?"
    
    menu:
        "공원에 가자.":
            j "좋아! 공원에서 산책하자."
            jump park_scene

        "쇼핑하러 가자.":
            j "쇼핑도 좋지! 함께 가자."
            jump shopping_scene

label cafe_scene:
    scene bg cafe
    e "커피가 정말 맛있다!"
    return

label movie_scene:
    scene bg theater
    e "이 영화 정말 재밌다!"
    return

label park_scene:
    scene bg park
    j "공원이 정말 예쁘다!"
    return

label shopping_scene:
    scene bg shopping
    j "여기에서 정말 많은 것을 살 수 있어!"
    return


