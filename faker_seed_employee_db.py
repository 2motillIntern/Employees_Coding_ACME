from faker import Faker

def getProfile():
    fake = Faker
    return fake.profile()

import os
from CodingACME_employee_api.models import Employee
from CodingACME_employee_api import db

def seedData():
    for seed_num in range(20):
        data = getProfile()
        employee = Employee(data['name'],\
        data['sex'], data['birth_date'], data['ssn'], data['phone_num'], data['email'] )
        
        db.session.add(employee)
        db.session.commit()

seedData()