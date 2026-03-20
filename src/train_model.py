# src/train_model.py
import joblib
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from clean_data import load_and_clean

df = load_and_clean("../data/movies.csv")
X = df.drop("revenue", axis=1)
y = df["revenue"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

joblib.dump(model, "model.pkl")
print("✅ Model trained and saved.")
