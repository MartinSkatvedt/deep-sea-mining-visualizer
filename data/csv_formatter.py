
def create_json_object(coordinate):
    print("{")
    print('"type": "Feature",')
    print('"properties": {},')
    print('"geometry": {')
    print('"type": "Point",')
    print('"coordinates": [')
    print(coordinate)
    print("]")
    print("}")
    print("},")

with open("EiT-3.csv", "r") as f:
    for line in f.readlines():
        coords = line.strip().split(" ")
        if len(coords) != 2:
            continue
        lon = coords[0].strip()[:-1]
        #print(lon)

        lat = coords[1].strip()[2:]
        if lat[-1] == "W":
            lat = "-" + lat[:-1]
        else:
            lat = lat[:-1]
        
        create_json_object(lat+ ", " + lon)