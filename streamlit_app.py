import streamlit as st
import mysql.connector
import  matplotlib.pyplot as plt

# ---------------------------------------------------------------
# st.write("demo pristatymo vaizdas")
#
# name = st.text_input("prisistatyk!")
# age = st.number_input("kiek tau metu?")
# st.write(f'labas {name} kuriam yra {age} metu')

# ------------------------------------------------------------------
st.title("Prekiu analize")

grafiko_pasirinkimas =st.selectbox('Pasirinkite grafika', ['Kainos ir pavadinimai', 'Kategorijos ir kiekiai'])
if grafiko_pasirinkimas == 'Kainos ir pavadinimai':
    conn = mysql.connector.connect(
        host = "127.0.0.1",
        user = "root",
        password = "",
        database = "supermarketai"
    )

    c=conn.cursor()

    c.execute('select title, price from product where title like "%griki%"')
    result =c.fetchall()

    titles = [row[0] for row in result]
    prices = [row[1] for row in result]

    titles = [title if len(title) <= 15 else title[:10] + '...' for title in titles]

    sorted_prices = sorted(zip(prices, titles))
    min_prices = sorted_prices[:3]
    max_prices =sorted_prices[-3:]
    rodyti_pigiausias = st.checkbox("Rodyti tris pigiausias prekes")
    rodyti_brangiausias = st.checkbox("Rodyti tris brangiausias prekes")
    if rodyti_pigiausias:
        st.subheader("Trys pigiausios prekes:")
        for price, title in min_prices:
            st.write(f'{title} {price} eur')
    if rodyti_brangiausias:
        st.subheader("Trys brangiausios prekes:")
        for price, title in max_prices:
            st.write(f'{title} {price} eur')

    colors = []
    for price, title in zip(prices, titles):
        if (price, title) in min_prices and rodyti_pigiausias:
            colors.append('green')
        elif (price, title) in max_prices and rodyti_brangiausias:
            colors.append('red')
        else:
            colors.append('blue')

    plt.bar(titles, prices, color=colors)
    plt.xticks(rotation=90)
    plt.tight_layout()
    st.pyplot(plt)
else:
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="supermarketai"
    )
    c=conn.cursor()
    c.execute('select category2, count(*) from categories group by category2 ')
    result =c.fetchall()


    prekiu_kategorijos = [row[0] for row in result]
    prekiu_kiekis = [row[1] for row in result]

    prekiu_kategorijos = [title if len(title) <= 15 else title[:12] + '...' for title in prekiu_kategorijos]

    Rodyti_vidurkio_linija = st.checkbox('Rodyti prekiu kiekio vidurio linija')
    vidurkis = round(sum(prekiu_kiekis)/len(prekiu_kiekis),2)
    if Rodyti_vidurkio_linija:
        plt.axhline(y=vidurkis, color='red', linestyle='--', label=f'Prekiu kiekio vidurkis:{vidurkis}')

    bars = plt.bar(prekiu_kategorijos, prekiu_kiekis)
    plt.xticks(rotation=90, fontsize=7)
    plt.ylim(0, max(prekiu_kiekis) *1.1)
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval + 0.1, f'{int(yval)}', ha='center', va='bottom',fontsize=7)

    plt.legend()
    plt.tight_layout()
    st.pyplot(plt)


