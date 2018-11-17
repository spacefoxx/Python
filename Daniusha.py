word = input("Write a single word that is loger than 5 symbols\n")
word_len = len(word)

is_hungry = word_len > 10
is_sleepy = word_len % 2 != 0
is_bitter = "a" in word or "e" in word

if is_bitter and is_hungry and is_sleepy:
    print("Pai se!")
elif is_bitter and is_sleepy:
    print("Izgasi lampata")
elif is_hungry and is_bitter:
    print("Az shte napravq guakamole")
elif is_hungry and is_sleepy:
    print("Po dobre da hapnem utre")
else:
    print("Safe si!")
