import pandas as pd
import numpy as np
import os
import sys
from DimondPricePrediction.logger import logging
from DimondPricePrediction.exception import CustomException
from dataclasses import dataclass
from DimondPricePrediction.utils.utils import save_object
from DimondPricePrediction.utils.utils import evaluate_model

from sklearn.linear_model import LinearRegression,Ridge,Lasso,ElasticNet

@dataclass 
class ModelTrainerConfig:
    trained_model_file_path=os.path.join('artifacts','model.pkl')



class ModelTrainer:
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()

    def initiate_model_training(self,train_array,test_array):
        try:
            logging.info("splitting dependent and independent variables from train and test data")
            x_train,y_train,x_test,y_test=(
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )

            models={
                'LinearRegression':LinearRegression(),
                'Lasso':Lasso(),
                'Ridge':Ridge(),
                'Elasticnet':ElasticNet()
            }

            model_report:dict=evaluate_model(x_train,y_train,x_test,y_test,models)
            print(model_report)
            print('\n=================================================================\n')
            logging.info(f'model report : {model_report}')

            #to get the best model score from dictionary
            best_model_score=max(sorted(model_report.values()))

            best_model_name=list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            best_model=models[best_model_name]

            print(f'best model found,model name : {best_model_name} , R2 score : {best_model_score}')
            print('\n==========================================================================\n')
            logging.info(f'best model found, model name: {best_model_name}, R2 score : {best_model_score}')


            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )

        except Exception as e:
            logging.info('exception occured at model training')
            raise CustomException(e,sys)    