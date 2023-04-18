from flask import Flask, request, jsonify, session, send_file
from flask_cors import CORS

import os
import json, shutil
from datetime import datetime

app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.route("/upload",methods=["POST"])
def upload():
    file = request.files['data']
    fileext = (file.filename).split(".")[-1]
    file_bytes = file.read()

    try:
        path = "data/"
        if fileext == "pcap":
            f = open(path+'test.pcap',"wb")
            f.write(file_bytes)
            f.close()
    except Exception as e:
        return jsonify({"error":"Failed"}), 500

    return jsonify({"status":"Success"}), 200
    


@app.route("/analyse",methods=["POST"])
def analyse():
    return "200"

@app.route("/getresults",methods=["GET"])
def results():
    return "200"

@app.route("/getassets",methods=["GET"])
def assets():
    return "200"

@app.route("/gettable",methods=["GET"])
def table():
    return "200"

if __name__ == "__main__":
    # app.secret_key = 'super secret key'
    app.run(debug=True,threaded=True)