"""
Chained Comparison Operators
"""

print(1 < 2 < 3)
# Output: True

print(1 < 2 and 2 < 3)
# Output: True

print(1 < 3 > 2)
# Output: True

print(1 < 3 and 3 > 2)
# Output: True

print(1 == 2 or 2 > 1)
# Output: True

print(1 == 1 or 100 == 1)
# Output: True