k = int(input())

start = 19
step = 9

counter =  0

while counter != k:
    if sum(int(d) for d in str(start)) == 10:
        counter += 1
        if counter == k:
            print(start)
            break
     
    start += step
    

