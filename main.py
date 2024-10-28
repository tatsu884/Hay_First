import streamlit as st
import time

import pandas as pd
st.title('Streamlit 超入門')

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar=st.progress(0)

for i in range(100):
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i+1)
  time.sleep(0.1)

'Done!!!!!'

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')

if button:
  right_column.write('ここは右カラム')
  
expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ1の回答')
expander1 = st.expander('問い合わせ2')
expander1.write('問い合わせ2の回答')
expander1 = st.expander('問い合わせ3')
expander1.write('問い合わせ3の回答')

# text = st.text_input('あなたの趣味を教えて下さい')
# condition = st.slider('あなたの今の調子は？',0,100,50)
