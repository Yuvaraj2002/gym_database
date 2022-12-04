import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="gym_database"
)

c = mydb.cursor()

def create_table():
    c.execute('create table if not exists gym(gym_id varchar(255) not null, location varchar(255), contact varchar(10), primary key (gym_id))')
    c.execute('create table if not exists equipments(eq_id int not null, eq_name varchar(255), count int, gymid varchar(255),primary key (eq_id,gymid),constraint equipments_ibfk_1 foreign key (gymid) references gym(gym_id) on delete cascade)')
    c.execute('create table if not exists managers(mgr_id varchar(255) not null, fname varchar(255), lname varchar(255), ph_no varchar(10), gym_id varchar(255),primary key(mgr_id),constraint manager_ibfk_1 foreign key (gym_id) references gym(gym_id) on delete cascade)')
    #c.execute('create table if not exists support_staff(ss_id varchar(255) not null, fname varchar(255), lname varchar(255), ph_no int, mgr_id varchar(255),primary key (ss_id),constraint support_staff_ibfk_1 foreign key (mgr_id) references manager(mgr_id))')
    c.execute('create table if not exists trainers(trainer_id varchar(255) not null, fname varchar(255), lname varchar(255), ph_no varchar(10), mgr_id varchar(255),primary key (trainer_id),constraint trainers_ibfk_1 foreign key (mgr_id) references managers(mgr_id) on delete cascade)')
    c.execute('create table if not exists customers(cust_id varchar(255) not null, fname varchar(255), lname varchar(255), ph_no varchar(10), age int(50), height int(50), weight int(50), workout varchar(255), start_date date, end_date date, trainer_id varchar(255), slot int(50), primary key (cust_id),constraint customers_ibfk_1 foreign key (trainer_id) references trainers(trainer_id) on delete cascade)')
    c.execute('create table if not exists payment_info(transaction_id int not null, amt int, tr_date date, cust_id varchar(255), gymid varchar(255), primary key (transaction_id) ,constraint payment_info_ibfk_1 foreign key (cust_id) references customers(cust_id) on delete cascade,constraint payment_info_ibfk_2 foreign key (gymid) references gym(gym_id) on delete cascade)')
    c.execute('create table if not exists backup(cust_id varchar(255) not null, fname varchar(255), lname varchar(255), ph_no varchar(255))')

def add_gym_data(gym_id, location, contact):
    c.execute('insert into gym(gym_id, location, contact) values (%s, %s, %s)',
    (gym_id, location, contact,))
    mydb.commit()

def add_trainer_data(trainer_id, fname, lname, ph_no, mgr_id):
    c.execute('insert into trainers(trainer_id, fname, lname, ph_no, mgr_id) values (%s, %s, %s, %s, %s)', (trainer_id, fname, lname, ph_no, mgr_id))
    mydb.commit()

def add_cust_data(cust_id,fname, lname, ph_no, age, height, weight, workout, start_date, end_date, trainer_id, slot):
    c.execute('INSERT INTO customers(cust_id,fname, lname, ph_no, age, height, weight, workout, start_date, end_date, trainer_id, slot) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
              (cust_id,fname, lname, ph_no, age, height, weight, workout, start_date, end_date, trainer_id, slot))
    mydb.commit() 

def add_manager_data(mgr_id, fname, lname, ph_no, gym_id):
    c.execute('INSERT INTO managers(mgr_id, fname, lname, ph_no, gym_id) VALUES (%s,%s,%s,%s,%s)',
              (mgr_id, fname, lname, ph_no, gym_id))
    mydb.commit()
def add_equipment_data(eq_id, eq_name, count, gym_id):
    c.execute('INSERT INTO equipments(eq_id, eq_name, count, gymid) VALUES (%s,%s,%s, %s)',
              (eq_id, eq_name, count, gym_id))
    mydb.commit()

def add_payment_data(transaction_id, amt, tr_date, cust_id, gym_id):
    c.execute('INSERT INTO payment_info(transaction_id, amt, tr_date, cust_id, gymid) VALUES (%s,%s,%s,%s,%s)',
              (transaction_id, amt, tr_date, cust_id, gym_id))
    mydb.commit()

def view_all_gym_data():
    c.execute('SELECT * FROM gym')
    data = c.fetchall()
    return data

def view_all_equipment_data():
    c.execute('SELECT * FROM equipments')
    data = c.fetchall()
    return data

def view_all_manager_data():
    c.execute('SELECT * FROM managers')
    data = c.fetchall()
    return data

def view_all_trainer_data():
    c.execute('SELECT * FROM trainers')
    data = c.fetchall()
    return data

def view_all_customer_data():
    c.execute('SELECT * FROM customers')
    data = c.fetchall()
    return data

def view_all_payment_data():
    c.execute('SELECT * FROM payment_info')
    data = c.fetchall()
    return data

