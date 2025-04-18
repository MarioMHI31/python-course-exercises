# def main():
#     fisier=open("fisier.txt",'w')
#     for numar in range(5):
#         cuvant=input("Introduceti un cuvant: ")
#         fisier.write(cuvant+ '\n')
# main()

# 2. Scrieți un program care să citească un fișier text “text.txt” și să afișeze câte vocale și consoane conține textul din fișier.
# def main():
#     fisier=open("fisier.txt",'r')
#     text=fisier.read()
#     nr_vocale=0
#     nr_consoane=0
#     vocale = "aeiouAEIOU"
#     for litera in text:
#         if litera in vocale:
#             nr_vocale+=1
# def main():
#     fisier=open("fisier.txt",'r')
#     text=fisier.read()
#     nr_vocale=0
#     nr_consoane=0
#     for litera in text:
#         if litera.lower in "aeiou":
#             nr_vocale+=1
#         elif litera.isalpha():
#             nr_consoane+=1
#     print(f"vocale: {nr_vocale} ,consoane:{nr_consoane}")
# main()




#
# 3. Scrieți un program care să citească un fișier text “propozitie.txt” și să afișeze cuvintele din propozitie în ordine inversă.
# def main():
#     fisier=open("propozitie.txt",'r')
#     text=fisier.read()
#     cuvinte=text.split()
#     cuvinte_inversate=" ".join(reversed(cuvinte))
#     # fisier.close()
#     with open("propozitie.txt",'a') as file:
#         file.write("\n propozitie inversata:" + cuvinte_inversate)
#     print(f"Propozitia inversata este: {cuvinte_inversate}")

# main()
# 4. Scrieți un program care să citească un fișier text “text.txt” și să afișeze de câte ori apare fiecare cuvânt în text.
# def main():
#     fisier=open("text.txt",'r')
#     text=fisier.read()
#     # numar_cuvinte=0
#     cuvinte=text.split()
#     cuvinte_unice=set(cuvinte)
#     for cuvant in cuvinte_unice:
#         # numar_cuvinte+=1
#         print(f"{cuvant}: {cuvinte.count(cuvant)} aparitii.")
#     fisier.close()
# main()
# 5.Scrieți un program care să creeze un fișier text “animale.txt” și să ceară utilizatorului să introducă numele a 5 animale.
# La final, programul va afișa toate animalele introduse în ordine alfabetică.
# def main():
#     with open("animale.txt", "w") as fisier:
#         animale = []
#
#         for animall in range(5):
#             animal = input(f"Introdu numele animalului {animall + 1}: ")
#             animale.append(animal)
#
#         for animal in animale:
#             fisier.write(animal + "\n")
#
#     animale.sort()
#     print("Animalele introduse în ordine alfabetica sunt:")
#     for animal in animale:
#         print(animal)
#
#
# main()
# Creează o funcție care generează un fișier numit numere_pare.txt și scrie în el doar numerele pare de la 1 la 100, fiecare pe o linie separată.
# def scrie_numere_pare():
#     with open('numere_pare.txt', 'w') as f:
#         for i in range(1, 101):
#             if i % 2 == 0:
#                 f.write(f"{i}\n")

# Creează o funcție care generează un fișier numit patrate.txt și scrie în el pătratul numerelor de la 1 la 100 (fiecare pe o linie).
# def main():
#     with open('patrate.txt','w') as fisier:
#         for numar in range(1,101):
#             fisier.write(f"{numar**2}\n")
# main()
# Creează o funcție care generează un fișier numit tabel_inmultire.txt și scrie în el tabla înmulțirii pentru numerele de la 1 la 10 (de exemplu, 1 * 1 = 1, 1 * 2 = 2 etc.).
# def main():
#     with open('tabel_inmultire.txt', 'w') as fisier:
#         for i in range(1,11):
#             for j in range(1,11):
#                 fisier.write(f"{i}*{j}={i*j}\n")
# main()

