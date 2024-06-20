#QUICK SORT
   
# if i found smaller element than pivot then increase j by one and swap it by i
# if i found smaller element than pivot then don't do anything
'''
def divide(l,low,high):
    pivot=l[high]
    pi=high
    j=low-1
    for i in range(low,high):
        if l[i]<=pivot:
            j+=1
            l[i],l[j]=l[j],l[i]
    j+=1
    l[j],l[pi]=l[pi],l[j]
    pi=j
    return pi

def quick_sort(l,low,high):
    if low<high:
        pi=divide(l,low,high)
        print(pi,low,high)
        quick_sort(l,low,pi-1)
        quick_sort(l,pi+1,high)
    return 

if __name__=="__main__":      
    l=list(map(int,input().split()))
    low=0
    high=len(l)-1
    print(low,high)
    quick_sort(l,low,high)
    print("sorted array= ",l)
    '''