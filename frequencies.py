"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    seen=[]
    # Your code goes here
    new = ""
    
    for i in items:
        i = str(i)
        if i != new and i not in seen:
            new = i
            seen.append(i)
    print(seen)
    
    
    for i in seen:
        count = 0
        for j in items:
            j=str(j)
            if i==j:
                count +=1
        frequencies[i] = count
    return frequencies

    
frequencies(["100",100,100,100,"a","b","a","b","c"])