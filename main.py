import random as r

a = [] # list 

for i in range (10): # to add random numbers 
    a.append(r.randint(0,100))


print(f"Original: {a}") # before swap

i = 0
j = 0

b = a[i] # swap

"""sorting alogrithm """

# greatest to least

for n in range (len(a)-1): # this is to double check again to make sure there is 
    i = 0 # reset
    j = 0
    for x in range (len(a)-1): # goes throug the array checking
        b = a[i]
        
        if a[i] <= a[j+1]: #checks if the first number is greater than the second, if yes set the first number to the second set the seconds to the first
            a[i] = a[j+1]
            a[j+1] = b
            
        i +=1 # adds to continue on each instance
        j +=1 

print("")
print(f" Final_first {a}")


# Least to greatest
for n in range (len(a)-1): # this is to double check again to make sure there is 
    i = 0 # reset
    j = 0
    for x in range (len(a)-1): # goes throug the array checking
        b = a[i]
        
        if a[i] >= a[j+1]: #checks if the first number is greater than the second, if yes set the first number to the second set the seconds to the first
            a[i] = a[j+1]
            a[j+1] = b
            
        i +=1 # adds to continue on each instance
        j +=1 
print("")
print(f" Final_second {a}")