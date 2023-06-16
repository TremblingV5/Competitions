import numpy as np
import pandas as pd
from lightgbm import LGBMClassifier
from sklearn.svm import SVC
from xgboost import XGBClassifier
from catboost import CatBoostClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, r2_score, roc_auc_score
from utils.optimizer import GAOptimizer
from sklearn.ensemble import VotingClassifier


data = pd.read_csv("./data/all.csv")
data = data.drop(labels="Glucose Value (mg/dL)", axis=1)

Y = data["Y"]
X = data.drop(labels="Y", axis=1)

train_x, test_x, train_y, test_y = train_test_split(X, Y)

model1 = LGBMClassifier()
model2 = XGBClassifier()
model3 = RandomForestClassifier()
model4 = CatBoostClassifier()
model5 = HistGradientBoostingClassifier()

model = VotingClassifier(
    estimators=[
        ("lgbm", model1), ("xgb", model2), ("rf", model3), ("cb", model4), ("hgbc", model5)
    ],
    voting="hard"
)

model.fit(train_x, train_y)
predicted = model.predict(test_x)

print("Accuracy: ", accuracy_score(test_y, predicted))
print("Precision: ", precision_score(test_y, predicted))
print("Recall: ", recall_score(test_y, predicted))
print("R2-Score: ", r2_score(test_y, predicted))
print("ROC: ", roc_auc_score(test_y, predicted))
