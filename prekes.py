import mysql.connector
import  matplotlib.pyplot as plt

conn = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "",
    database = "supermarketai"
)

c=conn.cursor()

# ----------------------------------------------------------------------------

# c.execute('select title, price from product where title like "%griki%"')
# result =c.fetchall()
# print(result)
#
# titles = [row[0] for row in result]
# prices = [row[1] for row in result]
#
# titles = [title if len(title) <= 15 else title[:10] + '...' for title in titles]
# plt.bar(titles, prices)
# plt.xticks(rotation=90)
# plt.tight_layout()
# plt.show()

# -----------------------------------------------------------------------------------

# c.execute('select category2, count(*) from categories group by category2 ')
# result =c.fetchall()
# print(result)
#
# prekiu_kategorijos = [row[0] for row in result]
# prekiu_kiekis = [row[1] for row in result]
#
# prekiu_kategorijos = [title if len(title) <= 15 else title[:12] + '...' for title in prekiu_kategorijos]
#
# vidurkis = round(sum(prekiu_kiekis)/len(prekiu_kiekis),2)
# plt.axhline(y=vidurkis, color='red', linestyle='--', label=f'Prekiu kiekio vidurkis:{vidurkis}')
#
# bars = plt.bar(prekiu_kategorijos, prekiu_kiekis)
# plt.xticks(rotation=90, fontsize=7)
# plt.ylim(0, max(prekiu_kiekis) *1.1)
# for bar in bars:
#     yval = bar.get_height()
#     plt.text(bar.get_x() + bar.get_width() / 2, yval + 0.1, f'{int(yval)}', ha='center', va='bottom',fontsize=7)
#
# plt.legend()
# plt.tight_layout()
# plt.show()

# ------------------------------------------------------------------------

