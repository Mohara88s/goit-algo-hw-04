# 📊 Sorting algorithm performance report

This experiment compares the performance of three sorting algorithms on datasets of different sizes.

## ⚙️ Sorting functions

- `sorted()` — Python built-in sorting
- `insertion_sort()` — Custom implementation
- `merge_sort()` — Custom implementation

*New datasets are created each time the program is run, so the results will be different each time.

---

## 🔬 Experiment for a small data set:

```
Duration of sorting by function:
- SORTED - 2.374732866883278e-05
- INSERTION SORT - 0.0004506162367761135
- MERGE SORT - 0.0003908323124051094
The current experiment shows that:
 - SORTED is 18.97544953624723 times faster than INSERTION SORT
 - SORTED is 16.45794850677491 times faster than MERGE SORT
```

---

## 🔬 Experiment for the average data set:

```
Duration of sorting by function:
- SORTED - 0.00012822868302464485
- INSERTION SORT - 0.06588407186791301
- MERGE SORT - 0.003267733845859766
The current experiment shows that:
 - SORTED is 513.8013610827653 times faster than INSERTION SORT
 - SORTED is 25.48364194952954 times faster than MERGE SORT
```

---

## 🔬 Experiment for a large data set:

```
Duration of sorting by function:
- SORTED - 0.001768380869179964
- INSERTION SORT - 5.235464842058718
- MERGE SORT - 0.07273605978116393
The current experiment shows that:
 - SORTED is 2960.5979872913435 times faster than INSERTION SORT
 - SORTED is 41.131444616279516 times faster than MERGE SORT
```

---

## ✅ Conclusion

Built-in `sorted()` is extremely efficient, especially on large datasets, compared to custom sorting implementations.
