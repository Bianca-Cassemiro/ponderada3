# -*- coding: utf-8 -*-
import pandas as pd
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
import pickle

# Create the app
app = FastAPI()


# Load trained Pipeline

class InputModel(BaseModel):
    CustomerID: int
    Gender: int
    Age: float
    Annual: float

class OutputModel(BaseModel):
    prediction: float

# Define predict function
@app.post("/predict", response_model=OutputModel)
def predict(data: InputModel):
    input_data = [[
        data.CustomerID,
        data.Age,
        data.Gender,
        data.Annual
    ]]

    model = pickle.load(open('random_forest.pkl', 'rb'))
   
    prediction = model.predict(input_data)
    return {"prediction": prediction[0]}


if __name__ == "__main__":
    uvicorn.run(app, port=5000)
