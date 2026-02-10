import streamlit as st
st.markdown(
    """
    <style>
    /* Стили для кнопки сайдбара */
    [data-testid="stSidebarCollapseButton"] {
        width: 10vw; 
        height: 10vw;
        min-width: 50px;
        min-height: 50px;
        background-color: blue; /* Синий цвет */
        color: white;
        border-radius: 2vw;
    }

    [data-testid="stSidebarCollapseButton"] svg {
        fill: white; /* Цвет самой стрелочки */
        width: 20vw;
        height: 20vw;
        min-width: 100px;
    }

    /* Ховер-эффект */
    [data-testid="stSidebarCollapseButton"]:hover {
        background-color: blue;
        border: 2px solid #ffffff;
    }
    </style>
    """,
    unsafe_allow_html=True
)

about_us = st.Page("pages/About_us.py", title="О нас")
buy_page = st.Page("pages/Buy_page.py", title="Покупка")
main_page = st.Page("pages/main_page.py", title="Главная")
pg = st.navigation([main_page, about_us, buy_page])

pg.run()


