import streamlit as st
import joblib
import pandas as pd

model=joblib.load("spam_clf.pkl")
st.set_page_config(layout="wide")

#st.sidebar.image("img.jpg",width=150)

st.sidebar.title("About us")
st.sidebar.text("Spam classification uses machine learning and NLP to automatically detect whether a message is Spam or Not Spam. This project supports both single and bulk message prediction, helping filter unwanted messages efficiently and accurately")
st.sidebar.title("Contact us")
st.sidebar.text("999999999")
st.sidebar.title("Email Id")
st.sidebar.text("tazeenara28@gmail.com")

st.markdown("""
<style>
.banner {
    background: linear-gradient(90deg, #ff9966, #ff5e62);
    padding: 25px;
    border-left: 8px solid #4CAF50;
    font-size: 36px;
    font-weight: 600;
    color: white;
    border-radius: 10px;
}
</style>

<div class="banner"> Spam Classifier Project</div>
""", unsafe_allow_html=True)





col1,col2=st.columns([1.5,2],gap="large")
with col1:
    st.markdown("""
<style>
.section-header {
    background: linear-gradient(90deg, #36d1dc, #5b86e5);
    padding: 15px 25px;
    border-radius: 10px;
    color: white;
    font-size: 28px;
    font-weight: 600;
    margin-top: 20px;
    margin-bottom: 15px;
}
</style>

<div class="section-header">📩 Single Message Prediction</div>
""", unsafe_allow_html=True)
   

    text=st.text_input("Enter MSG")
    if st.button("Predict"):
        result=model.predict([text])
        if result=="spam":
            st.error("Spam->Irrelevent")
        else:
            st.success("Ham->Relevent")

with col2:
    st.markdown("""
<style>
.section-header {
    background: linear-gradient(90deg, #36d1dc, #5b86e5);
    padding: 15px 25px;
    border-radius: 10px;
    color: white;
    font-size: 28px;
    font-weight: 600;
    margin-top: 25px;
    margin-bottom: 15px;
}
</style>

<div class="section-header">📂 Bulk Message Prediction</div>
""", unsafe_allow_html=True)


    file=st.file_uploader("select file containing bulk msgs",type=['txt','csv'])

    if file!=None:
        df=pd.read_csv(file.name,header=None,names=["Msg"])
        place=st.empty()
        place.dataframe(df)
        if st.button("Predict",key="b2"):
            df['result']=model.predict(df.Msg)
            place.dataframe(df)