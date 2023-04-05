import requests
from flask import Flask, jsonify, Request
import GeoFence

app = Flask(__name__)

# Define the geo-fence polygon as a list of (lat, lon) points
center_point = (12.919357504801521, 80.097336276434)
GEO_FENCE = GeoFence.calculateGeoFence(center_point)

# Define the route for checking if a location is inside the geo-fence and sending a message


@app.route('/')
# def index():
#     return "welcome"
def check_location():
    # Get the location coordinates from the request body
    lat = 80.09734521073366
    lon = 12.919358646979163

    # lon , lat = 12.919822070212279, 80.09640865503496

    # Check if the location is inside the geo-fence using the ray-casting algorithm
    inside_geo_fence = False
    j = len(GEO_FENCE) - 1
    for i in range(len(GEO_FENCE)):
        if (GEO_FENCE[i][1] < lon and GEO_FENCE[j][1] >= lon or GEO_FENCE[j][1] < lon and GEO_FENCE[i][1] >= lon) and (GEO_FENCE[i][0] + (lon - GEO_FENCE[i][1]) / (GEO_FENCE[j][1] - GEO_FENCE[i][1]) * (GEO_FENCE[j][0] - GEO_FENCE[i][0])) < lat:
            inside_geo_fence = not inside_geo_fence
        j = i

    # Send a message if the location is inside the geo-fence
    if inside_geo_fence:
        # Get the message content from the request body

        # message_content = "inside"

        # Set up the URL and headers for the target API
        # api_url = 'https://example.com/api/v1/messages'
        # api_headers = {
        #     'Authorization': 'Bearer my_api_key',
        #     'Content-Type': 'application/json'
        # }

        # Send the message to the target API using the requests library
        # api_response = requests.post(api_url, headers=api_headers, json={'content': message_content})

        # Check if the message was sent successfully and return the appropriate response
        # if api_response.status_code == 200:
        #     return jsonify({'message': 'Location is inside geo-fence and message sent successfully'})
        # else:
        #     return jsonify({'error': 'Failed to send message'})
        return "inside"

    # Return a response indicating whether the location is inside the geo-fence
    else:
        # return jsonify({'message': 'Location is outside geo-fence'})
        return "outside"


if __name__ == '__main__':
    app.run(debug=True)
