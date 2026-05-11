import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv("data/water_usage_dataset.csv")

season_encoder = LabelEncoder()
rain_encoder = LabelEncoder()
target_encoder = LabelEncoder()

df["season"] = season_encoder.fit_transform(df["season"])
df["rainfall_level"] = rain_encoder.fit_transform(df["rainfall_level"])
df["category"] = target_encoder.fit_transform(df["category"])

X = df[["people","season","rainfall_level","daily_usage"]]
y = df["category"]

X_train,X_test,y_train,y_test = train_test_split(
X,y,test_size=0.2,random_state=42
)

model = XGBClassifier(
n_estimators=200,
learning_rate=0.05,
max_depth=5
)

model.fit(X_train,y_train)

pred = model.predict(X_test)

print("Accuracy:",accuracy_score(y_test,pred))

pickle.dump(
(model,season_encoder,rain_encoder,target_encoder),
open("model.pkl","wb")
)