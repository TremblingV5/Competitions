import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from loguru import logger

from utils.optimizer import GAOptimizer

logger.add("./rf_optimize.log")

data = pd.read_csv("./data/all.csv")
data = data.drop(labels="Glucose Value (mg/dL)", axis=1)

Y = data["Y"]
X = data.drop(labels="Y", axis=1)

train_x, test_x, train_y, test_y = train_test_split(X, Y)

def model(params):
    model = RandomForestClassifier(**params)
    model.fit(train_x, train_y)
    pred = model.predict(test_x)
    return accuracy_score(test_y, pred)

def target(p):
    params = {
        "n_estimators": int(p[0])
    }
    acc = model(params)
    logger.info(f"ACC: {acc}, {params}")


if __name__ == "__main__":
    lb = [1]
    ub = [2000]

    optimizer = GAOptimizer(
        func=target, lb=lb, ub=ub
    )

    bext_x, best_y = optimizer.run()
    print(bext_x, best_y)

