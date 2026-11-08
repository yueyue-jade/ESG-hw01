#--------------------------------------------------------------------------------------
#Requests.get
#------------------------------------------------------------------------------------
import streamlit as st  # [新增] Streamlit 框架
import pandas as pd
import requests

st.title("證交所開放資料")  # [新增] 網頁標題

url = "https://mopsfin.twse.com.tw/opendata/t187ap46_O_1.csv" #換連結
response = requests.get(url,verify=False)
with open("data01.csv","wb")as file:
  file.write(response.content)
df = pd.read_csv("data01.csv",encoding="utf-8-sig") #繁體中文
df=df.dropna()
st.dataframe(df)  # [修改] 原本是 df（只適用 Jupyter），Streamlit 要用 st.dataframe 顯示
