import streamlit as st
import pickle
import numpy as np

    
def predict_two_Variable(cost_in_TV_adv,cost_in_newspaper_adv,adv_option):

    input_array = np.array([[cost_in_TV_adv,cost_in_newspaper_adv]])

    if adv_option == "Radio and TV":
        with open("Multi_Linear_Regression_TV_Radio.pickle", "rb") as file:
            model = pickle.load(file)

    elif adv_option == "Radio and Newspaper":
        with open("Multi_Linear_Regression_Radio_Newspaper.pickle", "rb") as file:
            model = pickle.load(file)

    elif adv_option == "Newspaper and TV":
        with open("Multi_Linear_Regression_TV_Newspaper.pickle", "rb") as file:
            model = pickle.load(file)

    prediction = model.predict(input_array)
    return prediction


def predict_single_Variable(cost_in_TV_adv,adv_option):

    input_array = np.array([[cost_in_TV_adv]])

    if adv_option == "Radio":
        with open("Linear_Regression_Radio.pickle", "rb") as file:
            model = pickle.load(file)

    elif adv_option == "TV":
        with open("Linear_Regression_TV.pickle", "rb") as file:
            model = pickle.load(file)

    elif adv_option == "Newspaper":
        with open("Linear_Regression_News.pickle", "rb") as file:
            model = pickle.load(file)

    prediction = model.predict(input_array)
    return prediction

def open_slicer(selected_option):

    cost_in_radio_adv = 0
    cost_in_TV_adv = 0
    cost_in_newspaper_adv = 0

    if selected_option == "Radio" or selected_option == "Radio and TV" or selected_option == "Radio and Newspaper":
        cost_in_radio_adv = st.slider("Investment in Radio advertisement", min_value = 0.0, max_value = 100.0, value = 20.0,step=0.01)
    
    if selected_option == "TV" or selected_option == "Radio and TV" or selected_option == "Newspaper and TV":
        cost_in_TV_adv = st.slider("Investment in TV advertisement", min_value = 0.0, max_value = 100.0, value = 20.0,step=0.01)
    
    if selected_option == "Newspaper" or selected_option == "Radio and Newspaper" or selected_option== "Newspaper and TV":
        cost_in_newspaper_adv = st.slider("Investment in newspaper advertisement", min_value = 0.0, max_value = 100.0, value = 20.0,step=0.01)
    

    return [cost_in_radio_adv, cost_in_TV_adv, cost_in_newspaper_adv]


st.title("Multi Linear Regression Prediction")

adv_option = st.selectbox("Select the mode of Investment made for advertisement", ["Radio","TV","Newspaper","Radio and TV","Radio and Newspaper", "Newspaper and TV"])

cost_of_ad = open_slicer(adv_option )

cost_in_radio_adv = cost_of_ad[0]
cost_in_TV_adv = cost_of_ad[1]
cost_in_newspaper_adv = cost_of_ad[2]

if st.button ("Predict"):
    if adv_option == "Radio":
        prediction = predict_single_Variable(cost_in_radio_adv,adv_option)
        st.write(f"The Estimated sales from {adv_option} will be {prediction}")
    elif adv_option == "TV":
        prediction = predict_single_Variable(cost_in_TV_adv,adv_option)
        st.write(f"The Estimated sales from {adv_option} will be {prediction}")
    elif adv_option == "Newspaper":
        prediction = predict_single_Variable(cost_in_newspaper_adv,adv_option)
        st.write(f"The Estimated sales from {adv_option} will be {prediction}")
    elif adv_option == "Radio and TV":
        prediction = predict_two_Variable(cost_in_TV_adv,cost_in_radio_adv,adv_option)
        st.write(f"The Estimated sales from {adv_option} will be {prediction}")
    elif adv_option == "Radio and Newspaper":
        prediction = predict_two_Variable(cost_in_radio_adv,cost_in_newspaper_adv,adv_option)
        st.write(f"The Estimated sales from {adv_option} will be {prediction}")
    elif adv_option == "Newspaper and TV":
        prediction = predict_two_Variable(cost_in_TV_adv,cost_in_newspaper_adv,adv_option)
        st.write(f"The Estimated sales from {adv_option} will be {prediction}")
