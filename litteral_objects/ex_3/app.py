geolocations = []

# Get from user 3 geolocations and add them to list
for i in range(3):
    latitude = int(input("Please enter latitude: "))
    longitude = int(input("Please enter longitude: "))
    geolocation = {"latitude": latitude, "longitude": longitude}
    geolocations.append(geolocation)
    print()

print("---------------------------------\n")

# Run over items in list and print geolocations
for geolocation in geolocations:
    latitude = geolocation["latitude"]
    longitude = geolocation["longitude"]
    print(f"({latitude}, {longitude})")
