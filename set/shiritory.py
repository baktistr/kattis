# https://open.kattis.com/problems/shiritori

# input
n = int(input())
words = []
for i in range(n):
    word = input()
    words.append(word)

# initiate the 'seen' set and first last_letter
seen = set()
last_letter = words[0][-1]

for i in range(n):
    word = words[i]

    # Check if word has been used before or doesn't start with last letter, determine the player with modulo i (remind index: i = 0, player 1 start)
    if word in seen or (i > 0 and words[i][0] != last_letter):
        player = 1 + (i % 2)
        print("Player", player, "lost")
        break

    seen.add(word)
    last_letter = word[-1]

# game finish
else:
    print("Fair Game")