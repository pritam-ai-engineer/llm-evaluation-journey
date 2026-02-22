def calculate_confusion_matrix(actual, predicted):
    """
    Calculate TP, FP, TN, FN values.
    """

    if len(actual) != len(predicted):
        raise ValueError("Length of actual and predicted lists must match")

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


if __name__ == "__main__":
    actual = [1, 0, 1, 1, 0]
    predicted = [1, 1, 1, 0, 0]

    TP, FP, TN, FN = calculate_confusion_matrix(actual, predicted)

    print("TP:", TP)
    print("FP:", FP)
    print("TN:", TN)
    print("FN:", FN)