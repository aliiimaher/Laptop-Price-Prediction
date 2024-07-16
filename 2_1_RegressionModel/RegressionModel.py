import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
import joblib

df = pd.read_csv('./allDigikalaLaptops_CLEANED_001.csv')

# Drop unnecessary columns
df_cleaned = df.drop(['title', 'url'], axis=1)

# One-hot encode categorical features
df_encoded = pd.get_dummies(df_cleaned, columns=[
    'Processor manufacturer', 'Processor model', 'Processor series',
    'RAM', 'internal storage type', 'GPU manufacturer', 'GPU model'
])

# save column for test the result (only for debug)
# with open('columns.txt', 'w', encoding='utf-8-sig') as f:
#     for col in df_encoded.columns:
#         f.write(f'{col}\n')

# Slipt data (80% for train and 20% for test)
X = df_encoded.drop('price', axis=1)
y = df_encoded['price']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Save the model to a file
joblib.dump(model, 'laptop_price_model.pkl')

### Model efficiency calculations ###
# Predict the prices on the test set
y_pred = model.predict(X_test)

# Calculate the Mean Absolute Error (MAE) and R-squared score
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean Absolute Error (MAE): {mae}')
print(f'R-squared score: {r2}')

### Testing the model on a sample ###
df_new = pd.DataFrame(df_encoded.iloc[21]).T.drop(['price'], axis=1)
# print(df_encoded.iloc[21].values)
predicted_price = model.predict(df_new)
print("===========================")
print(f'Predicted Price: {predicted_price[0]}')
print(f'Actual Price: {df_encoded.iloc[21]["price"]}')
print(f'error: {predicted_price[0] - df_encoded.iloc[21]["price"]}')
