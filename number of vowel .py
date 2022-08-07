string = input("enter your String please ")
count = 0
vowels = set("aeiou")
for alphabet in string:

    if alphabet in vowels:
        count = count + 1

print(" number of vowel: ", count)