#!/usr/bin/env python
#Case description:this progress selects numbers and an arithmetic function randomly, display the question to an user and verify the results given by the user.Reslts are given after 3 times wrong, the progress will wait until the user to enter a correct answer.

from operator import add, sub
from random import randint, choice

ops = {'+': add, '-': sub} #a dictionary contains the operators and their associated set of functions
MAXTRIES = 2 #the integer variable show how many times the user have opportunities to try to answer

def doprob():
 op = choice('+-') #it is used to obtain a sequence and returns the random elements
 nums = [randint(1,10) for i in range(2)] #using list comprehension is more easy to expand and upgrade
 nums.sort(reverse=True) #sort numbers to avoid negative
 ans = ops[op](*nums) #store the operation result like apply(),*tuple
 pr = '%d %s %d = ' % (nums[0], op, nums[1])
 oops = 0 #count times of user's answers
 while True:
  try:
   if int(raw_input(pr)) == ans: #right answer
    print 'correct'
    break
   if oops == MAXTRIES: #answer more than maxtries
    print 'answer\n%s%d'%(pr, ans)
   else:
    print 'incorrect... try again'
    oops += 1
  except (KeyboardInterrupt, EOFError, ValueError): #invalid input
   print 'invalid input... try again'

def main():
 while True:
  doprob()
  try:
   opt = raw_input('Again? [y]').lower() # give users a choice whether to continue the answer
   if opt and opt[0] == 'n':
    break
  except (KeyboardInterrupt, EOFError):
   break

if __name__ == '__main__':
 main()
