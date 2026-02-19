print("Score Trend Analyzer")

tests = int(input("Enter number of tests: "))

i = 0
previous = None
improved = 0
total = 0

while i < tests:
    score = int(input("Enter score: "))
    total = total + score

    if previous is not None:
        if score > previous:
            improved = improved + 1
            print("Improved")
        elif score == previous:
            print("Same score")
        else:
            print("Declined")
    else:
        print("First score entered")

    previous = score
    i = i + 1


print("Improvement count:", improved)

if improved > tests / 2:
    print("Overall improvement")
else:
    print("Needs improvement")

average = total / tests
print("Average score:", average)
