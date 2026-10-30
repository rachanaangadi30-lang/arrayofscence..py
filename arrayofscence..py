import sys 

scores = list(map(int, sys.argv[1:]))

total = sum(scores)
average = total / len(scores) if scores else 0

print("Scores:", scores)
print("Sum:", total)
print("Average:", average)