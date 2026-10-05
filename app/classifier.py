"""Optional ML model that assigns a category to a note (Lab 10).

Loaded only when MODEL_PATH points to a model file saved with joblib. Without it the app
works exactly as before and notes have no category. scikit-learn and joblib are needed only
when a model is used, so they are imported here and not at the top of the app.
"""

import os


class Classifier:
    def __init__(self, path: str) -> None:
        import joblib  # noqa: PLC0415 - only needed when a model is configured

        self.path = path
        self._model = joblib.load(path)

    def predict(self, text: str) -> str:
        return str(self._model.predict([text])[0])


def load_classifier() -> Classifier | None:
    path = os.getenv("MODEL_PATH")
    return Classifier(path) if path else None
