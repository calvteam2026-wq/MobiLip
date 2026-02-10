import streamlit as st
st.set_page_config(page_title="MobiLip", layout="wide")
st.markdown("""
        <style>
               .block-container {
                    padding-top: 1rem;
                    padding-bottom: 0rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
        </style>
        """, unsafe_allow_html=True)

def circular_responsive_image(image_url):
    st.markdown(
        f"""
        <style>
        .circle-container {{
            width: 100%; /* Занимает всю ширину колонки */
            aspect-ratio: 1 / 1; /* Делает контейнер квадратным */
            overflow: hidden;
            border-radius: 50%;
            border: 0px solid #333;
        }}
        .circle-container img {{
            width: 100%;
            height: 100%;
            object-fit: cover;
        }}
        </style>
        <div class="circle-container">
            <img src="{image_url}">
        </div>
        """,
        unsafe_allow_html=True
    )
col1, col2, col3 = st.columns([2, 2, 1])
with col2:
    st.title('Наша команда')
    st.write('')

st.write('')
c1, c2, c3, c4 = st.columns([1,1,1,1])
with c1:
    circular_responsive_image('https://i.ibb.co.com/qbvNj1m/amirzhan.jpg')
    st.write('')
    with st.expander("Амиржан — TeamLead команды"):
        st.write('''
                    Окончил колледж по специальности слесарь КИПиА. Руководит
                    разработкой и отвечает за общую инженерную концепцию проекта.
                ''')

with c2:
    circular_responsive_image('https://i.ibb.co.com/zhc1thXj/issabek.jpg')
    st.write('')
    with st.expander("Исабек — 3D-моделист, дизайнер"):
        st.write('''
                    В проекте отвечает за 3D моделирование и проработку
                    конструкции устройства, а также занимается
                    организационными вопросами и переговорами. Интересуется
                    инженерными проектами и робототехникой, имеет опыт
                    работы в SOLIDWORKS, AutoCAD и Inventor, проходил
                    практику в сервисном отделе ТОО «Сайман».
                ''')

with c3:
    circular_responsive_image('https://i.ibb.co.com/4RV3bQHB/artur.jpg')
    st.write('')
    with st.expander("Артур — инженер-программист"):
        st.write('''
                        Инженер по встроенным системам
                        и ИИ, работает в лаборатории над
                        прикладными инженерными задачами.
                        Интересуется робототехникой и схемотехникой.
                    ''')


with c4:
    circular_responsive_image('https://i.ibb.co.com/QFfm6RtN/sergey.jpg')
    st.write('')
    with st.expander("Сергей — специалист по электронике"):
        st.write('''
                    Студент 3 курса специальности «Автоматизация и
                    управление», имеет опыт работы инженером КИПиА в ДСК GLB.
                    Интересуется промышленной автоматизацией и
                    электроникой, отвечает за сборку и аппаратную часть устройств.
                ''')

st.write('')
with c1:
    st.write('urazbekov2004@gmail.com')
with c2:
    st.write('matkulov.isabek@gmail.com')
with c3:
    st.write('artitopgo@gmail.com')
with c4:
    st.write('litvinovsergey2005@gmail.com')