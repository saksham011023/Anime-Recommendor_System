from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input,Embedding,Dot,Flatten,Dense,Activation,BatchNormalization
from utils.common_functions import read_yaml
from src.logger import get_logger
from src.custom_exception import CustomException

logger=get_logger(__name__)

class BaseModel:
    def __init__(self,config_path):
        try:
            self.config=read_yaml(config_path)
            logger.info("Loaded configuration from config.yaml")
        except Exception as e:
            raise CustomException(f"Error loading the configuration {e}")
        
    def RecommendorNet(self,n_users,n_anime):
        try:
            
            embedding_size=self.config["model"]["embedding_size"] #no of vectors

            user=Input(name="user",shape=[1])

            user_embedding=Embedding(name="user_embedding",input_dim=n_users,output_dim=embedding_size)(user) #the embedding layer would be working on input layer

            anime=Input(name="anime",shape=[1])

            anime_embedding=Embedding(name="anime_embedding",input_dim=n_anime,output_dim=embedding_size)(anime)

            x=Dot(name="dot_product",normalize=True,axes=2)([user_embedding,anime_embedding]) #similarities between user and anime

            x=Flatten()(x) #Convertws high dimensional vector into single dimensional vector

            x=Dense(1,kernel_initializer="he_normal")(x)
            x=BatchNormalization()(x)
            x=Activation("sigmoid")(x)

            model=Model(inputs=[user,anime],outputs=x)
            model.compile(
                loss=self.config["model"]["loss"],
                optimizer=self.config["model"]["optimizer"],
                metrics=self.config["model"]["metrics"]
            )
            logger.info("Model created succesfully...")
            
            return model
        
        except Exception as e:
            logger.error(f"Error during model architecture {e}")
            raise CustomException("Failed to create model architecture",e)
        
