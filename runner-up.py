n = int(input())
arr = map(int, input().split())
    
    
score = []

for i in arr:
    score.append(i)
    score.sort()
    
if score.count(max(score)) == 1:
    print(score[n-2])
    
elif score.count(max(score)) > 1 :
    set1 = set(score)
    set1.remove(max(set1))
    print(max(set1))
