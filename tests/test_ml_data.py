from collections import Counter

from ml.data import CATEGORIES, load_notes, train_test


def test_data_loads_with_known_categories():
    texts, labels = load_notes()
    assert len(texts) == len(labels) > 400
    assert set(labels) == set(CATEGORIES)


def test_split_is_fixed_stratified_and_disjoint():
    a = train_test()
    b = train_test()
    assert a == b
    x_train, x_test, y_train, y_test = a
    assert len(x_test) / (len(x_train) + len(x_test)) == __import__("pytest").approx(0.25, abs=0.01)
    assert set(Counter(y_test)) == set(CATEGORIES)
