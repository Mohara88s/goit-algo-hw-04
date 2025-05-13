import timeit
import random
from utilities import insertion_sort, merge_sort

def analyzing_func(not_sorted_data, sort_func, func_name):
    start_time = timeit.default_timer()
    sorted_data = sort_func(not_sorted_data)
    end_time = timeit.default_timer()
    duration = end_time - start_time
    print(f'- {func_name} - {duration}')
    return duration

def experiment(not_sorted_data_set):
    print(f'Duration of sorting by function:')
    test_sorted = analyzing_func(not_sorted_data_set, sorted, 'SORTED')
    test_insertion_sort = analyzing_func(not_sorted_data_set, insertion_sort, 'INSERTION SORT')
    test_merge_sort = analyzing_func(not_sorted_data_set, merge_sort, 'MERGE SORT')

    print('The current experiment shows that:')
    print(f' - SORTED is {test_insertion_sort/test_sorted} times faster than INSERTION SORT')
    print(f' - SORTED is {test_merge_sort/test_sorted} times faster than MERGE SORT')


def main():
    print('\n Experiment for a small data set:')
    sample_data = [random.randint(0,1000) for _ in range(100)] 
    experiment(sample_data)

    print('\n Experiment for the average data set:')
    sample_data = [random.randint(0,1000) for _ in range(1000)] 
    experiment(sample_data)

    print('\n Experiment for a large data set:')
    sample_data = [random.randint(0,1000) for _ in range(10000)] 
    experiment(sample_data)


if __name__ == "__main__":
    main()