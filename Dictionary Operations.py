student = { 'Alice': 90, 'Bob': 85, 'Charlie': 88, 'David': 92, 'Eve': 95}
print(student.keys())
sum = sum(student.values())
sum = sum/len(student)
print("Average score is:", sum)