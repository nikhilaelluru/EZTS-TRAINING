# Scenario: Alex, an intrepid treasure hunter, is navigating through a labyrinth with seven checkpoints.
# At each checkpoint, there are multiple gates, each marked with a number representing the potential clues or challenges it holds. 
# Only one gate at each checkpoint leads to the next, and the correct gate is determined by an equilibrium condition: the sum of all 
# integers (clues/challenges) on its left must be equal to the sum of allintegers on its right. If no such gate exists, the middle gate 
# is deemed correct.

#  Objective: Develop a program that assists Alex in identifying the correct gates at each checkpoint to reach the final destination. 
#  The program should accept an array A of N integers, where each integer represents the number of clues or challenges associated with 
#  a gate and output the index of the equilibrium gate.
 
# Requirements: The program must process an array of integers as input for each checkpoint.
                # The output must clearly indicate the index of equilibrium gate.
                # If no equilibrium gate exists, the program should return the midpoint state.
''' 
def gate(lst):
    flag=False
    for i in range(len(lst)):
        ls=sum(lst[0:1])
        rs=sum(lst[i:])
        if ls==rs:
            flag=True
            eq_gate=i
            break
    if flag:
        return(eq_gate)
    else:
        if len(lst)%2==0:
            mid=len(lst)//2-1
        else:
            mid=len(lst)//2
        return(mid)
    
i_p=[
    [2,2,1,2,1],
    [4,2,3,1,2,1,2,3],
    [1,1,1,1,1],
    [3,0,3],
    [1,2,1,1,2,1],
    [1,1,1,2,1],
    [5,2,1,3,1,2,5] 
    ]

result={}
for i in i_p:
    st="checkpoint"+str(i_p.index(i)+1)
    result[st]=gate(i)
print(result)
'''