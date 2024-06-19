# Background: A group of friends embarks on a picnic and decides to engage in a friendly
#  competition during their journey. The game they choose involves each participant stating
#  a sentence about themselves. The objective is to have the sentence with the highest frequency
#  of any single vowel. In the event of a tie, the winner is determined by the alphabetical
#  precedence of the most frequent vowel.

# Objective: Develop a program that assists in determining the winner of the game by analysing 
# the sentences provided by each player. The program should accept a string input, which represents
#  the sentence spoken by a player, and output the most frequent vowel(s) in that sentence. 
# If multiple vowels tie for highest frequency, all such vowels should be printed in alphabetical
#  order.

# Requirements:
# •	The program must handle multiple sentences as input, one for each player.
# •	The output must clearly indicate the most frequent vowel(s) for each input sentence.
# •	In case of ties, vowels must be sorted alphabetically and displayed accordingly.

# Test cases:
# Input	Output
# [
#     ["Alex", "I enjoy hiking in the mountains."],
#     ["Sam", "A lovely sunny day at the beach."],
#     ["Jamie", "Reading a book is my favorite pastime."],
#     ["Taylor", "I love playing video games on weekends."],
#     ["Chris", "Exploring new cities is exciting and fun."]
# ]	{
# 'Alex': ['I'], 
# 'Sam': ['A'], 
# 'Jamie': ['A', 'I'], 
# 'Taylor': ['E'], 
# 'Chris': ['I']
# }


def count_vowels(st):   
    dic={'A':0,'E':0,'I':0,'O':0,'U':0}
    for i in st: 
        if i=='a' or i=='A':
            dic['A']+=1  
        elif i=='e' or i=='E':
            dic['E']+=1
        elif i=='i' or i=='I':
            dic['I']+=1 
        elif i=='o' or i=='O':
            dic['O']+=1  
        elif i=='u' or i=='U':
            dic['U']+=1 
    x=max(dic.values())
    result=[]
    for i,j in dic.items():
        if j==x:
            result.append(i)
    return result

i_p=[
    ["Alex","I enjoy hicking in the mountains"],
    ["Sam","A lovely sunny day at the beach"],
    ["Jamie","Reading a book is my favorite pastime"],
    ["Taylor","I love playing video games on weekends"],
    ["Chris","Exploring new cities is exciting and fun"]

]
o_p={}
for i in i_p:
    o_p[i[0]]=count_vowels(i[1])
print(o_p)
