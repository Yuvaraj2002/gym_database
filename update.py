import datetime

import pandas as pd
import streamlit as st
from database import *


def update_for_gym():
    result = view_all_gym_data()
    # st.write(result)
    df = pd.DataFrame(result, columns=['gym id','location', 'contact'])
    with st.expander("Current gym details"):
        st.dataframe(df)
    list_of_gym = [i[0] for i in view_only_gym_id()]
    #print(list_of_gym)
    selected_gym = st.selectbox("gyms to Edit", list_of_gym)
    #print(selected_gym)
    selected_result = get_all_info_gym(selected_gym)
    #print(selected_result)
    # st.write(selected_result)
    if selected_result:
        gym_id = selected_result[0][0]
        location = selected_result[0][1]
        contact = selected_result[0][2]
        with st.container():
            new_gym_id = st.text_input("gym id:", gym_id)
            new_location = st.text_input("location:", location)
            new_contact = st.text_input("contact:", contact)
        if st.button("Update gym"):
            edit_gym_data(new_gym_id, new_location, new_contact, gym_id)
            st.success("Successfully updated")

    result2 = view_all_gym_data()
    df2 = pd.DataFrame(result2, columns=['gym id','location', 'contact'])
    with st.expander("Updated data"):
        st.dataframe(df2)

def update_for_manager():
    result = view_all_manager_data()
    # st.write(result)
    df = pd.DataFrame(result, columns=['manager id', 'first name', 'last name', 'phone number', 'gym id'])
    with st.expander("Current manager details"):
        st.dataframe(df)
    list_of_managers = [i[0] for i in view_only_manager_id()]
    #print(list_of_gym)
    selected_manager = st.selectbox("managers to Edit", list_of_managers)
    #print(selected_gym)
    selected_result = get_all_info_manager(selected_manager)
    #print(selected_result)
    # st.write(selected_result)
    if selected_result:
        manager_id = selected_result[0][0]
        fname = selected_result[0][1]
        lname = selected_result[0][2]
        ph_no = selected_result[0][3]
        gym_id = selected_result[0][4]
        with st.container():
            new_fname = st.text_input("fname:", fname)
            new_lname = st.text_input("lname:", lname)
            new_ph_no = st.text_input("phone number:", ph_no)
            new_gym_id = st.text_input("gym id:", gym_id)

        if st.button("Update manager"):
            edit_manager_data(new_fname, new_lname, new_ph_no, new_gym_id, manager_id)
            st.success("Successfully updated")

    result2 = view_all_manager_data()
    df2 = pd.DataFrame(result2, columns=['manager id', 'first name', 'last name', 'phone number', 'gym id'])
    with st.expander("Updated data"):
        st.dataframe(df2)

def update_for_trainer():
    result = view_all_trainer_data()
    # st.write(result)
    df = pd.DataFrame(result, columns=['trainer id', 'first name', 'last name', 'phone number', 'manager id'])
    with st.expander("Current trainer details"):
        st.dataframe(df)
    list_of_trainers = [i[0] for i in view_only_trainer_id()]
    #print(list_of_gym)
    selected_trainer = st.selectbox("gyms to Edit", list_of_trainers)
    #print(selected_gym)
    selected_result = get_all_info_trainer(selected_trainer)
    #print(selected_result)
    # st.write(selected_result)
    if selected_result:
        trainer_id = selected_result[0][0]
        fname = selected_result[0][1]
        lname = selected_result[0][2]
        ph_no = selected_result[0][3]
        mgr_id = selected_result[0][4]
        with st.container():
            new_fname = st.text_input("first name:", fname)
            new_lname = st.text_input("last name:", lname)
            new_ph_no = st.text_input("phone number:", ph_no)
            new_mgr_id = st.text_input("manager id:", mgr_id)
        if st.button("Update trainer"):
            edit_trainer_data(new_fname, new_lname, new_ph_no, new_mgr_id, trainer_id)
            st.success("Successfully updated")

    result2 = view_all_trainer_data()
    df2 = pd.DataFrame(result2, columns=['trainer id', 'first name', 'last name', 'phone number', 'manager id'])
    with st.expander("Updated data"):
        st.dataframe(df2)

