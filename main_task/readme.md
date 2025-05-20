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
 Experiment for a small data set:
Duration of sorting by function:
- SORTED - 1.9999220967292786e-05
- INSERTION SORT - 0.0004279995337128639
- MERGE SORT - 0.0005620000883936882
The current experiment shows that:
 - INSERTION SORT is 21.400810282201732 times slower than SORTED
 - MERGE SORT is 28.101099003446027 times slower than SORTED
```

---

## 🔬 Experiment for the average data set:

```
 Experiment for the average data set:
Duration of sorting by function:
- SORTED - 0.00026009976863861084
- INSERTION SORT - 0.08158039953559637
- MERGE SORT - 0.003852599300444126
The current experiment shows that:
 - INSERTION SORT is 313.6504117731309 times slower than SORTED
 - MERGE SORT is 14.81200587224291 times slower than SORTED
```

---

## 🔬 Experiment for a large data set:

```
 Experiment for a large data set:
Duration of sorting by function:
- SORTED - 0.003258800134062767
- INSERTION SORT - 6.892750999890268
- MERGE SORT - 0.054267299361526966
The current experiment shows that:
 - INSERTION SORT is 2115.119282046006 times slower than SORTED
 - MERGE SORT is 16.652539931582602 times slower than SORTED
```

---

## ✅ Conclusion

Built-in `sorted()` is extremely efficient, especially on large datasets, compared to custom sorting implementations.
