text = input("Enter a word or sentence : ")

text = text.lower()
char_count = {}

for ch in text:
    if ch == " ":
        continue
    if ch in char_count:
        char_count[ch] += 1
    else :
        char_count[ch] = 1

for ch,count in char_count.items():
    print(f"{ch} -> {count}")
