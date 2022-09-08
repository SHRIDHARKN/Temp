import streamlit as st
import numpy as np
from keras.models import load_model
import joblib

#Interface
st.markdown('## Hotel Check In Prediction')

DaysSinceCreation = st.number_input('DaysSinceCreation')
LodgingRevenue = st.number_input('LodgingRevenue')
OtherRevenue = st.number_input('OtherRevenue')
PersonsNights = st.number_input('PersonsNights')
RoomNights = st.number_input('RoomNights')
DaysSinceLastStay = st.number_input('DaysSinceLastStay')
DaysSinceFirstStay = st.number_input('DaysSinceFirstStay')
AverageLeadTime = st.number_input('AverageLeadTime')
AverageLeadTime_NotLikely = 0 if AverageLeadTime>0 else 1

feats_selec = [DaysSinceCreation,LodgingRevenue, OtherRevenue, PersonsNights,
               RoomNights, DaysSinceLastStay, DaysSinceFirstStay,AverageLeadTime_NotLikely]

scaling_factor = joblib.load("scaling_factor")
feats_scaled = scaling_factor.transform(np.array([feats_selec]))

#Predict button
if st.button('Predict'):
    
    model = load_model(r"ANN_Model.h5")
    
    my_pred = model.predict(feats_scaled)[0][0]
    my_pred = "Will Check In" if my_pred==1 else "Won't Check In"
    st.markdown(f'### Customer {my_pred}')    
    
