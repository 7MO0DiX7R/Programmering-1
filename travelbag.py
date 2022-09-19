# Travelbag
# Skelettkod till uppgiften

travelbag = ["Yazen", "eiffel tower", "The pyramids"]

while True:
   menyval = input("1. Kolla i resväskan\n"
                   "2. Lägg sak i resväskan\n"
                   "3. Ta bort sak i resväskan\n"
                   "4. Avsluta program ")

   if menyval == "1":
     print(*travelbag, sep=", ")
       

   elif menyval == "2":
    A = input("Vad vill du lägga? ")
    travelbag.append(A)
    print(*travelbag, sep=", ")
       

   elif menyval == "3":
    B = input("Vad vill du tabort? ")
    travelbag.remove(B)
    print(*travelbag, sep=", ")

   elif menyval == "4":
       break