n = int(input())  

denominations = [100, 20, 10, 5, 1]

total_bills = 0

for denom in denominations:
    num_bills = n // denom  
    total_bills += num_bills  
    n %= denom  

print(total_bills)  
