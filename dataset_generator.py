import random

def main():
    # generate dataset: sorted
    small_sorted = []
    sorted_data_generator(small_sorted, 500)
    write_array_to_file("small_sorted.txt", small_sorted)

    med_sorted = []
    sorted_data_generator(med_sorted, 5000)
    write_array_to_file("med_sorted.txt", med_sorted)

    large_sorted = []
    sorted_data_generator(large_sorted, 50000)
    write_array_to_file("large_sorted.txt", large_sorted)

    # generate dataset: reversed
    small_reversed = small_sorted.copy()
    small_reversed.reverse()
    write_array_to_file("small_reversed.txt", small_reversed)

    med_reversed = med_sorted.copy()
    med_reversed.reverse()
    write_array_to_file("med_reversed.txt", med_reversed)

    large_reversed = large_sorted.copy()
    large_reversed.reverse()
    write_array_to_file("large_reversed.txt", large_reversed)

    # generate dataset: random
    small_random = small_sorted.copy()
    random.shuffle(small_random)
    write_array_to_file("small_random.txt", small_random)

    med_random = med_sorted.copy()
    random.shuffle(med_random)
    write_array_to_file("med_random.txt", med_random)

    large_random = large_sorted.copy()
    random.shuffle(large_random)
    write_array_to_file("large_random.txt", large_random)

def write_array_to_file(filename, data):
    with open(filename, 'w') as file:
        for item in data:  
            file.write(str(item) + '\n')    

def sorted_data_generator(a, size):
    for i in range(size):
        a.append(i)

if __name__ == "__main__":
    main()
