def main():
    t = int(input())
    
    for _ in range(t):
        n, k = map(int, input().split())
        x = list(map(int, input().split()))
        x.sort(reverse=True)
        
        cnt = 0
        sum_val = 0
        
        while cnt < len(x) and sum_val + n - x[cnt] < n:
            sum_val += n - x[cnt]
            cnt += 1
        
        print(cnt)