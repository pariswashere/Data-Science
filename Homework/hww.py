n = int(input("Enter days: "))

formula = n * (n + 1) // 2

loop = 0
for i in range(1, n + 1):
    loop += i

nested = 0
for i in range(1, n + 1):
    for j in range(i):
        nested += 1

print("Formula:", formula)
print("Loop:", loop)
print("Nested Loop:", nested)

print("Formula Time Complexity: O(1)")
print("Loop Time Complexity: O(n)")
print("Nested Loop Time Complexity: O(n²)")

print("Most Efficient: Formula Method")