from flask import Flask,request,render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData,PredictPipline


application=Flask(__name__)
app=application

##route for a home page:

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')
    
    else:
        data=CustomData(
          CustomerID=request.form.get('CustomerID'),
          PreferredLoginDevice=request.form.get('PreferredLoginDevice'),
          CityTier=request.form.get('CityTier'),
          PreferredPaymentMode=request.form.get('PreferredPaymentMode'),
          Gender=request.form.get('Gender'),
          HourSpendOnApp=float(request.form.get('HourSpendOnApp')),
          NumberOfDeviceRegistered=request.form.get('NumberOfDeviceRegistered'),
          PreferedOrderCat=request.form.get('PreferedOrderCat'),
          SatisfactionScore=request.form.get('SatisfactionScore'),
          MaritalStatus=request.form.get('MaritalStatus'),
          NumberOfAddress=request.form.get('NumberOfAddress'),
          Complain=request.form.get('Complain'),
          OrderAmountHikeFromlastYear=request.form.get('OrderAmountHikeFromlastYear'),
          CouponUsed=request.form.get('CouponUsed'),
          OrderCount=request.form.get('OrderCount'),
          DaySinceLastOrder=request.form.get('DaySinceLastOrder'),
          CashbackAmount=request.form.get('CashbackAmount'),
          Tenure_update=request.form.get('Tenure_update'),
          WarehouseToHome_update=request.form.get('WarehouseToHome_update')
        )
        
        pred_df=data.get_data_as_data_frame()
        print(pred_df)
        # print("before prediction")
        # preprocessor=pickle.load(open('artifacts\proprocessor.pkl','rb'))

        # data=preprocessor.fit_transform(pred_df)

        # model=pickle.load(open('artifacts\model.pkl','rb'))

        # pred=model.predict(data)



        predict_pipline=PredictPipline()
        # print("mid prediction")
        results=predict_pipline.predict(pred_df)
        # print("after Prediction")
        return render_template("home.html",results=results[0])
    
   
if __name__=="__main__":
    app.debug = True
    app.run()       