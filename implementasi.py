# Rania Maharani Narendra
# 2106650222
# Kode Asdos 1

import math, time, tracemalloc


def main():
    # read dataset
    small_sorted = read_file("small_sorted.txt")
    med_sorted = read_file("med_sorted.txt")
    large_sorted = read_file("large_sorted.txt")

    small_random = read_file("small_random.txt")
    med_random = read_file("med_random.txt")
    large_random = read_file("large_random.txt")

    small_reversed = read_file("small_reversed.txt")
    med_reversed = read_file("med_reversed.txt")
    large_reversed = read_file("large_reversed.txt")

    
    # # sorted in BCIS vs counting sort
    print("=================Small Sorted==============")
    result_small_sorted = small_sorted[:]
    tracemalloc.start()
    start = time.time()
    BCIS(result_small_sorted)
    end = time.time()
    memory_stats = tracemalloc.get_traced_memory()
    print("time executed for BCIS: " + str((end-start)* 1000))
    print(f"memory usage: {memory_stats[1] / 10**6} MB")

    k = max(small_sorted)
    result_small_sorted_2 = [0] * len(small_sorted)
    tracemalloc.start()
    start = time.time()
    counting_sort(small_sorted, result_small_sorted_2, k)
    end = time.time()
    memory_stats = tracemalloc.get_traced_memory()
    print("time executed for Counting Sort: " + str((end-start)* 1000))
    print(f"memory usage: {memory_stats[1] / 10**6} MB")

    print("=================Small Random==============")
    result_small_random = small_random[:]
    tracemalloc.start()
    start = time.time()
    BCIS(result_small_random)
    end = time.time()
    memory_stats = tracemalloc.get_traced_memory()
    print("time executed for BCIS: " + str((end-start)* 1000))
    print(f"memory usage: {memory_stats[1] / 10**6} MB")

    k = max(small_random)
    result_small_random_2 = [0] * len(small_random)
    tracemalloc.start()
    start = time.time()
    counting_sort(small_random, result_small_random_2, k)
    end = time.time()
    memory_stats = tracemalloc.get_traced_memory()
    print("time executed for Counting Sort: " + str((end-start)* 1000))
    print(f"memory usage: {memory_stats[1] / 10**6} MB")

    print("=================Small Reversed==============")
    result_small_reversed = small_reversed[:]
    tracemalloc.start()
    start = time.time()
    BCIS(result_small_reversed)
    end = time.time()
    memory_stats = tracemalloc.get_traced_memory()
    print("time executed for BCIS: " + str((end-start)* 1000))
    print(f"memory usage: {memory_stats[1] / 10**6} MB")

    k = max(small_reversed)
    result_small_reversed_2 = [0] * len(small_reversed)
    tracemalloc.start()
    start = time.time()
    counting_sort(small_reversed, result_small_reversed_2, k)
    end = time.time()
    memory_stats = tracemalloc.get_traced_memory()
    print("time executed for Counting Sort: " + str((end-start)* 1000))
    print(f"memory usage: {memory_stats[1] / 10**6} MB")

    print("=================Medium Sorted==============")
    result_med_sorted = med_sorted[:]
    tracemalloc.start()
    start = time.time()
    BCIS(result_med_sorted)
    end = time.time()
    memory_stats = tracemalloc.get_traced_memory()
    print("time executed for BCIS: " + str((end-start)* 1000))
    print(f"memory usage: {memory_stats[1] / 10**6} MB")

    k = max(med_sorted)
    result_med_sorted_2 = [0] * len(med_sorted)
    tracemalloc.start()
    start = time.time()
    counting_sort(med_sorted, result_med_sorted_2, k)
    end = time.time()
    memory_stats = tracemalloc.get_traced_memory()
    print("time executed for Counting Sort: " + str((end-start)* 1000))
    print(f"memory usage: {memory_stats[1] / 10**6} MB")

    print("=================Medium Random==============")
    result_med_random = med_random[:]
    tracemalloc.start()
    start = time.time()
    BCIS(result_med_random)
    end = time.time()
    memory_stats = tracemalloc.get_traced_memory()
    print("time executed for BCIS: " + str((end-start)* 1000))
    print(f"memory usage: {memory_stats[1] / 10**6} MB")

    k = max(med_random)
    result_med_random_2 = [0] * len(med_random)
    tracemalloc.start()
    start = time.time()
    counting_sort(med_random, result_med_random_2, k)
    end = time.time()
    memory_stats = tracemalloc.get_traced_memory()
    print("time executed for Counting Sort: " + str((end-start)* 1000))
    print(f"memory usage: {memory_stats[1] / 10**6} MB")

    print("=================Medium Reversed==============")
    result_med_reversed = med_reversed[:]
    tracemalloc.start()
    start = time.time()
    BCIS(result_med_reversed)
    end = time.time()
    memory_stats = tracemalloc.get_traced_memory()
    print("time executed for BCIS: " + str((end-start)* 1000))
    print(f"memory usage: {memory_stats[1] / 10**6} MB")

    k = max(med_reversed)
    result_med_reversed_2 = [0] * len(med_reversed)
    tracemalloc.start()
    start = time.time()
    counting_sort(med_reversed, result_med_reversed_2, k)
    end = time.time()
    memory_stats = tracemalloc.get_traced_memory()
    print("time executed for Counting Sort: " + str((end-start)* 1000))
    print(f"memory usage: {memory_stats[1] / 10**6} MB")


    print("=================Large Sorted==============")
    result_large_sorted = large_sorted[:]
    tracemalloc.start()
    start = time.time()
    BCIS(result_large_sorted)
    end = time.time()
    memory_stats = tracemalloc.get_traced_memory()
    print("time executed for BCIS: " + str((end-start)* 1000))
    print(f"memory usage: {memory_stats[1] / 10**6} MB")

    k = max(large_sorted)
    result_large_sorted_2 = [0] * len(large_sorted)
    tracemalloc.start()
    start = time.time()
    counting_sort(large_sorted, result_large_sorted_2, k)
    end = time.time()
    memory_stats = tracemalloc.get_traced_memory()
    print("time executed for Counting Sort: " + str((end-start)* 1000))
    print(f"memory usage: {memory_stats[1] / 10**6} MB")

    print("=================Large Random==============")
    result_large_random = large_random[:]
    tracemalloc.start()
    start = time.time()
    BCIS(result_large_random)
    end = time.time()
    memory_stats = tracemalloc.get_traced_memory()
    print("time executed for BCIS: " + str((end-start)* 1000))
    print(f"memory usage: {memory_stats[1] / 10**6} MB")

    k = max(large_random)
    result_large_random_2 = [0] * len(large_random)
    tracemalloc.start()
    start = time.time()
    counting_sort(large_random, result_large_random_2, k)
    end = time.time()
    memory_stats = tracemalloc.get_traced_memory()
    print("time executed for Counting Sort: " + str((end-start)* 1000))
    print(f"memory usage: {memory_stats[1] / 10**6} MB")

    print("=================Large Reversed==============")
    result_large_reversed= large_reversed[:]
    tracemalloc.start()
    start = time.time()
    BCIS(result_large_reversed)
    end = time.time()
    memory_stats = tracemalloc.get_traced_memory()
    print("time executed for BCIS: " + str((end-start)* 1000))
    print(f"memory usage: {memory_stats[1] / 10**6} MB")

    k = max(large_reversed)
    result_large_reversed_2 = [0] * len(large_reversed)
    tracemalloc.start()
    start = time.time()
    counting_sort(large_reversed, result_large_reversed_2, k)
    end = time.time()
    memory_stats = tracemalloc.get_traced_memory()
    print("time executed for Counting Sort: " + str((end-start)* 1000))
    print(f"memory usage: {memory_stats[1] / 10**6} MB")

