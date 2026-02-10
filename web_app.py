import streamlit as st
st.markdown("""
<style>
/* Когда sidebar открыт */
[data-testid="stSidebarCollapseButton"] * {
    transform: scale(1.6) !important;
    transform-origin: center;
}

/* Когда sidebar закрыт (кнопка покоя) */
[data-testid="stSidebarExpandButton"] * {
    transform: scale(1.6) !important;
    transform-origin: left;
}
</style>
""", unsafe_allow_html=True)
about_us = st.Page("pages/About_us.py", title="О нас")
buy_page = st.Page("pages/Buy_page.py", title="Покупка")
main_page = st.Page("pages/main_page.py", title="Главная")
pg = st.navigation([main_page, about_us, buy_page])

pg.run()











