n = int(input())

drinks = ["ABSINTH", "BEER", "BRANDY", "CHAMPAGNE", "GIN", "RUM", "SAKE", "TEQUILA", "VODKA", "WHISKEY", "WINE"]
checks = 0
for _ in range(n):
    client = input()
    
    if client.isdigit() and int(client) < 18:
        checks += 1
    if client in drinks:
        checks += 1
        
print(checks)         
