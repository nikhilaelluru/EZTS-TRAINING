# Liam works as a data analyst for a company that stores massive amounts of numerical data. He has been 
# tasked with determining how many commas are used when writing numbers in the range of to N (inclusive) 
# in a specific format In this format, if numbers are more than four digits long, commas are used to 
# separate the numbers into groups of three, starting from the right for the representation of the 
# number. Your task is to help Liam find and return an integer value, representing the total number of 
# commas used when writing each integer in the range of 1 to N. 

# Input Specification: Input: An integer value N. representing the number range.
# Output Specification: Return an integer value, representing total number of commas used when 
# writing each integer in the range of 1 to N.

# Sample Input: 5000 
# Sample Output: 4001

# c=0
# num=input()
# for i in num:
#     if i==",":
#         c+=1
# print(c)
# n=int(input())
# i=0
# while n>100:
#     r=n%1000
#     i=i+1
#     n=n//1000
# print(i)
#------------------------------------------------------------------------------------------
# n=int(input())
# c=1000
# comma=1
# res=0
# while c<=n:
#     m=c*1000
#     num=min(n-c+1,m-c)
#     res=num*comma
#     c=m
#     comma+=1
# print(res)
#------------------------------------------------------------------------------------------

arr=list(map(int,input().split()))
min=float('inf')
res=float('inf')
for i in arr:
    if i>0 and i<min:
        min=i
for j in range(min,len(arr)+1):
    if j>0 and j not in arr:
        res=j
        break
print(res)
