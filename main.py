from pyfiglet import Figlet
from termcolor import colored,cprint
import time
import sys

def mergeSort(numbers):
    if len(numbers) > 1:
        mid = len(numbers) // 2
        left = numbers[:mid]
        right = numbers[mid:]

        mergeSort(left)
        mergeSort(right)

        i = 0
        j = 0
        
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
              numbers[k] = left[i]
              i += 1
            else:
                numbers[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            numbers[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            numbers[k]=right[j]
            j += 1
            k += 1

def bubbleSort(numbers):
	numberofitems = len(numbers) - 1


	for x in range(numberofitems):
		for k in range(numberofitems):
			element1 = numbers[k]
			element2 = numbers[k+1]
			if element1 > element2:
				numbers[k] , numbers[k+1] = numbers[k+1] , numbers[k]


f = Figlet(font='standard')
f2 = Figlet(font = "small")
print(colored(f.renderText('NUMBER  SORTER'), 'red'))
print(colored(f2.renderText("Merge OR Bubble"), 'red'))


numbers = []
 
n = int(input("Enter number of numbers to be sorted : "))

for i in range(0, n):
    ele = int(input("Enter one of the numbers: "))
    numbers.append(ele)

chosen = False

while chosen == False:
	sortType = input("What sort type do you want? (0) Bubble  (1) Merge: ")
	if sortType == "0":
		bubbleSort(numbers)
		print("Bubble Selected")
	
		for i in range (n + 2):
			sys.stdout.write('\rLoading |')
			time.sleep(0.2)
			sys.stdout.write('\rLoading /')
			time.sleep(0.2)
			sys.stdout.write('\rLoading -')
			time.sleep(0.2)
			sys.stdout.write('\rLoading \\')
			time.sleep(0.2)
		sys.stdout.write('\rDone')
		print("\r~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
		print(colored(f2.renderText("Output: "), 'green'))
		chosen = True
	elif sortType == "1":
		mergeSort(numbers)
		print("Merge Selected")
	
		for i in range (n + 2):
			sys.stdout.write('\rLoading |')
			time.sleep(0.2)
			sys.stdout.write('\rLoading /')
			time.sleep(0.2)
			sys.stdout.write('\rLoading -')
			time.sleep(0.2)
			sys.stdout.write('\rLoading \\')
			time.sleep(0.2)
		sys.stdout.write('\rDone!     ')
		print("/r~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
		print(colored(f.renderText("Output: "), 'green'))	
		chosen = True
	else:
		print("Incorrect input please type 0 or 1")

print(numbers)