import sys

from helmet.exception import HelmetException
from helmet.logger import logging
from helmet.pipeline.train_pipeline import TrainPipeline

train_pipeline = TrainPipeline()
train_pipeline.run_pipeline()
print("Success")