def read_file(filename):
    data = []
    with open(filename, 'r') as file:
        for line in file:
            data.append(int(line.strip()))

    return data

def BCIS(A):
    SL = 0
    SR = len(A)-1
    while SL < SR:
        # for performance enhancement
        swap(A, SR, SL + math.ceil((SR-SL)/2))
        if A[SL] == A[SR]:
            if is_equal(A, SL, SR) == -1:
                break
        
        if A[SL] > A[SR]:
            swap(A, SL, SR)

        # for performance enhancement
        if (SR-SL) >= 100:
            for i in range(SL+1, int((SR-SL)**0.5)+1):
                if A[SR] < A[i]:
                    swap(A, SR, i)
                elif A[SL] > A[i]:
                    swap(A, SL, i)
        
        i = SL + 1
        
        LC = A[SL]
        RC = A[SR]

        while i < SR:
            current = A[i]
            if current >= RC:
                A[i] = A[SR-1]
                insert_right(A, current, SR, len(A)-1)
                SR -= 1
            elif current <= LC:
                A[i] = A[SL+1]
                insert_left(A, current, SL, 0)
                SL += 1
                i += 1
            else:
                i += 1
        SL += 1
        SR -= 1

def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp

def is_equal(a, SL, SR):
    for k in range(SL+1, SR):
        if a[k] != a[SL]:
            swap(a, k, SL)
            return k
    else:
        return -1

def insert_right(A, current, SR, right):
    j = SR

    while (j <= right) and (current > A[j]):
        A[j-1] = A[j]
        j = j+1
    
    A[j-1] = current
     
def insert_left(A, current, SL, left):
    j = SL

    while j >= left and current < A[j]:
        A[j+1] = A[j]
        j = j-1
    
    A[j+1] = current

def counting_sort(A, B, k):
    C = []
    for i in range(k+1):
        C.append(0)

    # frequency of each num
    for j in range(len(A)):
        C[A[j]] += 1
    
    # cumulative frequency
    for i in range(1, k+1):
        C[i] += C[i-1]

    for j in range(len(A)-1, -1, -1):
        B[C[A[j]] - 1] = A[j]
        C[A[j]] -= 1

if __name__ == "__main__":
    main()

