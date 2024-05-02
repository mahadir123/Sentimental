import streamlit as st
import joblib
#load the trained model

model= joblib.load("news-classification-model.pkl")

#define sentiment lab
news_labels = {'0': 'Technical' ,'1': 'Business','2': 'sports','3': 'Entertainment','4': 'Politics'}

#create streamlit app
st.title('News Classification')

#input text area
user_input = st.text_area("Enter news here : ")

#prediction button

if st.button("predict"):
   # print(user_input)
    predicted_label = model.predict([user_input])[0]
   # print("predicted label:" + str(predicted_label))
    predicted_news_label = news_labels[str(predicted_label)]

    st.info(f'predicted sentiment : {predicted_news_label} ')
