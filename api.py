from flask import Flask, request, redirect
import GeoFence

app = Flask(__name__)


@app.route('/')
def index():

    return "Working"


@app.route("/inside", methods=["POST"])
def inside():
    return "inside"


@app.route("/outside", methods=["POST"])
def outside():
    return "outside"


@app.route('/data', methods=['POST'])
def receive_data():
    # Get the JSON data from the request body
    data = request.json

    # Display the received data
    # print("Lat:", data['lat'])
    res = GeoFence.check(data["center-lat"], data["center-lon"],
                         data["lat"], data["lon"])

    if res == True:
        return "<h1>inside</h1>"
    elif res == False:
        return "<h1>outside</h1>"
    else:
        return "Default"

    # if res:
    #     print("inside")
    # else:
    #     print("outside")

    # Return a JSON response


if __name__ == '__main__':
    app.run(debug=True)
