import streamlit as st
import joblib
st.markdown("<h1 style='text-align:center'>Bill Prediction</h1>",unsafe_allow_html=True)
st.markdown("<h3  style='text-align:center'>Shows the total bill paid</h3>",unsafe_allow_html=True)
tip=st.number_input("Enter the tip paid",min_value=0)
sex=st.radio("Select your gender",["Male","Female"],horizontal=True)
smoker=st.selectbox("Smoker?",["Yes","No"])
time=st.selectbox("Enter the time",["Day","Night"])
size=st.number_input("Enter size of your family",min_value=0)
if sex=="Male":
    sex=1
else:
    sex=0
if smoker=="Yes":
    smoker=1
else:
    smoker=0
if time=="Day":
    time=0
else:
    time=1



if st.button("Predict"):
    model=joblib.load("tips_model.h5")
    prediction=model.predict([[tip,sex,smoker,time,size]])
    st.success(prediction[0])
