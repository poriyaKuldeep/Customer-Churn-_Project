# E-commerce Customer Churn Prediction  - Kuldeep Poriya


### About the Problem statement :
Customer churn can be a very good business metric for companies like Netflix, Amazon, Meesho, etc. If an organization already knows that x percentage of users might lose interest from their product or is not happy with their product, then they can do some root cause analysis on why a particular user is on the verge of leaving the service and retain that user. It is said that retaining an existing customer is cheaper than acquiring a new one. Hence, predicting whether a customer will churn or not will help the organization to retain existing customers and grow their business.



### Introduction About the Data :

**The dataset** The goal is to predict whetehr a customer will churn or not  (Classification Analysis).

There are 19 independent variables (including `CustomerID`):

* `CustomerID` :  Unique customer ID.
* `PreferredLoginDevice` :  Preferred login device of customer.
* `CityTier` : City tier.
* `PreferredPaymentMode` : Preferred payment method of customer.
* `Gender` : Gender of customer.
* `HourSpendOnApp` : Number of hours spend on mobile application or website.
* `NumberOfDeviceRegistered` : Total number of deceives is registered on particular customer.
* `PreferedOrderCat` : Preferred order category of customer in last month.
* `SatisfactionScore` :  Satisfactory score of customer on service.
* `MaritalStatus` : Marital status of customer.
* `NumberOfAddress` : Total number of added added on particular customer.
* `Complain` : Any complaint has been raised in last month.
* `OrderAmountHikeFromlastYear` : Percentage increases in order from last year.
* `CouponUsed` :  Total number of coupon has been used in last month.
* `OrderCount` : Total number of orders has been places in last month.
* `DaySinceLastOrder` :Day Since last order by customer.
* `CashbackAmount` : Average cashback in last month.
* `Tenure ` : Tenure of customer in organization.
* `WarehouseToHome ` : Distance in between warehouse to home of customer.
* `MaritalStatus` : Marital status of customer.


Target variable:
* `Churn `: Churn Flag 0 or 1.

Dataset Source Link :
[https://www.kaggle.com/datasets/ankitverma2010/ecommerce-customer-churn-analysis-and-prediction?source=post_page-----1f824f6d6108--------------------------------](https://www.kaggle.com/datasets/ankitverma2010/ecommerce-customer-churn-analysis-and-prediction?source=post_page-----1f824f6d6108--------------------------------)



<!-- ### Check this link for details : [American Gem Society](https://www.americangemsociety.org/ags-diamond-grading-system/)

# AWS Deployment Link :

AWS Elastic Beanstalk link : [http://gemstonepriceutkarshgaikwad-env.eba-7zp3wapg.ap-south-1.elasticbeanstalk.com/](http://gemstonepriceutkarshgaikwad-env.eba-7zp3wapg.ap-south-1.elasticbeanstalk.com/) -->

# Screenshot of UI

<img src="https://github.com/poriyaKuldeep/Customer-Churn-_Project/blob/main/Screenshot%20(33).png">

<!-- # YouTube Video Link

Link for YouTube Video : Click the below thumbnail to open 

[![https://youtu.be/Xvk5r0t_RQw](https://i.ytimg.com/vi/Xvk5r0t_RQw/hqdefault.jpg?sqp=-oaymwEcCNACELwBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLBbp5SouquUm3Y3t-NYfOYsg4N4oQ)](https://youtu.be/Xvk5r0t_RQw)

# AWS API Link

API Link : [http://gemstonepriceutkarshgaikwad-env.eba-7zp3wapg.ap-south-1.elasticbeanstalk.com/predictAPI](http://gemstonepriceutkarshgaikwad-env.eba-7zp3wapg.ap-south-1.elasticbeanstalk.com/predictAPI)

# Postman Testing of API :

![API Prediction](./Screenshots/APIPrediction.jpg) -->

# Approach for the project 

1. Data Ingestion : 
    * In Data Ingestion phase the data is first read as csv. 
    * Then the data is split into training and testing and saved as csv file.

2. Data Transformation : 
    * In this phase a ColumnTransformer Pipeline is created.
    * for Numeric Variables first SimpleImputer is applied with strategy median , then Standard Scaling is performed on numeric data.
    * for Categorical Variables SimpleImputer is applied with most frequent strategy, then ordinal encoding performed , after this data is scaled with Standard Scaler.
    * This preprocessor is saved as pickle file.

3. Model Training : 
    * In this phase base model is tested . The best model found was catboost regressor.
    * After this hyperparameter tuning is performed on catboost and knn model.
    * A final VotingRegressor is created which will combine prediction of catboost, xgboost and knn models.
    * This model is saved as pickle file.

4. Prediction Pipeline : 
    * This pipeline converts given data into dataframe and has various functions to load pickle files and predict the final results in python.

5. Flask App creation : 
    * Flask app is created with User Interface to predict the gemstone prices inside a Web Application.

# Exploratory Data Analysis Notebook

Link : [EDA Notebook](./notebook/1_EDA_Gemstone_price.ipynb)

# Model Training Approach Notebook

Link : [Model Training Notebook](./notebook/2_Model_Training_Gemstone.ipynb)

# Model Interpretation with LIME 

Link : [LIME Interpretation](./notebook/3_Explainability_with_LIME.ipynb)
