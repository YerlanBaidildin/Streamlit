import streamlit as st
import pandas as pd
import math
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns



st.write("""
         ## Количество браков и разводов в США в период с 1867 по 2010 годы
         """)




us_marriage_divorce_data = pd.read_csv('https://raw.githubusercontent.com/rhiever/python-data-visualization-course/master/Section%203%20-%20Data%20visualization%20in%20Python%20-%20matplotlib/exercises/data/us-marriages-divorces-1867-2014.csv', sep = ',')

plt.rcParams['figure.dpi'] = 150
plt.style.use('ggplot') # style
plt.figure(figsize = (6, 3), dpi = 500)
df = us_marriage_divorce_data[(us_marriage_divorce_data['Year'] > 1866) & (us_marriage_divorce_data['Year'] <2011)]
year_x = df['Year']
marriages_y = df['Marriages']
divorces_y = df['Divorces']
plt.xlabel('Year')
plt.ylabel('Marriages & Divorces')
plt.plot(year_x, marriages_y, '-g', label = 'Marriages')
plt.plot(year_x, divorces_y, '-b', label = 'Divorces')
plt.legend()

st.pyplot(plt)


st.write("""
         
         
         ## Самые "смертоносные" актеры Голливуда
         """)
plt.rcParams['figure.dpi'] = 150
hollywood_actor_kills = pd.read_csv('actor_kill_counts.csv', sep =',')
grups = hollywood_actor_kills['Actor']
colums = hollywood_actor_kills['Count']

plt.barh(grups, colums, height=0.5, left=0.1)
plt.xlabel('kills')
plt.ylabel('Actors')

st.pyplot(plt)

