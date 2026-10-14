slovo=input("Zadej slovo: ")
print(f"Slovo: {slovo}")
print(f"Počet znaků: {len(slovo)}")
print(f"První znak: {slovo[0]}")
print(f"Poslední znak: {slovo[-1]}")
print(f"Velkými písmeny: {slovo.upper()}")
back=slovo[::-1]
print(f"Pozpátku: {back}")
if slovo.lower()==back.lower():
    palindrom=True
else:
    palindrom=False
print(f"Palindrom: {palindrom}")