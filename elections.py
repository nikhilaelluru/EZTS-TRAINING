#ELECTIONS - to count the number of votes for 6 candidates and display the winner with
#            maximum number of votes.

list=[1,2,2,3,5,6,4,3,3,3]
def maxvote(list):
    c=0
    n=list[0]
    
    for i in list:
        cur=list.count(i)
        if(cur>c):
            c=cur
            n=i
    return n
print(maxvote(list))