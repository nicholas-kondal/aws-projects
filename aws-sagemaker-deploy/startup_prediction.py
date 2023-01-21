from __future__ import print_function

import argparse
import os
import pandas as pd

from sklearn import tree
from sklearn.externals import joblib

if __name__ == '__main__':

    # SageMaker-specific arguments. Defaults are set in the environment variables.
    parser = argparse.ArgumentParser()
    parser.add_argument('--output-data-dir', type=str, default=os.environ['SM_OUTPUT_DATA_DIR']) # checkpoints and graphs
    parser.add_argument('--model-dir', type=str, default=os.environ['SM_MODEL_DIR']) # model artifacts
    parser.add_argument('--train', type=str, default=os.environ['SM_CHANNEL_TRAIN']) # training data
    args = parser.parse_args()