#!/bin/python3

import math
import os
import random
import re
import sys
import itertools

#
# Complete the 'biggerIsGreater' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING w as parameter.
#

def biggerIsGreater(w):
    w = list(w)
    n = len(w)

    i = n - 2
    while i >= 0 and w[i] >= w[i + 1]:
        i -= 1

    if i == -1:
        return "no answer" 
    j = n - 1
    while w[j] <= w[i]:
        j -= 1

    w[i], w[j] = w[j], w[i]

    w[i + 1:] = reversed(w[i + 1:])

    return ''.join(w)
    
    
    
    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()


'''Great question! The reason we start from the **second last character** (`len(s) - 2`) is because we're trying to find the **first pair from the end** where the characters **increase** — this tells us **where we can make a change** to get a lexicographically **greater** string.

---

### 🔍 Why `len(s) - 2` and not `len(s) - 1`?

Let's break it down:

#### Given a string: `"abdc"`

Positions:

```
Index:    0   1   2   3  
Chars:   'a' 'b' 'd' 'c'
```

If we start at the **last character**, index 3 (`'c'`), we **can’t compare it to anything to the right** — it's the end.

But we need to compare each character with the one **after it**, like this:

```python
while s[i] >= s[i + 1]:
    i -= 1
```

So we must start from the **second last character** (`i = len(s) - 2`) because we’re checking:

```python
s[i] >= s[i + 1]
```

If we started from the last character, `s[i + 1]` would be out of bounds (index error).

---

### 🔁 What Are We Doing, Conceptually?

We're trying to find the **"pivot"** — the first character from the end where:

```plaintext
s[i] < s[i + 1]
```

This is the **last increasing point** from right to left. It tells us:

* **Where we can make a change** that will produce a greater word.
* Everything **after** that point is in **descending order**, so it's the highest permutation of that suffix.

By finding the pivot and then swapping it with the next greater element, we can rearrange the suffix into the **smallest possible order** — giving us the **next lexicographically smallest greater word**.

---

### 🔁 Visual Example:

String: `"dkhc"`
Indices:

```
0   1   2   3  
d   k   h   c
```

We go from the **second last** character:

* i = 2 → `'h' >= 'c'` → true → i = 1
* i = 1 → `'k' >= 'h'` → true → i = 0
* i = 0 → `'d' < 'k'` → stop!

Found pivot at index 0: `'d'`

That’s where we can make a change to go from `"dkhc"` to the **next word** → `"hcdk"`

---

Let me know if you'd like to visualize this with a diagram or animation-style breakdown!
'''