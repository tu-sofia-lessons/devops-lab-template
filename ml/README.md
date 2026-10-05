# ML data / Данни за ML (Lab 10)

`data/notes_labelled.csv`: 536 short notes in Bulgarian and English, each with a category: `work`, `personal`, `shopping`, `idea`. About 4% of the labels are wrong on purpose and a few notes are ambiguous, because real data is never perfectly clean. / 536 кратки бележки на български и английски с категория. Около 4% от етикетите са грешни нарочно, а някои бележки са двусмислени, защото истинските данни никога не са идеално чисти.

```python
from ml.data import train_test
X_train, X_test, y_train, y_test = train_test()   # fixed, stratified split
```

The training code is yours to write in Lab 10. / Кодът за обучение го пишете вие в Упражнение 10.
