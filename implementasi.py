# Rania Maharani Narendra
# 2106650222
# Kode Asdos 1

import math, time, tracemalloc

def main():
    # read dataset
    small_sorted = read_file("small_sorted.txt")
    run_check("Small Sorted", small_sorted)

    small_random = read_file("small_random.txt")
    run_check("Small Random", small_random)

    small_reversed = read_file("small_reversed.txt")
    run_check("Small Reversed", small_reversed)

    med_sorted = read_file("med_sorted.txt")
    run_check("Medium Sorted", med_sorted)

    med_random = read_file("med_random.txt")
    run_check("Medium Random", med_random)

    med_reversed = read_file("med_reversed.txt")
    run_check("Medium Reversed", med_reversed)

    large_sorted = read_file("large_sorted.txt")
    run_check("Large Sorted", large_sorted)

    large_random = read_file("large_random.txt")
    run_check("Large Random", large_random)

    large_reversed = read_file("large_reversed.txt")
    run_check("Large Reversed", large_reversed)


def run_check(cond, input, ):
    print(f"================={cond}==============")
    result = input[:]
    tracemalloc.start()
    start = time.time()
    BCIS(result)
    end = time.time()
    memory_stats = tracemalloc.get_traced_memory()
    tracemalloc.stop
    print("time executed for BCIS: " + str((end-start)* 1000))
    print(f"memory usage: {memory_stats[1] / 10**6} MB")

    k = max(input)
    tracemalloc.start()
    result2 = [0] * len(input)
    start = time.time()
    counting_sort(input, result2, k)
    end = time.time()
    memory_stats = tracemalloc.get_traced_memory()
    tracemalloc.stop
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
    
