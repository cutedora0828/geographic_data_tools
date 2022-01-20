from netCDF4 import Dataset
from geojson import Point, Feature, FeatureCollection, dump
import numpy as np



input_path = '.nc'
output_path1 = '.geojson'
data = Dataset(input_path)
#print(data)

lats = data.variables['longitude'][:] 
lons = data.variables['latitude'][:] 
value = data.variables[''][:] 

(d_height,d_witdth) = np.shape(value)


def transformation(data):

    """
    Input(.nc): input need to be .nc data format
    output(.geojson): output will auto save into your working space 
    """

    features = []
    i = 0
    while i < d_height:
        j = 0
        while j < d_witdth:
            point = Point((float(lats[j]), float(lons[i])))
            if value.data[i, j].astype(np.int64) > 0:
                features.append(Feature(geometry=point, 
                    properties={"": float(np.round(value[i,j],4))}))
            j += 1
        i += 1
    feature_collection = FeatureCollection(features)
    with open(output_path1, 'w') as f:
        dump(feature_collection, f, allow_nan= True)

