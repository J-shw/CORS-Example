from flask import Flask, render_template
import requests, os

app = Flask(__name__)
try:
    server1_url = os.environ.get("SERVER_1")
except:
    "Failed to load URL"

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/data")
def data():
    return {"data": "From server 2"}

@app.route("/request/data")
def requestData():
    try:
        response = requests.get(server1_url)
        response.raise_for_status()
        return {"data": response.text}
    except requests.exceptions.RequestException as e:
        return {"error": e}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="82")