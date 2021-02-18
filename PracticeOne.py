import math
import sys
import datetime
import calendar
import bs4
import requests
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import random
import math
'''
print(sys.version_info)
print(datetime.datetime.now())

'''
#
'''radius = float(input("Enter Radius"))
print(math.pi)
area = float(math.pi) * float(math.pow(radius,2))
print("Area ",area)'''

#
'''
firstName = input("Enter first name")
lastName = input("Enter last name")
print(lastName + " "+ firstName)'''

#accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
'''userData = input("Enter comma separated values")
myList = userData.split(",")
print("Your list is: ",myList)
myTuple = tuple(myList)
print("my tuple is: ",myTuple)'''

#
'''
fileName = input("Enter file name")
myList = fileName.split(".")
print("Extension is : "+myList[1])'''

#print the calendar of a given month and year.
#print(calendar.month(2020,8))

#remove and print every third number from a list of numbers until the list becomes empty.
'''
my_list =[10,20,30,40,50,60,70,80,90]

while len(my_list)>0:
    for i in my_list[::3]:
        print(i)
        my_list.remove(i)


print(my_list)'''

#program to get the top stories from Google news
'''
page = requests.get("https://news.google.com/topstories?tab=rn&hl=en-IN&gl=IN&ceid=IN:en")
print(page.status_code)


print("--------------------")

soup = bs4.BeautifulSoup(page.content, 'html.parser')

headlines = list(soup.find_all('a',class_='DY5T1d'))

for head in headlines:
    print(head.get_text())

'''

#create all possible permutations from a given collection of distinct numbers.
'''
def permute(nums):
  result_perms = [[]]
  for n in nums:
    print("n = ",n)
    new_perms = []
    for perm in result_perms:
      print("perm= ",perm)
      for i in range(len(perm)+1):
        print("i= ",i)
        new_perms.append(perm[:i] + [n] + perm[i:])
        result_perms = new_perms
        print("result_perms = ",result_perms)
  return result_perms

my_nums = [1,2,3]
print("Original Cofllection: ",my_nums)
print("Collection of distinct numbers:\n",permute(my_nums))

'''

#  calculate number of days between two dates.
'''
date1 = datetime.date(2014,2,2)
date2 = datetime.date(2015,2,2)

print(date1.strftime(date1,))
print(date2 - date1)'''

# To get LCM of number
'''
def get_lcm(a,b):
    if a>b:
        a=b
        y=a
    if a%b == 0:
        return a
    for i in range(2,a):
        temp = a*i
        print(temp)
        if temp%b == 0:
            return temp

print(get_lcm(17,15))
'''

# to find a distinct pair of numbers whose product is odd from a sequence of integer values
number_list = [1,2,3,4,6,7,8,9]
for i in range(len(number_list)-1):
    for j in range(0,i):
        print("I -- ",i)
        print(number_list[i], number_list[j+1])
        if (number_list[i]*number_list[j+1]) % 2 != 0:
            print("Product is ODD : ",number_list[i], number_list[j+1],(number_list[i]*number_list[j+1]))

