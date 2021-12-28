import pickle
import numpy as np
import pandas as pd
import math
model = pickle.load(open('crabage.pkl', 'rb'))
def predict(df):
    df = df[['Length', 'Diameter', 'Height', 'Weight', 'Shucked Weight','Viscera Weight','Shell Weight']]
    numpy_array = df.to_numpy()
    predictions = model.predict(numpy_array)
    return list(np.floor(predictions))
