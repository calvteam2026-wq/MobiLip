import streamlit as st
st.markdown("""
<style>
/* Кнопка сворачивания sidebar */
button[kind="header"] svg {
    width: 10vw;
    height: 10vw;
}

/* Увеличение кликабельной области */
button[kind="header"] {
    padding: 10vw;
}
</style>
""", unsafe_allow_html=True)

about_us = st.Page("pages/About_us.py", title="О нас")
buy_page = st.Page("pages/Buy_page.py", title="Покупка")
main_page = st.Page("pages/main_page.py", title="Главная")
pg = st.navigation([main_page, about_us, buy_page])

pg.run()






