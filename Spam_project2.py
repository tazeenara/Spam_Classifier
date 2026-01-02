import streamlit as st
import joblib
import pandas as pd

model=joblib.load("spam_clf.pkl")

st.set_page_config(layout="wide")


st.sidebar.title("About us")
st.sidebar.text("Spam classification uses machine learning and NLP to automatically detect whether a message is Spam or Not Spam. This project supports both single and bulk message prediction, helping filter unwanted messages efficiently and accurately")
st.sidebar.title("Contact us")
st.sidebar.text("999999999")
st.sidebar.title("Email Id")
st.sidebar.text("tazeenara28@gmail.com")


st.markdown("""
    <div style="
        background-color:brown;
        padding:20px;
        border-radius:12px;
        text-align:center;
        color:white;
        font-size:44px;
        font-weight:900;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.3);
    ">
        🚫Spam Classifier Project
    </div>
""", unsafe_allow_html=True)


st.text("")
col1,col2=st.columns([1.5,2],gap="large")
with col1:
    st.markdown("""
<h2 style="
    background: #1E88E5;
    padding:10px;
    border-radius:6px;
    color:white;
    font-weight:400;
    text-align:center;">
    Single Msg Prediction
</h2>
""", unsafe_allow_html=True)

    st.text("")
    text=st.text_input("Enter MSG")
    if st.button("Predict"):
        result=model.predict([text])
        if result=="spam":
            st.error("Spam->Irrelevent ❌")
        else:
            st.success("Ham->Relevent ✔")

with col2:
    st.markdown("""
<h2 style="
    background: #1E88E5;
    padding:10px;
    border-radius:6px;
    color:white;
    font-weight:400;
    text-align:center;">
    Bulk Msg Prediction
</h2>
""", unsafe_allow_html=True)
    st.text("")
    file=st.file_uploader("select file containg bulk msgs",type=['txt','csv'])
    
    if file!=None:
        df=pd.read_csv(file.name,header=None,names=["Msg"])
        place=st.empty()
        place.dataframe(df)
        if st.button("Predict",key="b2"):
            df['result']=model.predict(df.Msg)
            place.dataframe(df)
           
