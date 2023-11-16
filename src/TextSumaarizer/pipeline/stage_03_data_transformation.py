from src.TextSumaarizer.config.configuration import ConfigurationManager
from src.TextSumaarizer.conponents.data_transformation import  DataTransformation
from src.TextSumaarizer.logging import logger
import os


class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.convert()