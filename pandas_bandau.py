from tarfile import data_filter
from turtledemo.penrose import start

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------
# pd.__version__
# pd.show_versions()

# --------------------------------------
# empty = pd.Series()
# print(empty)

# ---------------------------------------
# x =[1, 2, 3, 4, 5]
# y = pd.Series(x)
# print(y)

# ---------------------------------------
# x = pd.Series([1, 2, 3, 4, 5])
# x.name = "Skaiciai"
# print(x)

# ----------------------------------------
# x = pd.Series([1, 2, 3, 4, 5])
# x.index = ['a', 'b', 'c', 'd', 'e']
# print(x)

# -----------------------------------------
# x = pd.Series([20, 22, 53, 54, 65])
# pirmas_elementas = x.iloc[0]
# print(pirmas_elementas)

# -------------------------------------------
# x = pd.Series([20, 22, 53, 54, 65])
# viduriniai_elementai = x.iloc[1:-1]
# print(viduriniai_elementai)

# -------------------------------------------
# x = pd.Series([20, 22, 53, 54, 65])
# reversas = x.iloc[::-1]
# print(reversas)

# -------------------------------------------
# x = pd.Series([20, 22, 53, 54, 65])
# float = x.astype(float)
# print(float)

# --------------------------------------------
# x = pd.Series([20, 22, 53, 54, 65])
# x.iloc[0], x.iloc[-1] = x.iloc[-1], x.iloc[0]
# print(x)

# --------------------------------------------
# x = pd.Series([20, 22, 53, 54, 65])
# didejimo_tvarka = x.sort_values()
# print(didejimo_tvarka)

# -----------------------------------------------
# x = pd.Series([20, 22, 53, 54, 65])
# x += 5
# # arba
# # x = x+5
# print(x)

# -------------------------------------------------
# x = pd.Series([20, 22, 53, 54, 65])
# x[:]=5
# print(x)

# ----------------------------------------------------
# x = pd.Series([20, 22, 53, 54, 65])
# x[2]=10
# print(x)

# ------------------------------------------------------
# x = pd.Series([20, -22, 53, -54, -65, 5, 13, 15])
# print(x.loc[x<0])

# ------------------------------------------------------
# x = pd.Series([20, -22, 53, -54, -65, 5, 13, 15])
# print(x.loc[x>10])

# ------------------------------------------------------
# x = pd.Series([20, -22, 53, -54, -65, 5, 13, 15])
# mean_value = x.mean()
# print(f'Vidurkis: {mean_value}')
# print(f'Daugiau negu vidurkis:\n{x.loc[x>mean_value]}')

# --------------------------------------------------------
# x = pd.Series([20, -22, 53, -54, -65, 5, 13, 15])
# y = pd.Series([20, -22, 53, 0, -65, 5, 13, 15])
# result = (x != 0).all()
# result1 = (y != 0).all()
# print(result)
# print(result1)

# ---------------------------------------------------------
# x = pd.Series([20, -22, 53, -54, -65, 5, 13, 15])
# sum = x.sum()
# print(sum)

# ----------------------------------------------------------
# x = pd.Series([20, -22, 53, -54, -65, 5, 13, 15])
# max = x.max()
# min = x.min()
# print(max, min)

# ------------------------------------------------------------
# empty = pd.DataFrame()
# print(empty)

