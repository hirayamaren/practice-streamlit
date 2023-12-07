import streamlit as st
import time

st.title('streamlit超入門')
st.write('ブログレスバーの表示')
'Start!!'

latest_iterarion=st.empty()
bar = st.progress(0)

for i in range(100):
   latest_iterarion.text(f'Iteration{i+1}')
   bar.progress(i+1)
   time.sleep(0.001)

'OK'

left_column, right_column= st.columns(2)
button =left_column.button('右にカラムを表示')
if button:
    right_column.write('ここに右カラム')

expander= st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')


