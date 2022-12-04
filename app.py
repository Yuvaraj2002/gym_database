# import mysql.connector
# mydb = mysql.connector.connect(
# host="localhost",
# user="root",
# password=""
# )
# c = mydb.cursor()
# c.execute("CREATE DATABASE gym_database")

# Importing pakages
import streamlit as st
import mysql.connector
import pandas as pd

from create import *
from database import *
from delete import *
from read import *
from update import *



def main():
    st.title("PESU GYM")
    menu = ["customers", "trainers", "equipments", "payment info", "gym", "managers", "query", "membership expired"]
    choice = st.sidebar.selectbox("Menu", menu)

    create_table()
    
    if choice == "customers":
        menu = ["add","remove", "update", "read"]
        choice2 = st.sidebar.selectbox("Menu", menu)
        if choice2 == "add":
            st.subheader("Enter customer Details:")
            create_for_customer()
        elif choice2 == "read":
            st.subheader("view the customer details:")
            read_for_customer()
        elif choice2 == "update":
            st.subheader("Update created tasks")
            update_for_customer()
        elif choice2 == "remove":
            st.subheader("Delete created tasks")
            delete_for_customers()
    elif choice == "gym":
        menu = ["add","remove", "update", "read"]
        choice2 = st.sidebar.selectbox("Menu", menu)
        if choice2 == "add":
            st.subheader("Enter gym Details:")
            create_for_gym()
        elif choice2 == "read":
            st.subheader("view the gym details:")
            read_for_gym()
        elif choice2 == "update":
            st.subheader("Update created tasks")
            update_for_gym()
        elif choice2 == "remove":
            st.subheader("Delete created tasks")
            delete_for_gym()

    elif choice == "managers":
        menu = ["add","remove", "update", "read"]
        choice2 = st.sidebar.selectbox("Menu", menu)
        if choice2 == "add":
            st.subheader("Enter manager Details:")
            create_for_managers()
        elif choice2 == "read":
            st.subheader("view the manager details:")
            read_for_manager()
        elif choice2 == "update":
            st.subheader("Update created tasks")
            update_for_manager()
        elif choice2 == "remove":
            st.subheader("Delete created tasks")
            delete_for_managers()

    elif choice == "trainers":
        menu = ["add","remove", "update", "read"]
        choice2 = st.sidebar.selectbox("Menu", menu)
        if choice2 == "add":
            st.subheader("Enter trainer Details:")
            create_for_trainers()
        elif choice2 == "read":
            st.subheader("view the trainer details:")
            read_for_trainer()
        elif choice2 == "update":
            st.subheader("Update created tasks")
            update_for_trainer()
        elif choice2 == "remove":
            st.subheader("Delete created tasks")
            delete_for_trainers()

    elif choice == "equipments":
        menu = ["add","remove", "update", "read"]
        choice2 = st.sidebar.selectbox("Menu", menu)
        if choice2 == "add":
            st.subheader("Enter equipments Details:")
            create_for_equipments()
        elif choice2 == "read":
            st.subheader("view the equipment details:")
            read_for_equipment()
        elif choice2 == "update":
            st.subheader("Update created tasks")
            update_for_equipment()
        elif choice2 == "remove":
            st.subheader("Delete created tasks")
            delete_for_equipments()

    elif choice == "payment info":
        menu = ["add","remove", "update", "read"]
        choice2 = st.sidebar.selectbox("Menu", menu)
        if choice2 == "add":
            st.subheader("Enter payment Details:")
            create_for_payment()
        elif choice2 == "read":
            st.subheader("view the payment details:")
            read_for_payment()
        elif choice2 == "update":
            st.subheader("Update created tasks")
            update_for_payment()
        elif choice2 == "remove":
            st.subheader("Delete created tasks")
            delete_for_payment_info()

    elif choice=="query":
        query = st.text_input("enter a query:")
        c.execute(query)
        columns_name = []
        #print(c.description)
        
        for i in c.description:
            columns_name.append(i[0])
            
        #print(columns_name)
        data = c.fetchall()
        df = pd.DataFrame(data, columns = columns_name)
        #print(data.columns)
        st.dataframe(df)
    elif choice=="membership expired":
        c.execute("select fname, subscription_expired(end_date) from customers")
        data = c.fetchall()
        columns_name = []
        for i in c.description:
            columns_name.append(i[0])
        df = pd.DataFrame(data, columns=columns_name)
        st.dataframe(df)
    else:
        st.subheader("About tasks")

if __name__ == '__main__':
    main()



    