# ------------------------------------------------------------
# marvel_data = [
#     ['Spider-Man', 'male', 1962],
#     ['Captain America', 'male', 1941],
#     ['Wolverine', 'male', 1974],
#     ['Iron Man', 'male', 1963],
#     ['Thor', 'male', 1963],
#     ['Thing', 'male', 1961],
#     ['Mister Fantastic', 'male', 1961],
#     ['Hulk', 'male', 1962],
#     ['Beast', 'male', 1963],
#     ['Invisible Woman', 'female', 1961],
#     ['Storm', 'female', 1975],
#     ['Namor', 'male', 1939],
#     ['Hawkeye', 'male', 1964],
#     ['Daredevil', 'male', 1964],
#     ['Doctor Strange', 'male', 1963],
#     ['Hank Pym', 'male', 1962],
#     ['Scarlet Witch', 'female', 1964],
#     ['Wasp', 'female', 1963],
#     ['Black Widow', 'female', 1964],
#     ['Vision', 'male', 1968],
# ]
# df = pd.DataFrame(marvel_data)
# print(df)
#
# # --------------------------------------------------
# marvel_data = [
#     ['Spider-Man', 'male', 1962],
#     ['Captain America', 'male', 1941],
#     ['Wolverine', 'male', 1974],
#     ['Iron Man', 'male', 1963],
#     ['Thor', 'male', 1963],
#     ['Thing', 'male', 1961],
#     ['Mister Fantastic', 'male', 1961],
#     ['Hulk', 'male', 1962],
#     ['Beast', 'male', 1963],
#     ['Invisible Woman', 'female', 1961],
#     ['Storm', 'female', 1975],
#     ['Namor', 'male', 1939],
#     ['Hawkeye', 'male', 1964],
#     ['Daredevil', 'male', 1964],
#     ['Doctor Strange', 'male', 1963],
#     ['Hank Pym', 'male', 1962],
#     ['Scarlet Witch', 'female', 1964],
#     ['Wasp', 'female', 1963],
#     ['Black Widow', 'female', 1964],
#     ['Vision', 'male', 1968],
# ]
# df = df.rename({0:"name", 1:"sex", 2:"date"}, axis=1)
# print(df)

# --------------------------------------------------------------
# marvel_data = [
#     ['Spider-Man', 'male', 1962],
#     ['Captain America', 'male', 1941],
#     ['Wolverine', 'male', 1974],
#     ['Iron Man', 'male', 1963],
#     ['Thor', 'male', 1963],
#     ['Thing', 'male', 1961],
#     ['Mister Fantastic', 'male', 1961],
#     ['Hulk', 'male', 1962],
#     ['Beast', 'male', 1963],
#     ['Invisible Woman', 'female', 1961],
#     ['Storm', 'female', 1975],
#     ['Namor', 'male', 1939],
#     ['Hawkeye', 'male', 1964],
#     ['Daredevil', 'male', 1964],
#     ['Doctor Strange', 'male', 1963],
#     ['Hank Pym', 'male', 1962],
#     ['Scarlet Witch', 'female', 1964],
#     ['Wasp', 'female', 1963],
#     ['Black Widow', 'female', 1964],
#     ['Vision', 'male', 1968],
# ]
# df = pd.DataFrame(marvel_data, columns=['name', 'sex', 'date'])
# df.set_index("name", inplace=True, verify_integrity=True)
# print(df.head())
# print(df.tail())
# print(df['sex'].head())

# ---------------------------------------------------------
# marvel_data = [
#     ['Spider-Man', 'male', 1962],
#     ['Captain America', 'male', 1941],
#     ['Wolverine', 'male', 1974],
#     ['Iron Man', 'male', 1963],
#     ['Thor', 'male', 1963],
#     ['Thing', 'male', 1961],
#     ['Mister Fantastic', 'male', 1961],
#     ['Hulk', 'male', 1962],
#     ['Beast', 'male', 1963],
#     ['Invisible Woman', 'female', 1961],
#     ['Storm', 'female', 1975],
#     ['Namor', 'male', 1939],
#     ['Hawkeye', 'male', 1964],
#     ['Daredevil', 'male', 1964],
#     ['Doctor Strange', 'male', 1963],
#     ['Hank Pym', 'male', 1962],
#     ['Scarlet Witch', 'female', 1964],
#     ['Wasp', 'female', 1963],
#     ['Black Widow', 'female', 1964],
#     ['Vision', 'male', 1968],
# ]
# df = pd.DataFrame(marvel_data, columns=['name', 'sex', 'date'])
# df.set_index("name", inplace=True, verify_integrity=True)
# first_element = df.head(1)
# last_element = df.tail(1)
# print(first_element)
# print(last_element)

