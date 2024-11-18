s=input()
n=len(s)
cons,vowel=0,0
for i in s:
    if i.lower() in "aeiou":
        vowel+=1
    elif "a"<i.lower()<="z":
        cons+=1
print(f"{vowel},{cons}")
