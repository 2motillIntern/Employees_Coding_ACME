from CodingACME_employee_api import app, db, ma, login_manager

from datetime import datetime

import uuid

from flask_login import UserMixin

from werkzeug.security import generate_password_hash, check_password_hash

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    full_name = db.Column(db.String, nullable = False)
    sex = db.Column(db.String, nullable = False)
    phone_num = db.Column(db.String, nullable = False)
    email = db.Column(db.String, nullable = False)
    birth_date = db.Column(db.String, nullable = False)

    def __init__(self,full_name,sex,phone_num,email,birth_date, id=id):
        self.full_name = full_name
        self.sex = sex
        self.phone_num = phone_num
        self.email = email
        self.birth_date = birth_date
    
    def __repr__(self):
        return f'Employee {self.full_name} has been added to employee roster'


class EmployeeSchema(ma.Schema):
    class Meta:
        #Create fields that will show after data is digested
        fields = ['id', 'full_name', 'sex', 'phone_num', 'email', 'birth_date']
#Differentiate One from Many
employee_schema = EmployeeSchema()
employees_schema = EmployeeSchema(many = True)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model,UserMixin):
    id = db.Column(db.String(70), primary_key = True)
    name = db.Column(db.String(120), nullable = False)
    email = db.Column(db.String(100))
    password = db.Column(db.String(50), nullable = False)
    token = db.Column(db.String(400))
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    token_refreshed = db.Column(db.Boolean, default = False)
    date_refreshed = db.Column(db.DateTime)

    def __init__(self,name,email,password, id = id):
        self.id = str(uuid.uuid4())
        self.name = name
        self.email = email
        self.password = self.set_password(password)

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash

    def __repr__(self):
        return f'{self.name} is now live! Date: {self.date_created}'