import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

columns = ['buying','maint','doors','persons','leg_boot','safety','class']
data = pd.read_csv(r"C:\naji\practice\car.data" , names = columns)
print(data.head())
print(data.info())
print(data.describe()) 
print(data.isnull().sum())
data.rename(columns={'buying': 'purchasing'}, inplace=True)
print(data.head())

X = data.drop('purchasing', axis=1)
y = data['persons']


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42 
)


print(X.head())
print(y.head())

X_encoded = pd.get_dummies(X)
# If target is categorical too, encode it:
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y_encoded = le.fit_transform(y)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X_encoded, y_encoded, test_size=0.2, random_state=42
)

print(X_train.head())
print(y_train[:5])

# Train Logistic Regression
model = LogisticRegression(max_iter=1000)  # Increase max_iter if needed
model.fit(X_train, y_train)

# Predict on test set
y_pred = model.predict(X_test)

# Evaluate
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred, target_names=le.classes_))

# Confusion matrix
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8,6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=le.classes_, yticklabels=le.classes_)
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()





