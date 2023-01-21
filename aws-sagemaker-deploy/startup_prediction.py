from __future__ import print_function

import argparse
import os
import pandas as pd

from sklearn.externals import joblib
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Needs to be called model_fn() for deployment
def model_fn(model_dir):
    # Deserialize and return fitted model (should have the same name as the serialized model)
    regressor = joblib.load(os.path.join(model_dir, "model.joblib"))
    return regressor

if __name__ == '__main__':
    # SageMaker-specific arguments (defaults are set in the environment variables)
    parser = argparse.ArgumentParser()
    parser.add_argument('--output-data-dir', type=str, default=os.environ['SM_OUTPUT_DATA_DIR']) # checkpoints and graphs location
    parser.add_argument('--model-dir', type=str, default=os.environ['SM_MODEL_DIR']) # model artifacts location
    parser.add_argument('--train', type=str, default=os.environ['SM_CHANNEL_TRAIN']) # training data location
    args = parser.parse_args()
    file = os.path.join(args.train, "50_Startups.csv")
    df = pd.read_csv(file, engine="python")

    X = df.iloc[:, :-1].values
    y = df.iloc[:, 4].values
    labelencoder = LabelEncoder()
    X[:, 3] = labelencoder.fit_transform(X[:, 3])

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)

    # Print the coefficients of the trained classifier, and save the coefficients
    joblib.dump(regressor, os.path.join(args.model_dir, "model.joblib"))