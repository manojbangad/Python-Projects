from flask import Flask, jsonify, request
from dbmodule import update_password, fetch_user, insert_data

app = Flask(__name__)

@app.route('/passwordUpdate/<string:user_id>/<string:new_pass>')
def updatePasswordForUser(user_id, new_pass):
    message = update_password(user_id, new_pass)
    if message == 'password updated':
        return jsonify({'message': 'Updated password successfully.'})
    else:
        return jsonify({'message': 'Failed to udpate the password.'})


@app.route('/login/<string:user_id>/<string:user_pwd>')
def userLogin(user_id, user_pwd):
    user_data = fetch_user(user_id, user_pwd)
    # print(user_data)
    if len(user_data) == 0 or user_data == None:
        return jsonify( { 'message': 'Invalid user credentials !' } )
    else:
        return jsonify( {'message': 'User Logged in successfully !'} )


@app.route('/register', methods = ['POST'])
def registerUser():
    reg_data = request.get_json()
    insert_data(reg_data['username'], reg_data['password'], reg_data['phone_number'])
    return jsonify({'message': 'User registered successfully. Now you can login !'})





app.run(port=5000)