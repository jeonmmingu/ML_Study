import numpy as np

# Indexing
# ex1.Basic usage
a = np.array([1.2, -1.3, 2.2, 5.3, 3.7])
print("1.",a)
print("2.",a[0])
print("3.",a[0:3])
print("4.",a[-1])
print("5.",a[-2])
print("6.",a[0:1])

# ex2.Save index
a = np.array([1.2,-1.3,2.2,5.3,3.7])
idx = [0,3]
print(a[idx])
