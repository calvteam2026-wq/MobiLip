import streamlit as st
st.markdown(
    """
    <style>
    /* Находим кнопку по атрибуту data-testid */
    [data-testid="stSidebarCollapseButton"] {
        background-color: #ff4b4b; /* Цвет фона кнопки */
        color: white;             /* Цвет самой стрелочки */
        border-radius: 50%;       /* Сделать её круглой */
        width: 10vw;              /* Ширина */
        height: 10vw;             /* Высота */
    }

    /* Эффект при наведении */
    [data-testid="stSidebarCollapseButton"]:hover {
        background-color: #ff1f1f;
        transform: scale(1.5);    /* Немного увеличиваем при наведении */
    }

    /* Изменение размера самой иконки (стрелочки) внутри кнопки */
    [data-testid="stSidebarCollapseButton"] svg {
        width: 40vw;
        height: 40vw;
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





