def calculate_confusion_matrix(actual, predicted):
    if len(actual) != len(predicted):
        raise ValueError("Length mismatch")

    TP = FP = TN = FN = 0

    for i in range(len(actual)):
        if actual[i] == 1 and predicted[i] == 1:
            TP += 1
        elif actual[i] == 0 and predicted[i] == 1:
            FP += 1
        elif actual[i] == 0 and predicted[i] == 0:
            TN += 1
        elif actual[i] == 1 and predicted[i] == 0:
            FN += 1

    return TP, FP, TN, FN


def precision(TP, FP):
    if TP + FP == 0:
        return 0
    return TP / (TP + FP)


def recall(TP, FN):
    if TP + FN == 0:
        return 0
    return TP / (TP + FN)


def f1_score(p, r):
    if p + r == 0:
        return 0
    return 2 * (p * r) / (p + r)


if __name__ == "__main__":
    actual = [1, 0, 1, 1, 0]
    predicted = [1, 1, 1, 0, 0]

    TP, FP, TN, FN = calculate_confusion_matrix(actual, predicted)

    p = precision(TP, FP)
    r = recall(TP, FN)
    f1 = f1_score(p, r)

    print("TP:", TP)
    print("FP:", FP)
    print("TN:", TN)
    print("FN:", FN)
    print("Precision:", round(p, 2))
    print("Recall:", round(r, 2))
    print("F1 Score:", round(f1, 2))