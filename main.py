# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 21:36:09 2023

@author: Chandrika
"""

import streamlit as st

#st.sidebar.header("Predicting the PMSM speed")
st.set_page_config(page_title='PMSM_speed Prediction')

st.header("PERMANENT MAGNET SYNCHRONOUS MOTORS")
st.image("pmsm1.jpg")
st.write("Permanent magnet synchronous motors (PMSM) are typically used for high-performance and high-efficiency motor drives. High-performance motor control is characterized by smooth rotation over the entire speed range of the motor, full torque control at zero speed, and fast acceleration and deceleration")
st.subheader("The attributes of the Permanent magnet synchronous motors are:")
st.write("Ambient = Ambient temperature as measured by a thermal sensor located closely to the stator.")
st.write("Coolant = Coolant temperature. The motor is water cooled. Measurement is taken at the outflow.")
st.write("u_q = Voltage q-componen")
st.write("Motor speed (Independent variable)")
st.write("Torque = Torque induced by current.")
st.write("i_d = Current d-component")
st.write("i_q =  Current q component")
st.write("pm = Permanent Magnet surface temperature representing the rotor temperature.This was measured with an infrared thermography unit.")
st.write("Stator_yoke = Stator yoke temperature is measured with a thermal sensor.")
st.write("Stator_tooth = Stator tooth temperature is measured with a thermal sensor.")
st.write("Stator_tooth = Stator tooth temperature is measured with a thermal sensor.")
st.write("Profile_id = Each measurement session has a unique ID.Make sure not to try to estimate from one session onto the other as they are strongly independent.")