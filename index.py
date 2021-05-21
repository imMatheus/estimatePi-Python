import random 

def estimatePi(n):
    num_in = 0
    for _ in range(n):
        x= random.uniform(0,1)
        y= random.uniform(0,1)
        distance = x**2+y**2
        if distance <= 1:
            num_in +=1
    return 4 *num_in/n

print(estimatePi(100000))