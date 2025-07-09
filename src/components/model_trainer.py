import os
import sys
import pickle
from sklearn.neighbors import NearestNeighbors
from scipy.sparse import csr_matrix
from src.logger.log import logging
from src.config.configuration import AppConfiguration
from src.exception.exception_handler import AppException

#import mlflow
import mlflow.sklearn

class ModelTrainer:
    def __init__(self, app_config = AppConfiguration()):
        try:
            self.model_trainer_config = app_config.get_model_trainer_config()
            mlflow.set_tracking_uri("http://localhost:5000")  # Or remote URI
            mlflow.set_experiment("Book_Recommender")
        except Exception as e:
            raise AppException(e, sys) from e


    def train(self):
        try:
            #loading pivot data
            with mlflow.start_run():
                book_pivot = pickle.load(open(self.model_trainer_config.transformed_data_file_dir,'rb'))
                book_sparse = csr_matrix(book_pivot)
                #Training model
                model = NearestNeighbors(algorithm= 'brute')
                model.fit(book_sparse)

                mlflow.log_params({
                                    "algorithm": "brute"
                })
                mlflow.sklearn.log_model(model, "recommender_model")

                mlflow.set_tag("model_type", "collaborative_filtering")

                print(f"Logged to MLflow run: {mlflow.active_run().info.run_id}")
                #Saving model object for recommendations
                os.makedirs(self.model_trainer_config.trained_model_dir, exist_ok=True)
                file_name = os.path.join(self.model_trainer_config.trained_model_dir,self.model_trainer_config.trained_model_name)
                pickle.dump(model,open(file_name,'wb'))
                logging.info(f"Saving final model to {file_name}")

        except Exception as e:
            raise AppException(e, sys) from e



    def initiate_model_trainer(self):
        try:
            logging.info(f"{'='*20}Model Trainer log started.{'='*20} ")
            self.train()
            logging.info(f"{'='*20}Model Trainer log completed.{'='*20} \n\n")
        except Exception as e:
            raise AppException(e, sys) from e
