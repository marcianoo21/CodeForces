n, m = map(int, input().split())
student_answers = [input() for _ in range(n)]
correct_answers = list(map(int, input().split()))

max_score = 0

for j in range(m):
    answer_counts = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0}
    
    for i in range(n):
        answer = student_answers[i][j]
        answer_counts[answer] += 1
    
    most_frequent_answer = max(answer_counts, key=answer_counts.get)
    
    max_score += correct_answers[j] * answer_counts[most_frequent_answer]

print(max_score)

