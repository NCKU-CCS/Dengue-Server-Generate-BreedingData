import random
import time
from geopy.distance import vincenty

random.seed(time.time())
lat, lng = 22.993996, 120.223463

for i in range(50):
    new_lat = lat + random.randint(-50, 50) * 0.00001
    new_lng = lng + random.randint(-50, 50) * 0.00001
    distance = vincenty((lat, lng), (new_lat, new_lng)).meters
    print("New lat, lng: {}, {}. Distance: {}".format(new_lat, new_lng, distance))

