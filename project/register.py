from . import app
from . import cursor
from flask import request
from . import conn

@app.route('/pythonProject/register', methods=['POST'])
def register():
    data = request.get_json()
    cursor.execute("select * from users where email = '"+ data["email"] +"'")
    row = cursor.fetchone()

    if row is not None:
        return "User already registered"

    cursor.execute("INSERT INTO `users` (`userId`, `firstname`, `lastname`, `email`, `password`) "
                   "VALUES (NULL, '" + data["firstname"] +"', '" +data["lastname"]+ "', '" +data["email"]+ "', '"+data["password"]+"')")
    conn.commit()
    return "User successfully registered"