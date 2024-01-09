from pyfiglet import Figlet
from termcolor import colored
import time
import sys


def mergeSort(numberList):
    if len(numberList) > 1:
        mid = len(numberList) // 2
        left = numberList[:mid]
        right = numberList[mid:]

        mergeSort(left)
        mergeSort(right)

        a = 0
        j = 0

        k = 0

        while a < len(left) and j < len(right):
            if left[a] <= right[j]:
                numberList[k] = left[a]
                a += 1
            else:
                numberList[k] = right[j]
                j += 1
            k += 1

        while a < len(left):
            numberList[k] = left[a]
            a += 1
            k += 1

        while j < len(right):
            numberList[k] = right[j]
            j += 1
            k += 1


def bubbleSort(numberList):
    numberofitems = len(numberList) - 1

    for x in range(numberofitems):
        for k in range(numberofitems):
            element1 = numberList[k]
            element2 = numberList[k + 1]
            if element1 > element2:
                numberList[k], numberList[k + 1] = numberList[k + 1], numberList[k]


def insertionSort(numberList):
    length = len(numberList)
    for count in range(1, length):
        current = numberList[count]
        point = count
        while point > 0 and numberList[point - 1] > current:
            numberList[point] = numberList[point - 1]
            point -= 1
        numberList[point] = current


f = Figlet(font='standard')
f2 = Figlet(font="small")
print(colored(f.renderText('NUMBER  SORTER'), 'red'))
# print(colored(f2.renderText("Merge OR Bubble"), 'red'))

numbers = []

n = int(input("Enter number of numbers to be sorted : "))

for i in range(0, n):
    ele = int(input("Enter one of the numbers: "))
    numbers.append(ele)

chosen = False

while not chosen:
    ahead = False
    sortType = input("What sort type do you want? (0) Bubble (1) Merge (2) Insertion: ")
    if sortType == "0":
        ahead = True
        bubbleSort(numbers)
        print("Bubble Selected")
    elif sortType == "1":
        ahead = True
        mergeSort(numbers)
        print("Merge Selected")
    elif sortType == "2":
        ahead = True
        insertionSort(numbers)
    else:
        print("Incorrect input please type 0 or 1")
    if ahead:
        for i in range(n + 1):
            sys.stdout.write('\rLoading |')
            time.sleep(0.1)
            sys.stdout.write('\rLoading /')
            time.sleep(0.1)
            sys.stdout.write('\rLoading -')
            time.sleep(0.1)
            sys.stdout.write('\rLoading \\')
            time.sleep(0.1)
        sys.stdout.write('\rDone')
        print("\r~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(colored(f2.renderText("Output: "), 'green'))
        chosen = True

print(numbers)
