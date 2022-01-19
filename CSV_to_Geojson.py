from geojson import Feature, FeatureCollection, Point, dump
import csv
# convert csv into geojson


features = []
with open('lon&lat.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    next(reader, None)
    for Codice, Attivita, lats, lons, Level, English in reader:
        longitude, latitude = map(float, (lons, lats))
        features.append(
            Feature(
                geometry = Point((longitude, latitude)),
                properties = {
                    'Level': Level,
                    'Codice': Codice, 
                    'Acitvity': English
                }
            )
        )

feature_collection = FeatureCollection(features)
with open("Output.geojson", 'w') as f:
    dump(feature_collection, f, allow_nan= True)

