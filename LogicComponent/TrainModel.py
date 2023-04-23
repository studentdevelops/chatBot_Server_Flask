import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import  os

data = pd.read_csv('Database\Surgical.csv')

# Split the dataset into features and target
X = data.drop('baseline_surgery', axis=1)
y = data['baseline_surgery']
print(X.columns)

# Split the dataset into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize the Random Forest Classifier
rfc = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the classifier on the training set
rfc.fit(X_train, y_train)

# Make predictions on the test set
y_pred = rfc.predict(X_test)

# Evaluate the performance of the classifier using accuracy score
accuracy = accuracy_score(y_test, y_pred)
print('Accuracy:', accuracy)

# Save the trained model to disk
model_path = os.path.join('MLMODELS', "rfc_model.pkl")
joblib.dump(rfc, model_path)

# Load the trained model from disk
#loaded_model = joblib.load(model_path)
