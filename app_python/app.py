"""
Main app file
"""
import requests
from datetime import datetime
from flask import Flask

app = Flask(__name__)


@app.route('/visits')
#main time function
def visits():
    """
    Gets vists and returns them
    """
    f = open("visits.txt", "r")
    contents = f.read()
    return contents


@app.route('/')
#main time function
def time():
    """
    Gets time data and returns it
    """
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    f = open("visits.txt", "a")
    f.write("visit at ", current_time)
    f.close()
    response = requests.get(
        'https://www.timeapi.io/api/Time/current/coordinate?latitude=55.45&longitude=37.36')
    if response.status_code == 200:
        payload = response.json()
        answer = "Moscow time:" + \
            str(payload["hour"])+":"+str(payload["minute"]) + \
            ":"+str(payload["seconds"])
    else:
        answer = response.status_code
    return answer


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
