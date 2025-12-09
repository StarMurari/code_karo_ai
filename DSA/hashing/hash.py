# words = ["apple", "banana", "apple", "orange", "banana", "apple"]

# # Create an empty hash table (dictionary)
# frequency = {}

# for word in words:
#     if word in frequency:
#         frequency[word] += 1   # update value
#     else:
#         frequency[word] = 1    # insert new key

# print(frequency["apple"])

arr = [1,2,3,1,2]

freq = {}

for i in arr:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print(freq[3])