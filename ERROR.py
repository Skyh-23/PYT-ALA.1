print("Score Trend Analyzer")
tests = int(input("Enter number of tests: "))
i = 0
previous = 0
improved = 0
while i < tests:
score = int(input("Enter score: "))
if score > previous:
improved = improved + 1
print("Improved")
elif score == previous:
print("Same score")
else:
print("Declined")
previous = score
i = i + 1
print("Improvement count:", improved
if improved > tests / 2:
print("Overall improvement")
else:
print("Needs improvement")
average = previous / tests
print("Average score:", average)
