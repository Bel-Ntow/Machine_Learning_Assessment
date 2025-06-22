# PROJECT REPORT

## 1. Project Overview
This project involved analyzing data from a bank’s direct marketing campaigns aimed at promoting term deposit subscriptions. The analysis followed a structured approach: initial data exploration, feature engineering, preprocessing, model building, and performance evaluation.


## 2. Objective
The goal of this project is to build a predictive model that determines whether a client will subscribe to a term deposit based on their personal, contact, and campaign-related attributes provided in the dataset.


## 3. Data Overview

- **Training set**: 45,211 rows × 17 columns  
- **Test set**: 4,521 rows × 17 columns  
- **Target variable**: `y` (binary: "yes" or "no")



## 4. Preprocessing and Analysis

###  Missing Values
- No missing values in either training or test datasets.

###  Duplicates
- No duplicate rows were found.

### Outlier Detection
- Outliers in numerical columns were detected using the **IQR (Interquartile Range)** method.
- Instead of removing them, extreme values were **capped** to reduce their influence.

### Feature Engineering
- Categorical variables were one-hot encoded.
- Numerical features were scaled using `StandardScaler`.

### Correlation
- Pairwise correlations were checked.
- Overall, most features had low to moderate correlation with each other.



## 5. Modeling Approach

- **Model used**: Logistic Regression  
- Class imbalance was handled using `class_weight='balanced'`.
- The model was integrated into a `Pipeline` that includes:
  - **ColumnTransformer** for scaling numeric features and encoding categorical ones


## 6. Model Performance

### Training Set

- **Accuracy**: 83.13%
- **Precision (positive class - "yes")**: 0.40
- **Recall (positive class - "yes")**: 0.84
- **F1-score (positive class)**: 0.54

**Confusion Matrix**:
[[33151 6771]
[ 856 4433]]


###  Test Set

- **Accuracy**: 81.53%
- **Precision (positive class - "yes")**: 0.37  
- **Recall (positive class - "yes")**: 0.83  
- **F1-score (positive class)**: 0.51

**Confusion Matrix**:
[[3253 747]
[ 88 433]]



## 7. Deployment

A simple **Streamlit web app** was developed to interact with the trained model. This allows end-users to input client information and receive real-time predictions.

###  User Inputs:
- Client profile details (e.g., age, job, marital status, balance, etc.)

###  App Output:
- **Prediction**: Whether the client is likely to subscribe to a term deposit ("Yes" or "No")
- **Probability**: Probability for the prediction

This deployment makes the model accessible to non-technical stakeholders, such as marketing teams, enabling data-driven decision-making during campaigns.



## 8. Insights
- The dataset is **imbalanced**, with far fewer positive outcomes ("yes").
- The model achieves **high recall** on the positive class, which is important in marketing.


## 9. Conclusion
A Logistic Regression model was developed and evaluated, showing strong performance, particularly in identifying potential term deposit subscribers. The model achieved over **81%** accuracy on the test set and high recall **(83%)** for the positive class, making it useful for targeting clients in future campaigns.
