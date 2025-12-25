s = input("enter a string:")

unique_chars  = set(s)

print("unique characters")

for ch in unique_chars:
    print(ch, end=" ")

print(f"\ncount of unique characters is {len(unique_chars)}")