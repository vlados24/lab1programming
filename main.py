from time import time


class ComputerGame:

    def __init__(self, name="NoName", numbeOfCharacters=0, numberOfReviewsImdb=0):

        self.name = name

        self.numbeOfCharacters = int(numbeOfCharacters)

        self.numberOfReviewsImdb = int(numberOfReviewsImdb)


with open("input.txt") as file:

    films = [ComputerGame(*line.split(',')) for line in file.readlines()]


def bubble_sort(alist, comparings=0, permutations=0):
    sorted = False
    length = len(alist) - 1
    while not sorted:
        sorted = True
        for i in range(length):
            comparings += 1
            if alist[i] < alist[i+1]:
                sorted = False
                alist[i], alist[i+1] = alist[i+1], alist[i]
                permutations += 1
                comparings += 1
    return comparings, permutations


A = [s.numberOfReviewsImdb for s in films]
start_time = time()
permutations, comparings = bubble_sort(A)
print(f"Bubble sort\ntime: {time()-start_time}, \npermutations: {permutations},\ncomparings: {comparings}, \nres: {A}\n")


def merge_sort(alist, p=0, c=0):

    if len(alist)>1:

        mid = len(alist)//2

        lefthalf = alist[:mid]

        righthalf = alist[mid:]

        p, c = merge_sort(lefthalf, p, c)

        p, c = merge_sort(righthalf, p, c)

        # merging
        i=0
        j=0
        k=0

        while i < len(lefthalf) and j < len(righthalf):

            c += 1

            p += 1

            if lefthalf[i] <= righthalf[j]:

                alist[k]=lefthalf[i]

                i += 1

            else:

                alist[k]=righthalf[j]

                j += 1

            k += 1

        while i < len(lefthalf):

            p += 1

            alist[k]=lefthalf[i]

            i += 1

            k += 1

        while j < len(righthalf):

            p += 1

            alist[k]=righthalf[j]

            j += 1

            k += 1

    return p, c


A = [s.numbeOfCharacters for s in films]

start_time = time()

permutations, comparings = merge_sort(A)

print(f"Merge sort\ntime: {time()-start_time},\npermutations: {permutations},\ncomparings: {comparings},\nres: {A}.\n")