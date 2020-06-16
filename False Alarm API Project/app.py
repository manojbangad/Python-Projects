import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
# from sklearn.externals import joblib
import joblib
from flask import Flask, jsonify, request
import sqlite3
from sqlite3 import Error

app = Flask(__name__)

@app.route('/train')
def train():
    df = pd.read_excel('False Alarm Cases.xlsx')
    df = df.iloc[ : , 1:8 ]

    X = df.drop('Spuriosity Index(0/1)', axis = 1)
    X.drop(['Unwanted substance deposition(0/1)', 'H2S Content(ppm)'], axis = 1, inplace = True)
    Y = df['Spuriosity Index(0/1)']

    ss = StandardScaler()
    scaled_array = ss.fit_transform(X)
    X = pd.DataFrame(scaled_array, columns=X.columns)

    model = KNeighborsClassifier()
    model.fit(X, Y)

    joblib.dump(model, 'model.pkl')
    return jsonify({'message' : 'Model trained !'})

@app.route('/test', methods = ['POST'])
def test():
    data = request.get_json()
    at = data['Temperature']
    cal = data['Calibration']
    hum = data['Humidity']
    nos = data['Nos']

    narr = np.array([at, cal, hum, nos]).reshape(1, 4)
    X_test = pd.DataFrame(narr, columns=['Temperature', 'Calibration', 'Humidity', 'Number of Sensors'])

    model = joblib.load('model.pkl')
    Y_pred = model.predict(X_test)

    if Y_pred == 0:
        return jsonify({'message' : 'No Danger'})
    else:
        return jsonify({'message' : 'Dengerous'})


def AddEntryInDB():
    db_path = "E:\Python Class\Pycharm HandsOn\BankingDemoProject\Data Files\ProjectDB.db"
    try:
        conn = sqlite3.connect(db_path)
        connection = conn.cursor()

        connection.execute("CREATE TABLE APIEntries(account_id INTEGER PRIMARY KEY,first_name TEXT NOT NULL,last_name TEXT NOT NULL)")
        print("\nCustomerDetails table created successfully..")

        conn.commit()
        conn.close()

    except Error as e:
        print(e)
        print("Error faced in adding entries in database!")


app.run(port='5000')
