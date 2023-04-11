from utils.one_hot import OneHotBuilder
from utils import outlier
from utils.read_data import FileReader
from sklearn.metrics import accuracy_score
from utils.optimizer import GAOptimizer
from loguru import logger
from lightgbm import LGBMClassifier


def solve_outlier(data):
    solver = outlier.OutlierHandler(data)
    return solver.solve("default", outlier.FillNaByValueStrategy("unknown")).build()


def one_hot(data):
    builder = OneHotBuilder(data, "id")
    data = builder.set("job")\
        .set("marital")\
        .set("default")\
        .set("housing")\
        .set("contact")\
        .set("month") \
        .set("day_of_week")\
        .set("poutcome")\
        .set("education")\
        .set("loan")\
        .build()
    return data


def solve_subscribe(data):
    data["subscribe"].replace({
        "yes": 1,
        "no": 0
    }, inplace=True)
    return data


def read():
    reader = FileReader("./data/train.csv", "subscribe", [solve_outlier, one_hot, solve_subscribe])
    return reader.read()


def read_test():
    reader = FileReader("./data/test.csv", "subscribe", [solve_outlier, one_hot, solve_subscribe])
    return reader.read_no_seg()


logger.add("./BankCustomerSubscriptionProductForecase.log")
train_x, train_y, test_x, test_y = read()


def target(p):
    params = {
        "learning_rate": p[0],
    }
    acc = model(params)
    logger.info(f"ACC: {acc} Learning rate: {p[0]}")
    return acc


def model(params):
    model = LGBMClassifier(**params)
    model.fit(train_x, train_y)
    pred = model.predict(test_x)
    return accuracy_score(test_y, pred)


if __name__ == "__main__":
    lb = [0]
    ub = [0.01]

    optimizer = GAOptimizer(
        func=target, lb=lb, ub=ub
    )
    best_x, best_y = optimizer.run()
    print(best_x, best_y)
