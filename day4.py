# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 10:13:22 2024

@author: rohit.kumar
"""

import streamlit as st
import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
import altair as alt
from datetime import time, datetime
from vega_datasets import data

st.header('st.write')
st.write('Hello *World!* :sunglasses:')
st.write(1234)

df = pd.DataFrame({'first column': [1, 2, 3, 4, 5],
                   'second column': [10, 20, 30, 40, 50]
                   })
df.index.name = 'sr.no'
st.write(df)
st.write('Below is a dataframe: ', df, 'Above is the dataframe')

df2 = pd.DataFrame(data=np.random.randn(200,3), 
                   columns=['a', 'b', 'c'])
h1 = alt.Chart(df2).mark_circle().encode(
    x = 'a', y = 'b', size = 'c', color = 'c', tooltip = ['a', 'b', 'c'])
st.write(h1)

st.text('I am a text string')

my_code = '''
            def my_function():
                print('Hello World!'')
            return print('done')
        '''

st.code(my_code, language='python')

st.latex(r''' 
         a + ar + ar^2 + ar^3 + \cdots + ar^{n-1} = 
         a * \sum_{k=0}^{n-1} ar^k = a \left( \frac{1-r^{n}}{1-r} \right)
         ''')
         
md = st.text_area('Type the text here (without outer quotes)',
                  "My name is Rohit Hedaoo :balloon:")
st.markdown(md)

multi = '''***I am writing this in***   
**two line**'''
st.markdown(multi)

st.caption("This is a caption :red[_ensure_] **to use it correctly** :boom:")

st.header("_This_ is a *Header* **in** :blue[Streamlet] :sunglasses:", divider='rainbow')
st.subheader('This is the Subheader', divider=True)

st.header('st.slider')
st.subheader('Slider')

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm, ", age, 'years old')

values = st.slider('Select a range of values', 0.0, 100.0, (25.0, 75.0))
st.write('Values: ', values)

st.subheader('Range time slider')

appointment = st.slider(
    'Scheduke your appointment:',
    value = (time(11,30), time(12,45))
    )
st.write("You're scheduled for: ", appointment)

st.subheader('Datetime slider')
start_time = st.slider(
    "When do you start?",
    value = datetime(2020,8, 13, 9, 30),
    format="DD/MMM/YYYY - hh:mm")
st.write("Start time:", start_time)

color = st.select_slider("Choose a color: ",
                         options = ['Red', 'Yellow', 'Green', 'Blue', 'Pink', 'Orange']
                         )
st.write('Your color is: ', color)


start_color, end_color = st.select_slider('Your color band is: ',
                               options = ['Red', 'Yellow', 'Green', 'Blue', 'Pink', 'Orange'],
                               value = ['Red', 'Blue']
                               )
st.write('Your chosen color band is: ', start_color, 'to', end_color)

chart_data = pd.DataFrame(data=np.random.randn(200,3), columns=['a', 'b', 'c'])
st.line_chart(chart_data)

c = (
     alt.Chart(chart_data)
     .mark_circle()
     .encode(x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
     )

st.altair_chart(c, use_container_width=True)

source = data.cars()

chart = (alt.Chart(source)
         .mark_circle()
         .encode(x='Horsepower',
                 y='Miles_per_Gallon',
                 color='Origin'
                 ).interactive()
         )
tab1, tab2 = st.tabs(['Theme Streamlit', 'Theme Altair'])

with tab1:
    st.altair_chart(chart, theme='streamlit', use_container_width=True)
    
with tab2:
    st.altair_chart(chart, theme=None, use_container_width=True)
    
source_weather = data.seattle_weather()

scale = alt.Scale(
    domain = ['sun', 'fog', 'drizzle', 'rain', 'snow'], 
    range = ["#e7ba52", "#a7a7a7", "#aec7e8", "#1f77b4", "#9467bd"]
    )

color = alt.Color('weather:N', scale=scale)    
         
brush = alt.selection_interval(encodings=['x'])
click = alt.selection_multi(encodings=['color'])

points = (
    alt.Chart()
    .mark_point()
    .encode(
        alt.X('monthdate(date):T', title='Date'),
        alt.Y('temp_max:Q', title='Maximum Daily Temperature (C)',
              scale = alt.Scale(domain=[-5, 40])),
        color=alt.condition(brush, color, alt.value('lightgray')),
        size=alt.Size('precipitation:Q', scale=alt.Scale(range=[5, 200]))
        )
    .properties(width=550, height=300)
    .add_selection(brush)
    .transform_filter(click)
    )

bars = (
        alt.Chart()
        .mark_bar()
        .encode(
            x = 'count()',
            y = 'weather:N',
            color = alt.condition(click, color, alt.value('lightgray')),
            )
        .transform_filter(brush)
        .properties(
            width=550
            )
        .add_selection(click)
        )

chart = alt.vconcat(points, bars, data=source_weather, title='Seattle Weather: 2012-2015')

tab1, tab2 = st.tabs(['Theme Streamlit', 'Theme Altair'])

with tab1:
    st.altair_chart(chart, theme='streamlit', use_container_width=True)

with tab2:
    st.altair_chart(chart, theme=None, use_container_width=True)
    

option = st.selectbox('What is your favourate color', ('Red', 'Green', 'Blue', 'Yellow'))

st.write('Your favourate color is ', option)

options = st.multiselect('What are your favourate colors', ['Red', 'Yellow', 'Blue', 'Green'], ['Red', 'Yellow'])
st.write('Your favourate colors are ', options)
    
st.subheader("What would you like to order?")

coffee = st.checkbox('COFFEE')
icecream = st.checkbox('ICECREAM')
cola = st.checkbox("COLA")

if coffee:
    st.write('He is some more :coffee:')

if icecream:
    st.write("Here is some :icecream:")
    
if cola:
    st.write("Here is some :cola:")
    
st.write('Contents of the ./streamlit/config.toml file of this app')

st.code("""
[theme]
primaryColor="#F39C12"
backgroundColor="#2E86C1"
secondaryBackgroundColor="#AED6F1"
textColor="#FFFFFF"
font="monospace"
""")

number = st.sidebar.slider('Select a number:', 0, 10, 5)
st.write('Selected number from slider widget is:', number)


#st.write(st.secrets['message'])

st.write('DB_Username is: ', st.secrets['DB_USER'])
st.write('DB_Pssword is: ', st.secrets['DB_PASSCODE'])






























