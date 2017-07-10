import sys
import os
from pprint import pprint as pp

answerContinue ='yes'
answerExit='no'

def first_user_input():
	pp("Please enter how many times you like to loop: ")
	number = raw_input()
	if number <= 0:
		raise ValueError("You entered invalid input, must be greater than zero") 
	pp("You have entered {}".format(number))
	try:
		return int(number)
	except:
		ValueError("Cannot convert to number")
		raise
		
		
def second_user_input(numeric):
	for i in range (numeric):
		print "So user wishes to loop " + str(numeric) + " times"
		print("Please enter the cycle times for {} loops".format(numeric))
		allUserInputCycles = map(int,raw_input("enter positive numbers separated by a single space only: " ).split())
		lengthOfUserInput = len(allUserInputCycles)
		if lengthOfUserInput != numeric:
			print ValueError("You entered either less or more cycles")
			print("Do you wish to continue? Y or N: ")
			userAnswerFirst = raw_input()
			if userAnswerFirst == 'Y' or userAnswerFirst == 'y':
				continue
			else:
				print("You decided not to continue, so exiting... ")
				break
		else:
			for i in allUserInputCycles:
				if i < 0:
					raise ValueError("Negative cycle not excepted")
			return allUserInputCycles
		

	
def calc_height(age):
    if age==0:
		return 1
		print 1
    elif age%2 == 0:
		actualHeight = calc_height(age-1) + 1
		return actualHeight
    else:
		actualHeight = 2*calc_height(age-1)
		return actualHeight
		
def main():
	while True:
		firstUserInput = first_user_input()
		secondUserInput = second_user_input(firstUserInput)
		print "secondUserInput: " + str(secondUserInput)
		for iLocalValue in secondUserInput:
			finalHeight = calc_height(iLocalValue)
			print "FinalHeight of magic tree: " + str(finalHeight) + " years"
	
if __name__ == '__main__':
	main()

	

	
	
	