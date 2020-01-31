import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

tree = BinarySearchTree(names_2.pop())
for name in names_2:
    tree.insert(name)

duplicates = []
for name_1 in names_1:
    if tree.contains(name_1):
        # Old version ran at O(n^2) Time
        # BST should reduce that to O(n log n)
        #     for name_2 in names_2:
        #         if name_1 == name_2:
        duplicates.append(name_1)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?