def update_for_customer():
    result = view_all_customer_data()
    # st.write(result)
    df = pd.DataFrame(result, columns=['customer id', 'first name', 'last name', 'phone number', 'age', 'height', 'weight', 'workout', 'start date', 'end date', 'trainer id', 'slot'])
    with st.expander("Current customer details"):
        st.dataframe(df)
    list_of_customers = [i[0] for i in view_only_customer_id()]
    #print(list_of_gym)
    selected_customer = st.selectbox("customers to Edit", list_of_customers)
    #print(selected_gym)
    selected_result = get_all_info_customer(selected_customer)
    #print(selected_result)
    # st.write(selected_result)
    if selected_result:
        cust_id = selected_result[0][0]
        fname = selected_result[0][1]
        lname = selected_result[0][2]
        ph_no = selected_result[0][3]
        age = selected_result[0][4]
        height = selected_result[0][5]
        weight = selected_result[0][6]
        workout = selected_result[0][7]
        start_date = selected_result[0][8]
        end_date = selected_result[0][9]
        trainer_id = selected_result[0][10]
        slot = selected_result[0][11]
        with st.container():
            new_fname = st.text_input("first name:", fname)
            new_lname = st.text_input("last name:", lname)
            new_ph_no = st.number_input("phone number:", ph_no)
            new_age = st.number_input("age:", age)
            new_height = st.number_input("height:", height)
            new_weight = st.number_input("weight:", weight)
            new_workout = st.text_input("workout:", workout)
            new_start_date = st.date_input("start_date:", start_date)
            new_end_date = st.date_input("end_date:", end_date)
            new_trainer_id = st.text_input("trainer id:", trainer_id)
            new_slot = st.number_input("slot:", slot)
        if st.button("Update customer"):
            edit_customer_data(new_fname, new_lname, new_ph_no, new_age, new_height, new_weight, new_workout, new_start_date, new_end_date, new_trainer_id, cust_id, new_slot)
            st.success("Successfully updated")

    result2 = view_all_customer_data()
    df2 = pd.DataFrame(result2, columns=['customer id', 'first name', 'last name', 'phone number', 'age', 'height', 'weight', 'workout', 'start date', 'end date', 'trainer id', 'slot'])
    with st.expander("Updated data"):
        st.dataframe(df2)

def update_for_payment():
    result = view_all_payment_data()
    # st.write(result)
    df = pd.DataFrame(result, columns=['transaction id', 'amount', 'date', 'customer id', 'gym id'])
    with st.expander("Current payment details"):
        st.dataframe(df)
    list_of_payments = [i[0] for i in view_only_payment_id()]
    #print(list_of_gym)
    selected_payment = st.selectbox("payments to Edit", list_of_payments)
    #print(selected_gym)
    selected_result = get_all_info_payment(selected_payment)
    #print(selected_result)
    # st.write(selected_result)
    if selected_result:
        transaction_id = selected_result[0][0]
        amount = selected_result[0][1]
        date = selected_result[0][2]
        cust_id = selected_result[0][3]
        gym_id = selected_result[0][4]
        with st.container():
            new_gym_id = st.text_input("gym id:", gym_id)
            new_amount = st.number_input("amount:", amount)
            new_date = st.date_input("date:", date)
            new_cust_id = st.text_input("cust_id:", cust_id)
        if st.button("Update payment"):
            edit_payment_data(new_amount, new_date, new_cust_id, new_gym_id, transaction_id)
            st.success("Successfully updated")

    result2 = view_all_payment_data()
    df2 = pd.DataFrame(result2, columns=['transaction id', 'amount', 'date', 'customer id', 'gym id'])
    with st.expander("Updated data"):
        st.dataframe(df2)

def update_for_equipment():
    result = view_all_equipment_data()
    # st.write(result)
    df = pd.DataFrame(result, columns=['equipment id', 'equipment name', 'count', 'gym id'])
    with st.expander("Current equipmnet details"):
        st.dataframe(df)
    list_of_equipments = [i[0] for i in view_only_equipment_id()]
    #print(list_of_gym)
    selected_equipment = st.selectbox("equipments to Edit", list_of_equipments)
    #print(selected_gym)
    selected_result = get_all_info_equipment(selected_equipment)
    #print(selected_result)
    # st.write(selected_result)
    if selected_result:
        eq_id = selected_result[0][0]
        eq_name = selected_result[0][1]
        count = selected_result[0][2]
        gymid = selected_result[0][3]
        with st.container():
            new_eq_name = st.text_input("equipment name:", eq_name)
            new_count = st.number_input("count:", count)
            new_gymid = st.text_input("gym id:", gymid)
        if st.button("Update equipments"):
            edit_equipment_data(new_eq_name, new_count, new_gymid, eq_id)
            st.success("Successfully updated")

    result2 = view_all_equipment_data()
    df2 = pd.DataFrame(result2, columns=['equipment id', 'equipment name', 'count', 'gym id'])
    with st.expander("Updated data"):
        st.dataframe(df2)
