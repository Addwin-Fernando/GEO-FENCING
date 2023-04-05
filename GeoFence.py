from geopy.distance import distance


def calculateGeoFence(center_point):
    radius = 25

    num_points = 5

    geo_fence = []
    for i in range(num_points):
        bearing = i * (360 / num_points)
        point = distance(meters=radius).destination(center_point, bearing)
        geo_fence.append((point.longitude, point.latitude,))

    return geo_fence
