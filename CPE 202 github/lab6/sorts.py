import random
import time


def selection_sort(list):
    # sort the list
    # count the number of comparisons
    # nested for loops to deal with the sorted and unsorted part of the list
    compare = 0
    for i in range(len(list)):
        min_index = i
        for j in range(i + 1, len(list)):
            compare += 1
            if list[min_index] > list[j]:
                min_index = j
        temp = list[i]
        list[i] = list[min_index]
        list[min_index] = temp
    return compare


def insertion_sort(list):
    # sort the list
    # count the number of comparisons
    compare = 0
    for i in range(1, len(list)):
        store = list[i]
        counter = i - 1
        compare += 1
        while counter >= 0 and store < list[counter]:
            list[counter + 1] = list[counter]
            counter -= 1
            compare += 1
        if counter < 0:
            compare -= 1
        list[counter + 1] = store
    return compare


def main():
    # Code coverage NOT required for main
    # Give the random number generator a seed, so the same sequence of 
    # random numbers is generated at each run
    random.seed(1234)

    # Generate 5000 random numbers from 0 to 999,999
    randoms = random.sample(range(1000000), 5000)
    start_time = time.time()
    comps = selection_sort(randoms)
    stop_time = time.time()
    print(comps, stop_time - start_time)


if __name__ == '__main__':
    main()