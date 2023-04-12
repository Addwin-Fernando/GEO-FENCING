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


def check(centerlat, centerlon, lat, lon):
    center = (centerlon, centerlat)
    GEO_FENCE = calculateGeoFence(center)

    inside_geo_fence = False
    j = len(GEO_FENCE) - 1
    for i in range(len(GEO_FENCE)):
        if (GEO_FENCE[i][1] < lon and GEO_FENCE[j][1] >= lon or GEO_FENCE[j][1] < lon and GEO_FENCE[i][1] >= lon) and (GEO_FENCE[i][0] + (lon - GEO_FENCE[i][1]) / (GEO_FENCE[j][1] - GEO_FENCE[i][1]) * (GEO_FENCE[j][0] - GEO_FENCE[i][0])) < lat:
            inside_geo_fence = not inside_geo_fence
        j = i

    return inside_geo_fence
