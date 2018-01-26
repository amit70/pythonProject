from . import app
from . import cursor
from flask import request


@app.route('/pythonProject/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data["email"]
    password = data["password"]
    cursor.execute("select * from users where email = '"+ email +"' and password = '"+ password +"' ")
    row = cursor.fetchone()

    if row is None:
        return "Invalid email or password"
    else:
        return "Login Successful"