def view_only_gym_id():
    c.execute("select gym_id from gym")
    data = c.fetchall()
    return data

def view_only_manager_id():
    c.execute("select mgr_id from managers")
    data = c.fetchall()
    return data

def view_only_trainer_id():
    c.execute("select trainer_id from trainers")
    data = c.fetchall()
    return data

def view_only_customer_id():
    c.execute("select cust_id from customers")
    data = c.fetchall()
    return data

def view_only_payment_id():
    c.execute("select transaction_id from payment_info")
    data = c.fetchall()
    return data

def view_only_equipment_id():
    c.execute("select eq_id from equipments")
    data = c.fetchall()
    return data

def get_all_info_gym(selected_gym):
    c.execute('select * from gym where gym_id="{}"'.format(selected_gym))
    data = c.fetchall()
    return data

def get_all_info_manager(selected_manager):
    c.execute('select * from managers where mgr_id="{}"'.format(selected_manager))
    data = c.fetchall()
    return data

def get_all_info_trainer(selected_trainer):
    c.execute('select * from trainers where trainer_id="{}"'.format(selected_trainer))
    data = c.fetchall()
    return data

def get_all_info_customer(selected_customer):
    c.execute('select * from customers where cust_id="{}"'.format(selected_customer))
    data = c.fetchall()
    return data

def get_all_info_payment(selected_payment):
    c.execute('select * from payment_info where transaction_id="{}"'.format(selected_payment))
    data = c.fetchall()
    return data

def get_all_info_equipment(selected_eq):
    c.execute('select * from equipments where eq_id="{}"'.format(selected_eq))
    data = c.fetchall()
    return data

def edit_gym_data(new_gym_id, new_location, new_contact, gym_id):
    c.execute("update gym set gym_id=%s, location=%s, contact=%s where gym_id=%s", (new_gym_id, new_location, new_contact, gym_id))
    mydb.commit()
    data = c.fetchall()
    return data

def edit_manager_data(new_fname, new_lname, new_ph_no, new_gym_id, manager_id):
    c.execute("update managers set fname=%s, lname=%s, ph_no=%s, gym_id=%s where mgr_id=%s", (new_fname, new_lname, new_ph_no, new_gym_id,manager_id))
    mydb.commit()
    data = c.fetchall()
    return data

def edit_trainer_data(new_fname, new_lname, new_ph_no, new_mgr_id, trainer_id):
    c.execute("update trainers set fname=%s, lname=%s, ph_no=%s, mgr_id=%s where trainer_id=%s", (new_fname, new_lname, new_ph_no, new_mgr_id, trainer_id))
    mydb.commit()
    data = c.fetchall()
    return data

def edit_customer_data(new_fname, new_lname, new_ph_no, new_age, new_height, new_weight, new_workout, new_start_date, new_end_date, new_trainer_id, cust_id, new_slot):
    c.execute("update customers set fname=%s, lname=%s, ph_no=%s, age=%s, height=%s, weight=%s, workout=%s, start_date=%s, end_date=%s, trainer_id=%s, slot=%s where cust_id=%s", (new_fname, new_lname, new_ph_no, new_age, new_height, new_weight, new_workout, new_start_date, new_end_date, new_trainer_id, cust_id, new_slot))
    mydb.commit()
    data = c.fetchall()
    return data

def edit_payment_data(new_amount, new_date, new_cust_id, new_gym_id, transaction_id):
    c.execute("update payment_info set amt=%s, tr_date=%s, cust_id=%s, gymid=%s where transaction_id=%s", (new_amount, new_date, new_cust_id, new_gym_id, transaction_id))
    mydb.commit()
    data = c.fetchall()
    return data

def edit_equipment_data(new_eq_name, new_count, new_gymid, eq_id):
    c.execute("update equipments set eq_name=%s, count=%s, gymid=%s where eq_id=%s", (new_eq_name, new_count, new_gymid, eq_id))
    mydb.commit()
    data = c.fetchall()
    return data

def delete_data_gym(selected_gym):
    c.execute('DELETE FROM gym WHERE gym_id="{}"'.format(selected_gym))
    mydb.commit()

def delete_data_managers(selected_manager):
    c.execute('DELETE FROM manager WHERE mgr_id="{}"'.format(selected_manager))
    mydb.commit()

def delete_data_trainers(selected_trainer):
    c.execute('DELETE FROM trainers WHERE trainer_id="{}"'.format(selected_trainer))
    mydb.commit()

def delete_data_customers(selected_customer):
    c.execute('DELETE FROM customers WHERE cust_id="{}"'.format(selected_customer))
    mydb.commit()

def delete_data_payment(selected_payment):
    c.execute('DELETE FROM payment_info WHERE tr_id="{}"'.format(selected_payment))
    mydb.commit()

def delete_data_equipment(selected_equipment):
    c.execute('DELETE FROM equipments WHERE eq_id="{}"'.format(selected_equipment))
    mydb.commit()