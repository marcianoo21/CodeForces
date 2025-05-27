n, m = map(int, input().split())

counter = 0
x = 1
y = 4
iterations = 0

while x <= n:
    iterations += 1
    if y <= m:
        counter += 1
        y += 5
    else:
        y -= (iterations - 1)*5 +1
        if y < 1:
            y += 5
        x += 1
        iterations = 0
       
print(counter)

### 2nd version(faster)
def count_pairs(n, m):
    cnt_n = [0] * 5
    cnt_m = [0] * 5

    for i in range(5):
        cnt_n[i] = n // 5 + (1 if i != 0 and i <= n % 5 else 0)
        cnt_m[i] = m // 5 + (1 if i != 0 and i <= m % 5 else 0)

    result = 0
    for i in range(5):
        result += cnt_n[i] * cnt_m[(5 - i) % 5]

    return result

n, m = map(int, input().split())
print(count_pairs(n, m))
