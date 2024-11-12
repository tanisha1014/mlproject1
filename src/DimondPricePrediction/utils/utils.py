import os
import sys
import pickle
import numpy as np
import pandas as pd
from DimondPricePrediction.logger import logging
from DimondPricePrediction.exception import CustomException
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error

def save_object(file_path,obj):
    try:
        dir_path=os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        with open(file_path,"wb") as file_obj: ##save the pickle file
            pickle.dump(obj,file_obj)

    except Exception as e:
        raise CustomException(e,sys) 

def evaluate_model(x_train,y_train,x_test,y_test,models):
    try:
        report={}
        for i in range(len(models)):
            model= list(models.values())[i]
            #train model
            model.fit(x_train,y_train)

            ##predict the testing data
            y_test_pred=model.predict(x_test)

            ##get r2 scores for train and test data
            #train_model_score=r2_score(y_train,y_train_pred)
            test_model_score=r2_score(y_test,y_test_pred)

            report[list(models.keys())[i]]=test_model_score

        return report    

    except Exception as e:
        logging.info('exception occured during model training')
        raise CustomException(e,sys)        

def load_object(file_path):
    try:
        with open(file_path,'rb') as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        logging.info("exception occured in load_object function utils")
        raise CustomException(e,sys)        
        
#save_object Function
#
# python
#Copy code
#def save_object(file_path, obj):
#Defines a function named save_object that takes two parameters: file_path (where to save the object) and obj (the object to be saved).
#python
#Copy code
#    try:
#Starts a try block to handle exceptions that may occur during the execution.
#python
#Copy code
 #       dir_path = os.path.dirname(file_path)
#Extracts the directory path from the provided file_path.
#python
#Copy code
 #       os.makedirs(dir_path, exist_ok=True)
#Creates the directory specified in dir_path. If it already exists, it won't raise an error due to exist_ok=True.
#python
#Copy code
  #      with open(file_path, "wb") as file_obj:
#Opens a file at file_path in write-binary mode ("wb"), creating a file object file_obj.
#python
#Copy code
#            pickle.dump(obj, file_obj)
#Serializes (pickles) the object obj and writes it to the file file_obj.
#python
#Copy code
 #   except Exception as e:
#Catches any exceptions that occur during the try block.
#python
#Copy code
 #       raise CustomException(e, sys)
#Raises a custom exception (CustomException) that includes the caught exception and system-specific information.
#evaluate_model Function
#python
#Copy code
#def evaluate_model(x_train, y_train, x_test, y_test, models):
#Defines a function named evaluate_model that takes training data (x_train, y_train), testing data (x_test, y_test), and a dictionary of models (models).
#python
#Copy code
#    try:
#Starts a try block for error handling.
#python
#Copy code
        report = {}
#Initializes an empty dictionary named report to store the evaluation results of each model.
#python
#Copy code
#        for i in range(len(models)):
#Loops over the range of the length of the models dictionary.
#python
#Copy code
#            model = list(models.values())[i]
#Gets the model corresponding to the current index i from the models dictionary.
#python
#Copy code
#            model.fit(x_train, y_train)
#Trains (fits) the current model on the training data (x_train and y_train).
#python
#Copy code
#            y_test_pred = model.predict(x_test)
#Uses the trained model to make predictions on the testing data (x_test).
#python
#Copy code
#            test_model_score = r2_score(y_test, y_test_pred)
#Calculates the R-squared score (a measure of how well the model predicts) by comparing the true labels (y_test) with the predicted labels (y_test_pred).
#python
#Copy code
#            report[list(models.keys())[i]] = test_model_score
#Updates the report dictionary with the model name (from the keys of models) and its corresponding test score.
#python
#Copy code
#        return report
#Returns the report dictionary containing the evaluation scores for all models.
#python
#Copy code
#  except Exception as e:
#Catches any exceptions that occur during the try block.
#python
#Copy code
#       logging.info('exception occurred during model training')
#Logs an informational message about the exception that occurred during model training.
#python
#Copy code
#        raise CustomException(e, sys)
#Raises a custom exception with the caught exception and system information.
#load_object Function
#python
#Copy code
#def load_object(file_path):
#Defines a function named load_object that takes one parameter: file_path (the location of the saved object).
#python
#Copy code
#    try:
#Starts a try block for error handling.
#python
#Copy code
#        with open(file_path, 'rb') as file_obj:
#Opens the file at file_path in read-binary mode ("rb"), creating a file object file_obj.
#python
#Copy code
#            return pickle.load(file_obj)
#Deserializes (loads) the object from file_obj and returns it.
#python
#Copy code
 #   except Exception as e:
#Catches any exceptions that occur during the try block.
#python
#Copy code
#        logging.info("exception occurred in load_object function utils")
#Logs an informational message about the exception that occurred while loading the object.
#python
#Copy code
 #       raise CustomException(e, sys)
#Raises a custom exception with the caught exception and system information.
