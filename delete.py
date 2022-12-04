import pandas as pd
import streamlit as st
from database import *

def delete_for_gym():
    result = view_all_gym_data()
    df = pd.DataFrame(result, columns=['gym id', 'location', 'contact'])
    with st.expander("View all gyms"):
        st.dataframe(df)

    list_of_gym = [i[0] for i in view_only_gym_id()]
    selected_gym = st.selectbox("gyms to delete", list_of_gym)
    st.warning("Do you want to delete ::{}".format(selected_gym))
    if st.button("Delete gym"):
        delete_data_gym(selected_gym)
        st.success("gym has been deleted successfully")
    result2 = view_all_gym_data()
    df2 = pd.DataFrame(result2, columns=['gym id','location', 'contact'])
    with st.expander("Updated data"):
        st.dataframe(df2)

def delete_for_equipments():
    result = view_all_equipment_data()
    df = pd.DataFrame(result, columns=['equipment id', 'equipment name', 'count', 'gym id'])
    with st.expander("View all equipments"):
        st.dataframe(df)

    list_of_equipments = [i[0] for i in view_only_equipment_id()]
    selected_equipment = st.selectbox("equipments to delete", list_of_equipments)
    st.warning("Do you want to delete ::{}".format(selected_equipment))
    if st.button("Delete equipment"):
        delete_data_equipment(selected_equipment)
        st.success("equipment has been deleted successfully")

    result2 = view_all_equipment_data()
    df2 = pd.DataFrame(result2, columns=['equipment id', 'equipment name', 'count', 'gym id'])
    with st.expander("Updated data"):
        st.dataframe(df2)

def delete_for_managers():
    result = view_all_manager_data()
    df = pd.DataFrame(result, columns=['manager id', 'first name', 'last name', 'phone number', 'gym id'])
    with st.expander("View all managers"):
        st.dataframe(df)

    list_of_managers = [i[0] for i in view_only_manager_id()]
    selected_manager = st.selectbox("managers to delete", list_of_managers)
    st.warning("Do you want to delete ::{}".format(selected_manager))
    if st.button("Delete manager"):
        delete_data_managers(selected_manager)
        st.success("manager has been deleted successfully")
    result2 = view_all_manager_data()
    df2 = pd.DataFrame(result2, columns=['manager id', 'first name', 'last name', 'phone number', 'gym id'])
    with st.expander("Updated data"):
        st.dataframe(df2)

def delete_for_trainers():
    result = view_all_trainer_data()
    df = pd.DataFrame(result, columns=['trainer id', 'first name', 'last name', 'phone number', 'manager id'])
    with st.expander("View all trainers"):
        st.dataframe(df)

    list_of_trainers = [i[0] for i in view_only_trainer_id()]
    
    selected_trainer = st.selectbox("trainers to delete", list_of_trainers)
    st.warning("Do you want to delete ::{}".format(selected_trainer))
    if st.button("Delete trainer"):
        delete_data_trainers(selected_trainer)
        st.success("trainer has been deleted successfully")
    result2 = view_all_trainer_data()
    df2 = pd.DataFrame(result2, columns=['trainer id', 'first name', 'last name', 'phone number', 'manager id'])
    with st.expander("Updated data"):
        st.dataframe(df2)

def delete_for_customers():
    result = view_all_customer_data()
    df = pd.DataFrame(result, columns=['customer id', 'first name', 'last name', 'phone number', 'age', 'height', 'weight', 'workout', 'start date', 'end date', 'trainer id', 'slot'])
    with st.expander("View all customers"):
        st.dataframe(df)

    list_of_customers = [i[0] for i in view_only_customer_id()]
    selected_customer = st.selectbox("customers to delete", list_of_customers)
    st.warning("Do you want to delete ::{}".format(selected_customer))
    if st.button("Delete customer"):
        delete_data_customers(selected_customer)
        st.success("customer has been deleted successfully")
    result2 = view_all_customer_data()
    df2 = pd.DataFrame(result2, columns=['customer id', 'first name', 'last name', 'phone number', 'age', 'height', 'weight', 'workout', 'start date', 'end date', 'trainer id', 'slot'])
    with st.expander("Updated data"):
        st.dataframe(df2)

def delete_for_payment_info():
    result = view_all_payment_data()
    df = pd.DataFrame(result, columns=['transaction id', 'amount', 'date', 'customer id', 'gym id'])
    with st.expander("View all payments"):
        st.dataframe(df)

    list_of_payments = [i[0] for i in view_only_payment_id()]
    selected_payment = st.selectbox("payments to delete", list_of_payments)
    st.warning("Do you want to delete ::{}".format(selected_payment))
    if st.button("Delete payment"):
        delete_data_payment(selected_payment)
        st.success("transaction has been deleted successfully")
    result2 = view_all_payment_data()
    df2 = pd.DataFrame(result2, columns=['transaction id', 'amount', 'date', 'customer id', 'gym id'])
    with st.expander("Updated data"):
        st.dataframe(df2)