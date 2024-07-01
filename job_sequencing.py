'''
Job Sequence
jobs:       j1      j2      j3      j4      j5  
profit:     20      40      10      30      50 
Deadline:   2       1        2      3       1  

Job Sequence: j5    j1     j4
Max Profit=100      

'''

jobs={}
d=[2,1,2,3,1]
p=[20,40,10,30,50]
for i in range(len(p)):
    jobs[p[i]]=d[i]
print(jobs)

seq_size=max(d)
print(seq_size)

l=list(jobs.items())
l.sort(key=lambda x:x[1],reverse=True)

sorted_jobs={}
for i in l:
    sorted_jobs[i[0]]=i[1]
print(sorted_jobs)

job_sequence=[0]*seq_size
