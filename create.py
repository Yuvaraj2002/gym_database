import streamlit as st
from database import *

def create_for_customer():
    
    with st.container():
        cust_id = st.text_input("cust_id")
        fname = st.text_input("fname:")
        lname = st.text_input("lname:")
        ph_no = st.number_input("phone number:")
        age = st.number_input("age:")
        height = st.number_input("height:")
        weight = st.number_input("weight:")
        workout = st.selectbox("workout program:",["weight loss","weight gain", "flexibility","fitness", "body building"])
        start_date = st.date_input("start date:")
        end_date = st.date_input("end date:")
        trainer_id = st.text_input("trainer id:")
        slot = st.number_input("slot")
    
    if st.button("Add customer Details"):
        add_cust_data(cust_id,fname, lname, ph_no, age, height, weight, workout, start_date, end_date, trainer_id, slot)
        st.success("Successfully added customer details: {}".format(fname))

def create_for_gym():
    
    with st.container():
        gym_id = st.text_input("gym id:")
        location = st.text_input("location:")
        contact = st.number_input("phone number:")
    if st.button("Add gym Details"):
        add_gym_data(gym_id, location, contact)
        st.success("Successfully added gym details: {}".format(gym_id))

def create_for_trainers():
    with st.container():
        trainer_id = st.text_input("trainer id:")
        fname = st.text_input("fname:")
        lname = st.text_input("lname:")
        ph_no = st.number_input("phone number:")
        mgr_id = st.text_input("manager id:")

    if st.button("Add trainer Details"):
        add_trainer_data(trainer_id, fname, lname, ph_no, mgr_id)
        st.success("Successfully added trainer details: {}".format(fname))

def create_for_equipments():
    
    with st.container():
        equipment_id = st.number_input("equipment_id:")
        equipment_name = st.text_input("equipment name:")
        count = st.number_input("count:")
        gym_id = st.text_input("gym id:")
    if st.button("Add gym Details"):
        add_equipment_data(equipment_id, equipment_name, count, gym_id)
        st.success("Successfully added equipment details: {}".format(equipment_name))

def create_for_managers():
    
    with st.container():
        mgr_id = st.text_input("manager id:")
        fname = st.text_input("first name:")
        lname = st.text_input("last name:")
        ph_no = st.number_input("phone number:")
        gym_id = st.text_input("gym id")
    if st.button("Add manager Details"):
        add_manager_data(mgr_id, fname, lname, ph_no, gym_id)
        st.success("Successfully added manager details: {}".format(fname))

def create_for_payment():
    
    with st.container():
        tr_id = st.text_input("transaction id:")
        amt = st.text_input("amount:")
        tr_date = st.date_input("transaction date:")
        cust_id = st.text_input("customer id")
        gym_id = st.text_input("gym id")
    if st.button("Add payment Details"):
        add_payment_data(tr_id, amt, tr_date, cust_id, gym_id)
        st.success("Successfully added payment details: {}".format(cust_id))

