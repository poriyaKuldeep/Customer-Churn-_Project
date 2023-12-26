import sys
import pandas as pd
import numpy as np
# import pickle
from src.exception import CustomException
from src.utils import load_object

class PredictPipline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path='artifacts\model.pkl'
            preprocessor_path='artifacts\proprocessor.pkl'
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            # preprocessor=pickle.load(open('artifacts\proprocessor.pkl','rb'))
            data_scaled=preprocessor.transform(features)
            pred=model.predict(data_scaled)
            return pred
        
        except Exception as e:
           raise CustomException(e,sys)
       

class CustomData:
    def __init__(self,
                 CustomerID:int,
                 PreferredLoginDevice:str,
                 CityTier:int,
                 PreferredPaymentMode:str,
                 Gender:str,
                 HourSpendOnApp:int,
                 NumberOfDeviceRegistered:int,
                 PreferedOrderCat:str,
                 SatisfactionScore:int,
                 MaritalStatus:str,
                 NumberOfAddress:int,
                 Complain:int,
                 OrderAmountHikeFromlastYear:int,
                 CouponUsed:int,
                 OrderCount:int,
                 DaySinceLastOrder:int,
                 CashbackAmount:int,
                 Tenure_update:int,
                 WarehouseToHome_update:int,
                 ):
        self.CustomerID=CustomerID
        self.PreferredLoginDevice=PreferredLoginDevice
        self.CityTier=CityTier
        self.PreferredPaymentMode=PreferredPaymentMode
        self.Gender=Gender
        self.HourSpendOnApp=HourSpendOnApp
        self.NumberOfDeviceRegistered=NumberOfDeviceRegistered
        self.PreferedOrderCat=PreferedOrderCat
        self.SatisfactionScore=SatisfactionScore
        self.MaritalStatus=MaritalStatus
        self.NumberOfAddress=NumberOfAddress
        self.Complain=Complain
        self.OrderAmountHikeFromlastYear=OrderAmountHikeFromlastYear
        self.CouponUsed=CouponUsed
        self.OrderCount=OrderCount
        self.DaySinceLastOrder=DaySinceLastOrder
        self.CashbackAmount=CashbackAmount
        self.Tenure_update=Tenure_update
        self.WarehouseToHome_update=WarehouseToHome_update


    def get_data_as_data_frame(self):
        try:
        #           CustomerID=self.CustomerID
        #           PreferredLoginDevice=self.PreferredLoginDevice
        #           CityTier=self.CityTier
        #           PreferredPaymentMode=self.PreferredPaymentMode
        #           Gender=self.Gender
        #           HourSpendOnApp=self.HourSpendOnApp
        #           NumberOfDeviceRegistered=self.NumberOfDeviceRegistered
        #           PreferedOrderCat= self.PreferedOrderCat
        #           SatisfactionScore=self.SatisfactionScore
        #           MaritalStatus=self.MaritalStatus
        #           NumberOfAddress=self.NumberOfAddress
        #           Complain=self.Complain
        #           OrderAmountHikeFromlastYear=self.OrderAmountHikeFromlastYear
        #           CouponUsed= self.CouponUsed
        #           OrderCount=self.OrderCount
        #           DaySinceLastOrder=self.DaySinceLastOrder
        #           CashbackAmount=self.CashbackAmount
        #           Tenure_update=self.Tenure_update
        #           WarehouseToHome_update=self.WarehouseToHome_update

        #           data=np.array([CustomerID,PreferredLoginDevice,CityTier,PreferredPaymentMode,Gender,
        #                          HourSpendOnApp,NumberOfDeviceRegistered,PreferedOrderCat,SatisfactionScore,
        #                          MaritalStatus,NumberOfAddress,Complain,OrderAmountHikeFromlastYear,CouponUsed,
        #                          OrderCount,DaySinceLastOrder,CashbackAmount,Tenure_update,WarehouseToHome_update,
        #                          ] ,dtype=object).reshape(1,19)
                  
        #           return data

        

            custome_data_input_dict={
                "CustomerID":[self.CustomerID],
                "PreferredLoginDevice":[self.PreferredLoginDevice],
                "CityTier":[self.CityTier],
                "PreferredPaymentMode":[self.PreferredPaymentMode],
                "Gender":[self.Gender],
                "HourSpendOnApp":[self.HourSpendOnApp],
                "NumberOfDeviceRegistered":[self.NumberOfDeviceRegistered],
                "PreferedOrderCat":[self.PreferedOrderCat],
                "SatisfactionScore":[self.SatisfactionScore],
                "MaritalStatus":[self.MaritalStatus],
                "NumberOfAddress":[self.NumberOfAddress],
                "Complain":[self.Complain],
                "OrderAmountHikeFromlastYear":[self.OrderAmountHikeFromlastYear],
                "CouponUsed":[self.CouponUsed],
                "OrderCount":[self.OrderCount],
                "DaySinceLastOrder":[self.DaySinceLastOrder],
                "CashbackAmount":[self.CashbackAmount],
                "Tenure_update":[self.Tenure_update],
                "WarehouseToHome_update":[self.WarehouseToHome_update],
            }

            return pd.DataFrame(custome_data_input_dict)
        
        except Exception as e:
            raise CustomException(e,sys)


