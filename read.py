import pandas as pd
import streamlit as st
#import plotly.express as px
from database import *


def read_for_gym():
    result = view_all_gym_data()
    df = pd.DataFrame(result, columns=['gym id', 'location', 'contact'])
    with st.expander("View all gyms"):
        st.dataframe(df)

def read_for_manager():
    result = view_all_manager_data()
    df = pd.DataFrame(result, columns=['manager id', 'first name', 'last name', 'phone number', 'gym id'])
    with st.expander("View all managers"):
        st.dataframe(df)

def read_for_equipment():
    result = view_all_equipment_data()
    df = pd.DataFrame(result, columns=['equipment id', 'equipment name', 'count', 'gym id'])
    with st.expander("View all equipments"):
        st.dataframe(df)

def read_for_trainer():
    result = view_all_trainer_data()
    df = pd.DataFrame(result, columns=['trainer id', 'first name', 'last name', 'phone number', 'manager id'])
    with st.expander("View all trainers"):
        st.dataframe(df)

def read_for_customer():
    result = view_all_customer_data()
    df = pd.DataFrame(result, columns=['customer id', 'first name', 'last name', 'phone number', 'age', 'height', 'weight', 'workout', 'start date', 'end date', 'trainer id', 'slot'])
    with st.expander("View all customers"):
        st.dataframe(df)

def read_for_payment():
    result = view_all_payment_data()
    df = pd.DataFrame(result, columns=['transaction id', 'amount', 'date', 'customer id', 'gym id'])
    with st.expander("View all payments"):
        st.dataframe(df)
