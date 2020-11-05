from CodingACME_employee_api import app,db
from CodingACME_employee_api.models import Employee, employee_schema, employees_schema, User, check_password_hash
from flask import jsonify, request, render_template, redirect, url_for

from flask_login import login_required, login_user, current_user, logout_user

import jwt

from CodingACME_employee_api.forms import UserForm, LoginForm

#Begin CRUD using methods (Create, Retrieve, Update, Delete)

@app.route('/employees/create', methods = ['POST'])
def create_employee():
    name = request.json['full_name'] 
    sex = request.json['sex']
    birth_date = request.json['birth_date']
    phone_num = request.json['phone_num']
    ssn = request.json['ssn']
    email = request.json['email']

    employee = Employee(name, sex, birth_date, phone_num, ssn, email)

    db.session.add(employee)
    db.session.commit()
    results = employee_schema.dump(employee)
    return jsonify(results)

#Tell the computer to go head and grab em' all poke ball ~ RETRIEVE ALL i.e. .all

@app.route('/employees', methods = ['GET'])
def get_employees():
    employees = Employee.query.all()
    return jsonify(employees_schema.dump(employees))

#Notice the difference in Employee and EmployeeS in our f(x) ~ RETRIEVE ONE
@app.route('/employees/<id>', methods = ['GET'])
def get_employee(id):
    employee = Employee.query.get(id)
    results = employee_schema.dump(employee)
    return jsonify(results)

#Upadate our employee roster
@app.route('/patients/update/<id>', methods = ['POST', 'PUT'])
def update_employee(id):
    employee = Employee.query.get(id)

    #Make it possible to upload all preliminary info
    employee.name = request.json['full_name']
    employee.ssn = request.json['ssn']
    employee.email = request.json['email']
    employee.sex = request.json['sex']
    employee.phone_num = request.json['phone_num']
    employee.birth_date = request.json['birth_date]'] 

    db.session.commit()

    return employee_schema.jsonify(employee)

@app.route('/employees/delete/<id>', methods = ['DELETE'])
def delete_employee(id):
    employee = Employee.query.get(id)
    db.session.delete(employee)
    db.session.commit()

    result = employee_schema.dump(employee)
    return jsonify(result)
