import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import time
st.markdown("""
        <style>
               .block-container {
                    padding-top: 1rem;
                    padding-bottom: 0rem;
                    padding-left: 1rem;
                    padding-right: 1rem;
                }
        </style>
        """, unsafe_allow_html=True)
# DESIGN implement changes to the standard streamlit UI/UX
st.set_page_config(page_title="MobiLip", layout="wide")

r1, r2, r3 = st.columns([3,4,1])
with r2:
    st.title('Оформление покупки')

FIO = st.text_input("Введите свое ФИО", "")
client_mail = st.text_input("Введите свою электронную почту", "")
client_number = st.text_input("Введите свой номер телефона", "")

st.write('Выберите количество товаров для заказа и оформите покупку')
col1, col2, col3, col4 = st.columns([1,1,1,1])
with col1:
    count_1 = st.number_input('Мышь №1', min_value=0, step=1)
with col2:
    count_2 = st.number_input('Мышь №2', min_value=0, step=1)
with col3:
    count_3 = st.number_input('Мундштук №1', min_value=0, step=1)
with col4:
    count_4 = st.number_input('Мундштук №2', min_value=0, step=1)


option = st.selectbox(
    "Выберите город для доставки:",
    (
        "Алматы", "Астана", "Шымкент", "Актау", "Актобе",
        "Атырау", "Караганда", "Кокшетау", "Костанай", "Кызылорда",
        "Павлодар", "Петропавловск", "Семей", "Талдыкорган",
        "Тараз", "Туркестан", "Уральск", "Усть-Каменогорск"
    ),
    index = None
)
client_adress = st.text_input("Введите свой адрес (улицу, дом, квартиру)", "")

col5, col6 = st.columns([1,1])
with col5:
    st.write("Товар будет доставлен в город: ", option if option!=None else '')


def send_email(recipient, message_text):
    sender = st.secrets["EMAIL"]
    password = st.secrets["EMAIL_PASSWORD"]

    msg = MIMEText(message_text, 'plain', 'utf-8')
    msg['Subject'] = Header('Новый заказ MobiLip', 'utf-8')
    msg['From'] = sender
    msg['To'] = recipient

    # Прямое выполнение без проверок
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender, password)
    server.sendmail(sender, recipient, msg.as_string())
    server.quit()

@st.dialog("Подтверждение покупки")
def check_buy(count_1, count_2, count_3, count_4, FIO, client_adress, client_mail, client_number, message):
    st.write("Проверьте данные и закончите покупку")
    st.write(f'ФИО: {FIO}')
    st.write(f'Почта покупателя: {client_mail}')
    st.write(f'Номер телефона: {client_number}')
    st.write(f'Мышь №1: {count_1} шт')
    st.write(f'Мышь №2: {count_2} шт')
    st.write(f'Мундштук №1: {count_3} шт')
    st.write(f'Мундштук №2: {count_4} шт')
    st.write(f'Город доставки: {option if option else "Не указан"}')
    st.write(f'Адрес: {client_adress}')
    if st.button("Потвердить"):
        recipient = 'matkulov.isabek@gmail.com' #напишите здесь кому из команды будет приходить сообщение
        send_email(recipient, message)

        message = f''' Уважаемый (ая) {FIO}, Вы оформили новый заказ:
                Мышь №1: {count_1} шт.
                Мышь №2: {count_2} шт.
                Мундштук №1: {count_3} шт.
                Мундштук №2: {count_4} шт.
                Город доставки: {option if option else 'Не указан'}.
                Адрес: {client_adress}.
                '''
        recipient = client_mail
        send_email(recipient, message)
        st.success("Заказ оформлен! Можете закрыть это окно.")



if st.button('Оформить покупку', type='primary'):
    if (count_1!=0 or count_2!=0 or count_3!=0 or count_4!=0) and FIO!='' and client_adress!='' and client_mail!='' and client_number!='':
        message = f"""
        Новый заказ:
        ФИО: {FIO}.
        Почта покупателя: {client_mail}.
        Номер телефона: {client_number}.
        Мышь №1: {count_1} шт.
        Мышь №2: {count_2} шт.
        Мундштук №1: {count_3} шт.
        Мундштук №2: {count_4} шт.
        Город доставки: {option if option else 'Не указан'}.
        Адрес: {client_adress}.
        """
        check_buy(count_1, count_2, count_3, count_4, FIO, client_adress, client_mail, client_number, message)
    else:
        with col6:
            placeholder = st.empty()  # Создаем пустое место в интерфейсе
            placeholder.badge("Недостаточно данных!", color="red") # Пишем туда сообщение
            time.sleep(4)  # Ждем 4 секунд
            placeholder.empty()



