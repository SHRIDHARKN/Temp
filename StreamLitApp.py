import streamlit as st
import numpy as np
from keras.models import load_model
import joblib

#Interface
st.markdown('## Hotel Check In Prediction')


DaysSinceCreation = st.number_input('DaysSinceCreation')
AverageLeadTime = st.number_input('AverageLeadTime')
LodgingRevenue = st.number_input('LodgingRevenue')
OtherRevenue = st.number_input('OtherRevenue')
PersonsNights = st.number_input('PersonsNights')
RoomNights = st.number_input('RoomNights')
DaysSinceLastStay = st.number_input('DaysSinceLastStay')
DaysSinceFirstStay = st.number_input('DaysSinceFirstStay')

feats_selec = [DaysSinceCreation, AverageLeadTime, LodgingRevenue, OtherRevenue, PersonsNights,
               RoomNights, DaysSinceLastStay, DaysSinceFirstStay]

#Predict button
if st.button('Predict'):
    
    model = load_model(r"ANN_Model.h5")
    
    X = np.array(feats_selec)
    my_pred = model.predict([feats_selec])[0][0]
    my_pred = "Check In" if my_pred==1 else "won't Check In"
    st.markdown(f'### Customer {my_pred}')    
    