# Dictionary Program Practice:
# 1. Count Frequency:
li = [1,2,2,3,3,3,4,4,4,4]
freq = {}
for i in li:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print(freq)

# 2. Word Count In Sentence:
sentence = input("Write a sentence: ")
words = sentence.split()
count = {}

for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1
print(count)

# 3. Highest Value find:
d = {"a": 10, "b": 25, "c": 15}

max_key = None
max_value = float('-inf')   # smallest possible value

for key in d:
    if d[key] > max_value:
        max_value = d[key]
        max_key = key

print("Key with highest value:", max_key)

# 4. Sort dictionary by keys (Ascending):
d = {"b": 2, "a": 1, "c": 3}

keys = list(d.keys())

# simple sorting (bubble sort logic)
for i in range(len(keys)):
    for j in range(i+1, len(keys)):
        if keys[i] > keys[j]:
            keys[i], keys[j] = keys[j], keys[i]

for k in keys:
    print(k, ":", d[k])

# 5. Sort dictionary by values
d = {"a": 10, "b": 5, "c": 15}

items = list(d.items())

for i in range(len(items)):
    for j in range(i+1, len(items)):
        if items[i][1] > items[j][1]:
            items[i], items[j] = items[j], items[i]

for k, v in items:
    print(k, ":", v)

# 6. Sum of all values:
d = {"a": 10, "b": 20, "c": 30}

total = 0
for key in d:
    total += d[key]

print("Sum:", total)

# 7. Remove duplicate values:
d = {1:'A', 2:'B', 3:'A'}

new_d = {}
seen = []

for key in d:
    if d[key] not in seen:
        new_d[key] = d[key]
        seen.append(d[key])

print(new_d)

# 8. Invert dictionary:
d = {"a": 1, "b": 2}

inv = {}

for key in d:
    value = d[key]
    inv[value] = key

print(inv)

# 9. Second highest value:
d = {"a": 10, "b": 25, "c": 15}

first = second = float('-inf')

for key in d:
    val = d[key]
    
    if val > first:
        second = first
        first = val
    elif val > second and val != first:
        second = val

print("Second highest:", second)

# 10. Group words by length:
words = ["hi", "hello", "hey"]

result = {}

for word in words:
    length = len(word)
    
    if length not in result:
        result[length] = []
    
    result[length].append(word)

print(result)

# 11. Check two dictionaries equal:
d1 = {"a": 1, "b": 2}
d2 = {"b": 2, "a": 1}

if len(d1) != len(d2):
    print("Not Equal")
else:
    flag = True
    for key in d1:
        if key not in d2 or d1[key] != d2[key]:
            flag = False
            break
    
    print("Equal" if flag else "Not Equal")

# 12. Character frequency (without built-in):
s = "programming"

freq = {}

for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print(freq)

# 13. Top frequent element:
d = {"a": 10, "b": 25, "c": 15}

max_key = None
max_val = float('-inf')

for key in d:
    if d[key] > max_val:
        max_val = d[key]
        max_key = key

print(max_key)

# 14. Find Squares:
d = {}

for i in range(1, 4):
    d[i] = i * i

print(d)

# 15. Filter even values:
d = {"a": 10, "b": 15, "c": 20}

new_d = {}

for key in d:
    if d[key] % 2 == 0:
        new_d[key] = d[key]

print(new_d)

# 16. Common keys in two dictionaries:
d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"b": 5, "c": 6, "d": 7}

for key in d1:
    if key in d2:
        print(key)
