scores = [75, 82, 90, 68, 95]

print("Direct Access:", scores[2])

target = 90
for score in scores:
    if score == target:
        print("Linear Search: Found")

count = 0
for i in scores:
    for j in scores:
        count += 1

print("Pair Comparisons:", count)

print("O(1), O(n), O(n²)")