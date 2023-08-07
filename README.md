# Bank Customers Churn Prediction 🏦💔

## 📝 Description 
This project focuses on predicting whether a bank customer is likely to churn (leave the bank) based on various features such as credit score, age, tenure, balance, number of products, etc.

## 📊 Dataset 
The dataset used for this project is stored in the file "Churn_Modelling.csv."

## 🎯 Approach 
1. Data Loading and Exploration:
   - Displaying the top 5 rows of the dataset.
   - Checking for null values and data types.
   - Dropping irrelevant features ('RowNumber', 'CustomerId', 'Surname').
   - Encoding categorical data using one-hot encoding.

2. Handling Imbalanced Data:
   - Checking the distribution of the target variable 'Exited.'
   - Using Synthetic Minority Over-sampling Technique (SMOTE) to balance the data.

3. Splitting the Dataset:
   - Splitting the data into the training set and test set.

4. Feature Scaling:
   - Scaling the features using StandardScaler.

5. Model Training and Evaluation:
   - Training multiple classifiers: Logistic Regression, Support Vector Classifier (SVC), KNeighbors Classifier, Decision Tree Classifier, Random Forest Classifier, and Gradient Boosting Classifier.
   - Evaluating each model's performance based on accuracy.

6. Model Comparison:
   - Visualizing the accuracy of each model using a bar plot.

7. Saving the Model:
   - Saving the trained Random Forest Classifier model using joblib.

## 📥 Installations 
To run the code, you need to install the required Python libraries. Use the following command to install the dependencies:

```
pip install pandas scikit-learn seaborn imbalanced-learn joblib
```

## ⚙️ Setup 
1. Clone the repository.
2. Ensure you have the "Churn_Modelling.csv" file in the project directory.

## 🛠️ Requirements 
- Python 3.x
- Pandas
- Scikit-learn
- Seaborn
- Imbalanced-learn
- Joblib

## 🚀 Technology Used 
- Python
- Machine Learning
- Data Preprocessing
- Logistic Regression
- Support Vector Machine (SVM)
- KNeighbors Classifier
- Decision Tree Classifier
- Random Forest Classifier
- Gradient Boosting Classifier

## ▶️ Run 
1. Execute the "code-Notebook" script to preprocess the data, train the models, and evaluate the model performance.
2. The script will save the trained Random Forest Classifier model as "churn_predict_model" using joblib.
3. To make predictions using the saved model, execute the following code:
   ```python
   import joblib

   model = joblib.load('churn_predict_model')
   result = model.predict([[619, 42, 2, 0.0, 0, 0, 0, 101348.88, 0, 0, 0]])
   print(result)
   ```

---

📝 I frequently create content focused on complete projects in the realm of data science using Python and R.

💬 Feel free to inquire about data science, computer vision, Python, and R.

---

<p align="Right">(◕‿◕) Thank you for exploring my GitHub project repository. 👋</p>