# ------------------------------------------------------
# marvel_data = [
#     ['Spider-Man', 'male', 1962],
#     ['Captain America', 'male', 1941],
#     ['Wolverine', 'male', 1974],
#     ['Iron Man', 'male', 1963],
#     ['Thor', 'male', 1963],
#     ['Thing', 'male', 1961],
#     ['Mister Fantastic', 'male', 1961],
#     ['Hulk', 'male', 1962],
#     ['Beast', 'male', 1963],
#     ['Invisible Woman', 'female', 1961],
#     ['Storm', 'female', 1975],
#     ['Namor', 'male', 1939],
#     ['Hawkeye', 'male', 1964],
#     ['Daredevil', 'male', 1964],
#     ['Doctor Strange', 'male', 1963],
#     ['Hank Pym', 'male', 1962],
#     ['Scarlet Witch', 'female', 1964],
#     ['Wasp', 'female', 1963],
#     ['Black Widow', 'female', 1964],
#     ['Vision', 'male', 1968],
# ]
# df = pd.DataFrame(marvel_data, columns=['name', 'sex', 'date'])
# df.set_index("name", inplace=True, verify_integrity=True)
# df.at['Vision', 'date']=1964
# # print(df.loc['Vision'])
# start_after_1970 = df[df['date']>1970]
# print(start_after_1970)

# -------------------------------------------------
# marvel_data = [
#     ['Spider-Man', 'male', 1962],
#     ['Captain America', 'male', 1941],
#     ['Wolverine', 'male', 1974],
#     ['Iron Man', 'male', 1963],
#     ['Thor', 'male', 1963],
#     ['Thing', 'male', 1961],
#     ['Mister Fantastic', 'male', 1961],
#     ['Hulk', 'male', 1962],
#     ['Beast', 'male', 1963],
#     ['Invisible Woman', 'female', 1961],
#     ['Storm', 'female', 1975],
#     ['Namor', 'male', 1939],
#     ['Hawkeye', 'male', 1964],
#     ['Daredevil', 'male', 1964],
#     ['Doctor Strange', 'male', 1963],
#     ['Hank Pym', 'male', 1962],
#     ['Scarlet Witch', 'female', 1964],
#     ['Wasp', 'female', 1963],
#     ['Black Widow', 'female', 1964],
#     ['Vision', 'male', 1968],
# ]
# df = pd.DataFrame(marvel_data, columns=['name', 'sex', 'date'])
# df.set_index("name", inplace=True, verify_integrity=True)
# # statistics = df.describe()
# # print(statistics)
#
# # mean_date = df['date'].mean()
# # print(mean_date)
#
# # min_date = df['date'].min()
# # print(min_date)
#
# min_date = df['date'].min()
# full_info = df[df['date'] == min_date]
# print(full_info)

# --------------------------------------------
marvel_data = [
    ['Spider-Man', 'male', 1962],
    ['Captain America', 'male', 1941],
    ['Wolverine', 'male', 1974],
    ['Iron Man', 'male', 1963],
    ['Thor', 'male', 1963],
    ['Thing', 'male', 1961],
    ['Mister Fantastic', 'male', 1961],
    ['Hulk', 'male', 1962],
    ['Beast', 'male', 1963],
    ['Invisible Woman', 'female', 1961],
    ['Storm', 'female', 1975],
    ['Namor', 'male', 1939],
    ['Hawkeye', 'male', 1964],
    ['Daredevil', 'male', 1964],
    ['Doctor Strange', 'male', 1963],
    ['Hank Pym', 'male', 1962],
    ['Scarlet Witch', 'female', 1964],
    ['Wasp', 'female', 1963],
    ['Black Widow', 'female', 1964],
    ['Vision', 'male', 1968],
]
df = pd.DataFrame(marvel_data, columns=['name', 'sex', 'date'])
df.set_index("name", inplace=True, verify_integrity=True)
reset= df.reset_index()
# print(reset)

# df['date'].plot(kind='hist', color='blue')

df['date'].plot.hist(color="skyblue", edgecolor="blue")
plt.grid(True, linestyle='--', alpha=0.3,)
plt.title('Informacija apie filmu pasirodymo data', fontweight='bold')
plt.xlabel('Pasirodymo metai')
plt.ylabel("Filmu kiekis")
plt.show()