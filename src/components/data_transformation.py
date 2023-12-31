import sys
from dataclasses import dataclass

import numpy as np 
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer,KNNImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from sklearn.model_selection import train_test_split
from src.exception import CustomException
from src.logger import logging
import os

from src.utils import save_object


@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts',"proprocessor.pkl")


class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()


    
    def get_data_transformer_object(self,train_df):
        # '''
        # This function is responsible for data trnasformation
        
        # '''
        try:
            numerical_columns = ["CustomerID","CityTier","HourSpendOnApp","NumberOfDeviceRegistered","SatisfactionScore","NumberOfAddress",
                                 "Complain","OrderAmountHikeFromlastYear","CouponUsed","OrderCount","DaySinceLastOrder",
                                 "CashbackAmount","Tenure_update","WarehouseToHome_update"]
            categorical_columns = ["PreferredLoginDevice","PreferredPaymentMode","Gender","PreferedOrderCat","MaritalStatus"]
            all_columns=["CustomerID","CityTier","HourSpendOnApp","NumberOfDeviceRegistered","SatisfactionScore","NumberOfAddress",
                                 "Complain","OrderAmountHikeFromlastYear","CouponUsed","OrderCount","DaySinceLastOrder",
                                 "CashbackAmount","Tenure_update","WarehouseToHome_update","PreferredLoginDevice",
                                 "PreferredPaymentMode","Gender","PreferedOrderCat","MaritalStatus"]
            
            # categorical_columns=train_df[["PreferredLoginDevice","PreferredPaymentMode","Gender","PreferedOrderCat","MaritalStatus"]]
            # all_columns=train_df
            # numerical_columns=train_df[["CustomerID","CityTier","HourSpendOnApp","NumberOfDeviceRegistered","SatisfactionScore","NumberOfAddress",
            #                      "Complain","OrderAmountHikeFromlastYear","CouponUsed","OrderCount","DaySinceLastOrder",
            #                      "CashbackAmount","Tenure_update","WarehouseToHome_update"]]
            # train_df=train_df.drop( columns=["Churn"],axis=1)
            # numerical_columns=train_df.select_dtypes(exclude="object").columns
            # categorical_columns=train_df.select_dtypes(include="object").columns

            

            

            num_pipeline=Pipeline(
                steps=[
                ('KNNimputer' ,KNNImputer(n_neighbors=5) ),
                ('scale' , StandardScaler()  )

                ]
            )

            cat_pipeline=Pipeline(
                steps=[
                ('one_hot' , OneHotEncoder(sparse_output=False,handle_unknown="ignore" ) ),
                ('KNNimputer' ,KNNImputer(n_neighbors=5) ),
                ('scale' , StandardScaler()  )
                ]
            )

            logging.info(f"Categorical columns: {categorical_columns}")
            logging.info(f"Numerical columns: {numerical_columns}")

            # trf1=ColumnTransformer(transformers=[
            #       ('one_hot' , OneHotEncoder(sparse_output=False,handle_unknown="ignore" ) ,categorical_columns)
            #            ],remainder="passthrough")
            
            # trf2=ColumnTransformer([
            #  ('KNNimputer' ,KNNImputer(n_neighbors=5),slice(32))
    
            #         ] ,remainder='passthrough')
            
            # trf3=ColumnTransformer([
            #     ('scale' , StandardScaler() ,[] )
            #     ],remainder="passthrough")
            
            # pipe=Pipeline([
            #      ("trf1",trf1),
            #      ("trf2",trf2),
            #      ("trf3",trf3),
            #            ])






            # pipeline_obj=Pipeline(steps=[
            #     ('one_hot' , OneHotEncoder(sparse_output=False,handle_unknown="ignore" ) ,categorical_columns),
            #     ('KNNimputer' ,KNNImputer(n_neighbors=5), all_columns),
            #     ('scale' , StandardScaler() ,all_columns),


            # ])

            preprocessor=ColumnTransformer(
                transformers=[
                    ("num_pipeline",num_pipeline,numerical_columns),
                    ("cat_pipelines",cat_pipeline,categorical_columns)
                ]
            )

            # base=Pipeline(steps=[
            #     ('preprocessor',preprocessor)
            # ])

            return preprocessor
        
        except Exception as e:
            raise CustomException(e,sys)
              
            
        

    def initiate_data_transformation(self,train_path,test_path):
        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)

            logging.info("read train and test data completed")

            logging.info("obtaining preprocessing object")

            preprocessing_obj= self.get_data_transformer_object(train_df)

            target_column_name="Churn"

            # numerical_columns = ["CustomerID","CityTier","HourSpendOnApp","NumberOfDeviceRegistered","SatisfactionScore","NumberOfAddress",
            #                      "Complain","OrderAmountHikeFromlastYear","CouponUsed","OrderCount","DaySinceLastOrder",
            #                      "CashbackAmount","Tenure_update","WarehouseToHome_update"]
            # categorical_columns = ["PreferredLoginDevice","PreferredPaymentMode","Gender","PreferedOrderCat","MaritalStatus"]
            # all_columns=[["CustomerID","CityTier","HourSpendOnApp","NumberOfDeviceRegistered","SatisfactionScore","NumberOfAddress",
            #                      "Complain","OrderAmountHikeFromlastYear","CouponUsed","OrderCount","DaySinceLastOrder",
            #                      "CashbackAmount","Tenure_update","WarehouseToHome_update","PreferredLoginDevice",
            #                      "PreferredPaymentMode","Gender","PreferedOrderCat","MaritalStatus"]]

            # categorical_columns=train_df[["PreferredLoginDevice","PreferredPaymentMode","Gender","PreferedOrderCat","MaritalStatus"]]
            # # all_columns=train_df
            # numerical_columns=train_df[["CustomerID","CityTier","HourSpendOnApp","NumberOfDeviceRegistered","SatisfactionScore","NumberOfAddress",
            #                      "Complain","OrderAmountHikeFromlastYear","CouponUsed","OrderCount","DaySinceLastOrder",
            #                      "CashbackAmount","Tenure_update","WarehouseToHome_update"]]
            
            # X_train=train_df.loc[:, train_df.columns != 'Churn']
            # Y_train=train_df["Churn"]

            # X_test=test_df.loc[:, test_df.columns != 'Churn']
            # Y_test=test_df["Churn"]


            
            # x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size = 0.3, random_state = 10)

            

            input_feature_train_df=train_df.drop( columns=[target_column_name],axis=1)
            target_feature_train_df=train_df[target_column_name]

            input_feature_test_df=test_df.drop(columns=[target_column_name],axis=1)
            target_feature_test_df=test_df[target_column_name]
        
            logging.info(
                f"Applying preprocessing object on training dataframe and testing dataframe."
            )

            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)


            train_arr = np.c_[
                input_feature_train_arr, np.array(target_feature_train_df)
            ]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            logging.info(f"Saved preprocessing object.")

            
            save_object(

                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj

            )

            

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
            )
        except Exception as e:
            raise CustomException(e,sys)

            

