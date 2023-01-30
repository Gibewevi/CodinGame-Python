
import sys
import math

# Replaces "@" with "?"
def replaceSpecialChars(t):
    return t.replace("@","?")

# Read length of letter
l = int(input())
# Read height of letter
h = int(input())
# Read text
t = input()
# Replace special characters in text and make uppercase
t = replaceSpecialChars(t.upper())

# List to store rows
rows = []
# List to store result
result = []

# Read and store rows in list
for i in range(h):
    rows.append(input())

# Loop through t
for i in range (len(t)):
    for j in range(h):
        c = t[i]
        # Calculate order
        order = (26*l) if ord(c) < ord("A") or ord(c) > ord("Z") else (ord(c) - 65) * l
        # Get letter from rows
        letter = rows[j][order:order+l]
        # Append or add to result
        if len(result) == h:
            result[j] += letter
        else: 
            result.append(letter)

# Print result
for i in range(len(result)):
    print(result[i])

# Debug message
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
