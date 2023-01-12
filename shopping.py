import csv
import sys

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python shopping.py data")

    # Load data from spreadsheet and split into train and test sets
    evidence, labels = load_data(sys.argv[1])
    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size=TEST_SIZE
    )

    # Train model and make predictions
    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)
    sensitivity, specificity = evaluate(y_test, predictions)

    # Print results
    print(f"Correct: {(y_test == predictions).sum()}")
    print(f"Incorrect: {(y_test != predictions).sum()}")
    print(f"True Positive Rate: {100 * sensitivity:.2f}%")
    print(f"True Negative Rate: {100 * specificity:.2f}%")


def load_data(filename):
    """
    Load shopping data from a CSV file `filename` and convert into a list of
    evidence lists and a list of labels. Return a tuple (evidence, labels).

    evidence should be a list of lists, where each list contains the
    following values, in order:
        - Administrative, an integer
        - Administrative_Duration, a floating point number
        - Informational, an integer
        - Informational_Duration, a floating point number
        - ProductRelated, an integer
        - ProductRelated_Duration, a floating point number
        - BounceRates, a floating point number
        - ExitRates, a floating point number
        - PageValues, a floating point number
        - SpecialDay, a floating point number
        - Month, an index from 0 (January) to 11 (December)
        - OperatingSystems, an integer
        - Browser, an integer
        - Region, an integer
        - TrafficType, an integer
        - VisitorType, an integer 0 (not returning) or 1 (returning)
        - Weekend, an integer 0 (if false) or 1 (if true)

    labels should be the corresponding list of labels, where each label
    is 1 if Revenue is true, and 0 otherwise.
    """
    month_dict = {"Jan": 0, "Feb": 1, "Mar": 2, "Apr": 3, "May": 4, "June": 5,
                  "Jul": 6, "Aug": 7, "Sep": 8, "Oct": 9, "Nov": 10, "Dec": 11}
    evidence = list()
    labels = list()
    f = open(filename, "r")
    # Skipping the CSV header
    f.readline()
    x = f.readline().strip()
    while x:
        lst = x.split(",")
        e = list()
        e.append(int(lst[0]))
        e.append(float(lst[1]))
        e.append(int(lst[2]))
        e.append(float(lst[3]))
        e.append(int(lst[4]))
        e.append(float(lst[5]))
        e.append(float(lst[6]))
        e.append(float(lst[7]))
        e.append(float(lst[8]))
        e.append(float(lst[9]))
        e.append(month_dict[lst[10]])
        e.append(int(lst[11]))
        e.append(int(lst[12]))
        e.append(int(lst[13]))
        e.append(int(lst[14]))
        e.append((1 if lst[15] == "Returning_Visitor" else 0))
        e.append((1 if lst[16] == "TRUE" else 0))
        labels.append((1 if lst[17] == "TRUE" else 0))
        evidence.append(e)
        x = f.readline().strip()
    return evidence, labels


def train_model(evidence, labels):
    """
    Given a list of evidence lists and a list of labels, return a
    fitted k-nearest neighbor model (k=1) trained on the data.
    """
    model = KNeighborsClassifier(n_neighbors=1)
    model.fit(evidence, labels)
    return model


def evaluate(labels, predictions):
    """
    Given a list of actual labels and a list of predicted labels,
    return a tuple (sensitivity, specificity).

    Assume each label is either a 1 (positive) or 0 (negative).

    `sensitivity` should be a floating-point value from 0 to 1
    representing the "true positive rate": the proportion of
    actual positive labels that were accurately identified.

    `specificity` should be a floating-point value from 0 to 1
    representing the "true negative rate": the proportion of
    actual negative labels that were accurately identified.
    """
    true_positive = 0
    total_positive = 0
    true_negative = 0
    total_negative = 0
    for x in range(len(labels)):
        if labels[x] == 1:
            total_positive += 1
            if labels[x] == predictions[x]:
                true_positive += 1
        elif labels[x] == 0:
            total_negative += 1
            if labels[x] == predictions[x]:
                true_negative += 1
    sensitivity = true_positive / total_positive
    specificity = true_negative / total_negative
    return sensitivity, specificity


if __name__ == "__main__":
    main()
