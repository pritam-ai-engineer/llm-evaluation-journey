def calculate_accuracy(actual, predicted):
    """
    Calculate classification accuracy.

    Parameters:
        actual (list): True labels
        predicted (list): Model predictions

    Returns:
        float: Accuracy score
    """

    if len(actual) != len(predicted):
        raise ValueError("Length of actual and predicted lists must match")

    correct = 0

    for i in range(len(actual)):
        if actual[i] == predicted[i]:
            correct += 1

    accuracy = correct / len(actual)
    return accuracy


if __name__ == "__main__":
    actual = [1, 0, 1, 1, 0]
    predicted = [1, 1, 1, 0, 0]

    score = calculate_accuracy(actual, predicted)

    print("Accuracy:", score)