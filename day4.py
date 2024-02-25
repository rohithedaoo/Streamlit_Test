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