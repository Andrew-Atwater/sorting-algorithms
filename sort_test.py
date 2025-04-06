import random
import time
import selection
import quicksort
import countsort

def run_verification():
    print("VERIFICATION")
    for module in [selection, quicksort, countsort]:
        data = [random.randint(1, 1000) for _ in range(1000)]
        sorted_data = module.sort(data.copy())
        is_sorted = module.vf(data, sorted_data)
        print(f"{module.__name__.capitalize()}: {is_sorted} {len(data) == len(sorted_data)}")

def time_sort(sort_func, arr):
    start = time.perf_counter_ns()
    sort_func(arr.copy())
    end = time.perf_counter_ns()
    return end - start

def benchmark():
    sizes = [100, 10_000, 1_000_000]
    results = {
        "selection": {size: [] for size in sizes},
        "quicksort": {size: [] for size in sizes},
        "countsort": {size: [] for size in sizes},
    }

    for _ in range(100):
        for size in sizes:
            base_list = [random.randint(1, 1000) for _ in range(size)]

            results["selection"][size].append(time_sort(selection.sort, base_list))
            results["quicksort"][size].append(time_sort(quicksort.sort, base_list))
            results["countsort"][size].append(time_sort(countsort.sort, base_list))

    def print_stats(title, stat_func):
        print(f"\n{title.upper()} SORTING TIME")
        print("Algorithm   100        10K         1ML")
        for algo in results:
            stats = [stat_func(results[algo][size]) for size in sizes]
            print(f"{algo.capitalize():<11} {stats[0]:<10} {stats[1]:<10} {stats[2]:<10}")

    print_stats("MIN", min)
    print_stats("MAX", max)
    print_stats("AVG", lambda x: sum(x) // len(x))

if __name__ == "__main__":
    print("running...")
    run_verification()
    benchmark()


