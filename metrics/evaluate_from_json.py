import json


def load_data(filepath):
    with open(filepath, "r") as file:
        return json.load(file)


def calculate_confusion_matrix(data):
    TP = FP = TN = FN = 0

    for item in data:
        actual = item["actual"]
        predicted = item["predicted"]

        if actual == 1 and predicted == 1:
            TP += 1
        elif actual == 0 and predicted == 1:
            FP += 1
        elif actual == 0 and predicted == 0:
            TN += 1
        elif actual == 1 and predicted == 0:
            FN += 1

    return TP, FP, TN, FN


def precision(TP, FP):
    return TP / (TP + FP) if (TP + FP) != 0 else 0


def recall(TP, FN):
    return TP / (TP + FN) if (TP + FN) != 0 else 0


def f1_score(p, r):
    return 2 * (p * r) / (p + r) if (p + r) != 0 else 0


if __name__ == "__main__":
    data = load_data("data/sample_predictions.json")

    TP, FP, TN, FN = calculate_confusion_matrix(data)

    p = precision(TP, FP)
    r = recall(TP, FN)
    f1 = f1_score(p, r)

    print("Confusion Matrix:")
    print("TP:", TP, "FP:", FP, "TN:", TN, "FN:", FN)
    print("Precision:", round(p, 2))
    print("Recall:", round(r, 2))
    print("F1 Score:", round(f1, 2))