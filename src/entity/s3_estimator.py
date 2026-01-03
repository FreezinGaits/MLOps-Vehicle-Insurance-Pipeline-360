from src.cloud_storage.aws_storage import SimpleStorageService
from src.exception import MyException
from src.entity.estimator import MyModel
import sys
from pandas import DataFrame


class Proj1Estimator:
    """
    This class is used to save and retrieve our model from s3 bucket and to do prediction
    """

    def __init__(self,bucket_name,model_path,):
        """
        :param bucket_name: Name of your model bucket
        :param model_path: Location of your model in bucket
        """
        self.bucket_name = bucket_name
        self.s3 = SimpleStorageService()
        self.model_path = model_path
        self.loaded_model:MyModel=None


    def is_model_present(self,model_path):
        try:
            return self.s3.s3_key_path_available(bucket_name=self.bucket_name, s3_key=model_path)
        except MyException as e:
            print(e) 
            return False

    def load_model(self,)->MyModel:
        """
        Load the model from the model_path
        :return:
        """

        return self.s3.load_model(self.model_path,bucket_name=self.bucket_name)

    def save_model(self,from_file,remove:bool=False)->None:
        """
        Save the model to the model_path
        :param from_file: Your local system model path
        :param remove: By default it is false that mean you will have your model locally available in your system folder
        :return:
        """
        try:
            self.s3.upload_file(from_file,
                                to_filename=self.model_path,
                                bucket_name=self.bucket_name,
                                remove=remove
                                )
        except Exception as e:
            raise MyException(e, sys)


    def predict(self,dataframe:DataFrame):
        """
        :param dataframe:
        :return:
        """
        try:
            if self.loaded_model is None:
                self.loaded_model = self.load_model()
            return self.loaded_model.predict(dataframe=dataframe)
        except Exception as e:
            raise MyException(e, sys)




# 1. Big Picture: What Is Proj1Estimator?

  # Proj1Estimator is a model manager + inference wrapper.
  # Its responsibilities are very specific and intentional:

  # 1. Interact with S3 to:
    # Check if a model exists
    # Load a trained model
    # Save a trained model
  # 2. Cache the loaded model in memory
  # 3. Run predictions on input data

  # It does NOT:
    # train the model
    # preprocess data
    # talk directly to AWS credentials

  # Those responsibilities are already delegated elsewhere.

  # This is clean architecture.

# 2. Why This Class Exists (Design Intent)
  # In a real ML system, you want:
    # Training code → saves model
    # Inference code → loads model
    # Prediction code → uses model

  # But you do not want:
    # S3 logic everywhere
    # pickle.load() scattered across files
    # repeated S3 downloads
    
  # This class centralizes model lifecycle management.