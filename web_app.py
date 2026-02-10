import streamlit as st
st.markdown("""
<style>
[data-testid="stSidebarExpandButton"] svg,
[data-testid="stSidebarCollapseButton"] svg {
    width: 150px !important;
    height: 150px !important;
}
</style>
""", unsafe_allow_html=True)
about_us = st.Page("pages/About_us.py", title="О нас")
buy_page = st.Page("pages/Buy_page.py", title="Покупка")
main_page = st.Page("pages/main_page.py", title="Главная")
pg = st.navigation([main_page, about_us, buy_page])

pg.run()













