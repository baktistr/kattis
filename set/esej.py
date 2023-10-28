# https://open.kattis.com/problems/esej

import random
import string
import math

# function to generate word, min 1 char to max 15 char
def generate_word():
    word_length = random.randint(1, 15)
    random_chars = random.choices(string.ascii_lowercase, k=word_length)
    random_word = ''.join(random_chars)
    return random_word

# handle input
A, B = map(int, input().split())

# Step 1 : Generate  B/2 Unique word first
unique_words = set()
for i in range(math.ceil(B / 2)):
    new_word = generate_word()
    unique_words.add(new_word)

## Check for size and add more unique words if needed
while len(unique_words) < math.ceil(B / 2):
    new_word = generate_word()
    unique_words.add(new_word)


# Step 2: If A > B//2, generate additional random words to reach A
additional_words = []
if A > len(unique_words):
    for _ in range(A - len(unique_words)):
        new_word = generate_word()
        additional_words.append(new_word)

# Step 3: Combine both lists
essay_words = list(unique_words) + additional_words

# Join them into a string
essay = ' '.join(essay_words)

print(essay)