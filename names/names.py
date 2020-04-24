import time

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert values into BST
    def insert (self, value):
        node = self
        while True:
            if value >= node.value:
                if(node.right != None):
                    node = node.right
                else:
                    node.right = BinarySearchTree(value)
                    break
            else:
                if(node.left != None):
                    node = node.left
                else:
                    node.left = BinarySearchTree(value)
                    break

    def contains(self, target):
        node = self
        while node != None:
            if target == node.value:
                return True
            else:
                if target > node.value:
                    node = node.right
                else:
                    node = node.left
        
        return False

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

bst = BinarySearchTree(names_1[0])

for i in range(1, len(names_1)):
    bst.insert(names_1[i])

for j in names_2:
    if bst.contains(j):
        duplicates.append(j)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
