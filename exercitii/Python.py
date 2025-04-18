# print("Hello, Mario!")
# print(float(12))
# print(int(14.8))
# print(int("236"))
# print(float("236"))
# print(type(str(17)))
# print(int(False))
#
# # scoala = "Mario este student al colegiului"
# # salutare = scoala + " Mihai Eminescu"
# # print(salutare)
#
# cuvant = "Hello"
#
# print (len(cuvant))
#1
# numere = 123
# print(type(numere))
# siruri_de_caractere = "Ana are mere"
# print(type(siruri_de_caractere))
# valoare_de_adevar = False
# print(type(valoare_de_adevar))
# #2
# print(2+3+4+5)
# print(10-9-8-7)
# print(2*4*6)
# print(8/4/2)
# #3
# print(8==8)
# print(8==7)
# print(5!=5)
# print(5!=6)
# print(9>=8)
# print(7>=8)
# print(9<=8)
# print(7<=8)
# #4.1
# print("Buna seara," + "" + "lume!")
# #4.2
# print("Buna dimineata!".upper())
# print("Buna dimineata!".lower())
# #4.3
# nume="Mario"
# print(f"Numele meu este {nume}")
# #4.4
# nume="Mario"
# varsta="19"
# print(f"Numele meu este {nume} si am varsta de {19} ani")
# #5.1
# print("Salut, " + "Mario!")
# # 5.2
# print("hello" * 5)
# #5.3
# cuvant = "Beautiful"
# print(cuvant[3])
# # 5.4
# txt = "Good morning!"
# print(txt[2:5])
# # 5.5
# text="Good evening!"
# print(len(text))
# #5.6
# print("Hello" in "Hello ,people!")
# print("Hello" not in "Hello, people!")
# #5.7
# print("Burning".count("n"))
# # 5.8
# print("Buna Seara!".upper())
# print("Buna Seara!".lower())
# print("Buna Seara!".capitalize())
# # 5.9
# print("Buna seara, lume!".replace("seara","ziua"))
 # print("Buna seara, lume!".split())
 # print('banane','pere','ananas',sep=" ")
# print("Ana are mere".replace("mere","pere"))
# print("Ana are mere".split(" "))


#   5.10 Exercițiu: Eliminați spațiile albe de la începutul și sfârșitul unui string a = " Hello World ".(Hint: folosiți strip()).
# print(" Ana are mere ".strip())
# TODO 6: Exercitii cu input de la tastatura
#  6.1 Exercițiu: Exercițiu: Solicitați utilizatorului să introducă un nume și afișați-l.
# nume=input("Numele tau este:")
# print(nume)
#  6.2 Exercițiu: Exercițiu: Cereți utilizatorului să introducă anul său de naștere și calculați vârsta acestuia în anul curent.
# an_nastere=int(input("In ce an te-ai nascut?"))
# anul_curent=2024
# print(f"Varsta este {anul_curent-an_nastere}")
#  6.3 Exercițiu: Scrieți un program care cere utilizatorului să introducă două numere și apoi adunati numeerele. Efectuați operația și afișați rezultatul.
# numar_unu=int(input("Primul numar este "))
# numar_doi=int(input("Al doilea numar este "))
# print(f"Rezultatul este {numar_unu+numar_doi}")

# TODO 7: Exercitii combinate
#  7.1 Exercițiu: Cereți utilizatorului să introducă un număr și apoi afișați rezultatul ridicat la pătrat.
# numar=int(input("Numerul strazii este "))
# print(numar**2)
#
# nume= input("Numele tau este: ")
# prenume = input("Prenumele tau este: ")
# adresa_de_mail= f"{nume}.{prenume}@yahoo.com"
# print(adresa_de_mail)
#
# prima_nota=int(input("Prima nota este: "))
# nota_doi=int(input("Nota doi este: "))
# nota_trei=int(input("Nota trei este: "))
# media_notelor=f"Media notelor este {(prima_nota+nota_doi+nota_trei)/3}"
# print(media_notelor)
#
# text=input("Introduceti un sir de caractere: ")
# print(text[::-1])
#
# cuvant = input("Introduceți un cuvânt: ")
# este_palindrom = cuvant == cuvant[::-1]
# print(este_palindrom)


# lista_mea=[1,2,3,4,5,6]
# lista_mea.reverse()
# print(lista_mea)

# dictionarul_meu = {'nume': 'Alex', 'varsta': 33, 'oras': 'Bucuresti'}
 # print(dictionarul_meu["nume"])

#1.1
#lista_mea=["Oua","Legume","Fructe","Plante"]
#print(lista_mea)
#1.2
#lista_mea.append("Animale")
#print(lista_mea)
#1.3
#lista_mea.remove("Oua")
#print(lista_mea)
#1.4
#print(lista_mea.index("Legume"))
#lista_mea[0]="Cauciuc"
#print(lista_mea)
#1.5
#sublist=lista_mea[::3]
#print(sublist)
#2.1
#dictionarul_meu = dict("nume"="Serban", "oras"="Iasi", "varsta"=18)
#print(dictionarul_meu)
#2.2
#dictionarul_meu={"nume":"Serban", "oras":"Iasi", "varsta":18}
#dictionarul_meu["nume"]="Andrei"
#print(dictionarul_meu)
#2.3
#del dictionarul_meu["oras"]
#print(dictionarul_meu)
#3.1
#tupla_mea=("Pisica","Caine","Delfin","Tigru")
#print(tupla_mea)
#3.2
#print(tupla_mea.index("Delfin"))
#print(tupla_mea.index("Tigru"))
#4.1
#setul_meu= {1,2,3,4,5}
#print(setul_meu)
#4.2
#setul_meu.update([6,7,0])
#print(setul_meu)
#setul_meu.remove(4)
#print(setul_meu)

# text="123  124 125"
# for numar in text:
#     print(numar)

# lista_mea=[1,2,3,"java"]
# # print(lista_mea)
#
# lista_mea.append("Mario")
# # print(lista_mea)
#
# # lista_mea.remove("java")
# # print(lista_mea)
#
# lista_mea[1]="doi"
# print(lista_mea)

# sublista=lista_mea[2:5]
# print(sublista)

# dictionarul_meu=dict(nume="Mario",varsta=19,oras="Bucuresti")
# print(dictionarul_meu)

# dictionarul_meu={'nume': 'Mario', 'varsta': 19, 'oras': 'Bucuresti'}
# # dictionarul_meu['nume']="Mihai"
# # print(dictionarul_meu)
#
# dictionarul_meu.pop("varsta")
# print(dictionarul_meu)
#
# tupla_mea=("Mario",1,2,3)
# # print(tupla_mea)
# print(tupla_mea.index("Mario"))
#
# setul_meu={1,2,3,4}
# # print(setul_meu)
# # setul_meu.add("Mario")
# setul_meu.update(["Mario",4,5,6])
# setul_meu.discard(6)
# setul_meu.remove(5)
# print(setul_meu)

5.1
# numar=int(input("Numarul dvs este: "))
# if numar % 2==0:
#     print(f"{numar} is an even number")
# else:
#     print(f"{numar} is an odd number")
5.2
# primul_numar=input("Primul numar este: ")
# numarul_doi=input("Numar doi este: ")
# if primul_numar>numarul_doi:
#     print(f"{primul_numar} este mai mare.")
# elif numarul_doi>primul_numar:
#     print(f"{numarul_doi} este mai mare.")
# else:
#     print(f"{primul_numar} este egal cu numarul {numarul_doi}")
5.3
# varsta_utilizatorului=int(input('Care este varsta dvs? '))
# if varsta_utilizatorului>=18:
#     print(f"Accesul in club va este permis.")
# else:
#     print(f"Accesul in club nu va este permis.")
5.4
# prima_persoana=int(input("Varsta ta este: "))
# if prima_persoana <= 0:
#     print("Varsta este invalida")
# elif prima_persoana<18:
#     print("copil")
# elif prima_persoana<=65:
#     print("adult")
# elif prima_persoana>65:
#     print("senior")
5.5
# numarul_meu=int(input("Numarul meu este: "))
# if numarul_meu % 3==0 and numarul_meu % 5==0:
#     print(f"{numarul_meu} este divizibil si cu 3 si cu 5 ")
# elif numarul_meu % 3==0:
#     print(f"{numarul_meu} este divizibil cu 3 si nu cu 5")
# elif numarul_meu % 5==0:
#     print(f"{numarul_meu} este divizibil cu 5 si nu cu 3")
# else:
#     print(f"{numarul_meu} nu e divizibil nici cu 3 nici cu 5")

6.1
# for numar in range(11):
#     print(numar)
6.2
# n=int(input("numarul introdus de utilizator: "))
# for numar in range(1,n):
#     print(numar)
6.3
# lista_mea=[1,2,3,4,5,"Mario","frumosul"]
# for element in lista_mea:
#     print(element)
6.4
# stringul=input("Ce string doriti sa fie afisat? ")
# for caracter in stringul:
#     print(caracter)
6.5
# fructe=["banane","mere","caise",123]
# for fruct in enumerate(fructe):
#     print(fruct)
7.1
# for numar in range(1,11):
#     if numar == 7:
#         continue
#     print(numar)
7.2
# for numar in range(1,11):
#     if numar == 8:
#         break
#     print(numar)
7.3
# lista_mea=[1,3,4,5,6,7,8,9,10]
# for numar in lista_mea:
#     if numar%2==0:
#         break
#     print(numar)
7.4
# lista_mea=[1,2,3,4,5,6,7,8,9,10]
# for numar in lista_mea:
#     if numar % 2 == 0:
#         continue
#     print(numar)
7.5

# parola_corecta= "parola123"
# numar_de_incercari= 3
# for incercari in range(numar_de_incercari):
#     parola_introdusa=input("Introduceti parola dvs: ")
#
#     if parola_introdusa == parola_corecta:
#         print(f"Parola corecta.Acces permis!")
#         break
#     else:
#         print(f"Parola introdusa a fost gresita. Incercare {incercari+1} din {numar_de_incercari}")
#     if incercari==numar_de_incercari-1:
#         print(f"Numarul maxim de incercari a fost atins.")




# -------------------------------------------------------------------------
# lista_mea=[1,2,3,4,"Maria","loialitate"]
# lista_mea.append(5)
# print(lista_mea)
# lista_mea.remove("loialitate")
# print(lista_mea)
# lista_mea[5]="infidelitate"
# print(lista_mea)
# sublista=lista_mea[:6:2]
# print(sublista)
# dictionarul_meu=dict(nume="Mario",varsta=19,oras="Bucuresti")
# print(dictionarul_meu)
# dictionar={'nume': 'Mario', 'varsta': 19, 'oras': 'Bucuresti'}
# # dictionar["nume"]="Mihai"
# # print(dictionar)
# dictionar.pop("nume")
# print(dictionar)
# tupla=(1,2,3,4,5,6)
# # # print(tupla.index(2))
# numar=int(input("Digite um numero: "))
# if numar % 2 == 0:
#     print(f"{numar} este par")
# else:
#     print(f"{numar} este impar")
# suma=0
# while suma<=100:
#     numar=int(input("Ingrese un numero: "))
#     suma=suma+numar
# print(suma)

# numar_secret=5
# while True:
#     numar_ales=int(input("Alege un numar intre 1-10: "))
#     if numar_ales==numar_secret:
#         print("Ai ghicit")
#         break
#     else:
#         print("Mai incearca!")

# for i in range(1,51):
#     if i % 3 == 0 and i % 5 == 0:
#         print(i)

# cuvant=input("Care este cuvantul tau: ")
# palindrom=cuvant[::-1]
# if cuvant==palindrom:
#     print(f"{cuvant} este un palidrom")

# cuvant=input("Cuvant: ")
# vocale="aeiouAEIOU"
# numar_vocale=0
# for litera in cuvant:
#     if litera in vocale:
#         numar_vocale+=1
# print(f"Cuvantul {cuvant} are {numar_vocale} vocale")

# numar =input("Scrie un numar: ")
# suma_cifre = 0
# for cifra in numar:
#     suma_cifre += int(cifra)
# print(f"Suma cifrelor numărului {numar} este {suma_cifre}.")

# lista=["Mario","Maria","foc","scantei"]
# element=input("Elementul tau este? ")
# if element in lista:
#     print(f"{element} este in lista mea")
# else:
#     print(f"{element} nu este in lista mea")

# numar_utilizator=int(input("Introduceti un numar: "))
# for numar in range(1,numar_utilizator+1):
#     if numar % 2 != 0:
#         print(numar)

# numar_unu=int(input("Introduceti primul numar: "))
# numar_doi=int(input("Introduceti al 2-lea numar: "))
# numar_trei=int(input("Introduceti al 3-lea numar: "))
# numar_patru=int(input("Introduceti al 4-lea numar: "))
# numar_cinci=int(input("Introduceti al 5-lea numar: "))
# if numar_unu>numar_doi and numar_unu>numar_trei and numar_unu>numar_patru and numar_unu>numar_cinci:
#     print(f"{numar_unu} este cel mai mare")
# elif numar_doi>numar_unu and numar_doi>numar_trei and numar_doi>numar_patru and numar_doi>numar_cinci:
#     print(f"{numar_doi} este cel mai mare")
# elif numar_trei>numar_unu and numar_trei>numar_doi and numar_trei>numar_patru and numar_trei>numar_cinci:
#     print(f"{numar_trei} este cel mai mare")
# elif numar_patru>numar_unu and numar_patru>numar_doi and numar_patru>numar_trei and numar_patru>numar_cinci:
#     print(f"{numar_patru} este cel mai mare")
# elif numar_cinci>numar_unu and numar_cinci>numar_doi and numar_cinci>numar_patru and numar_cinci>numar_trei:
#     print(f"{numar_cinci} este cel mai mare")

# maxim=None
# for i in range(5):
#     numar = int(input(f"Introdu numarul {i+1}: "))
#     if maxim is None or numar > maxim:
#         maxim =numar
# print(f"Cel mai mare numar este: {maxim}")

# numar=int(input("Digite um numero: "))
# if numar%1==0 and numar%

# n=input("Un numar: ")
# suma_cifre=0
# for cifra in n:
#     suma_cifre+=int(cifra)
# print(f"Suma cifrelor numărului {n} este {suma_cifre}.")

# numar_utilizator=input("Introduceti un numar: ")
# suma=0
# for numar in numar_utilizator:
#     suma+=int(numar)
# print(f"Suma cifrelor numarului {numar_utilizator} este {suma}")

# for i in range(1,10):
#     if i%2!=0:
#         print(f"Bucla se oprește la numărul {i}")
#         break

# for i in range(1,16):
#     if i%3==0:
#         continue
#     print(i)







# def suma_doua_numere(numarul_1,numarul_2):
#     total=numarul_1+numarul_2
#     return total
# print(suma_doua_numere(5,6))

# def saluta(nume):
#     mesaj="Salut "+nume
#     return mesaj
# print(saluta("Mario"))

# def suma(*args):
#     total=0
#     for numere in args:
#         total+=numere
#     return total
# print(suma(1,2,3,4,5,6,100))

# def suma_doi(*args):
#     return sum(args)
# print(suma_doi(1,2,3,4))

# def informatii_personale(**kwargs):
# 	for cheie, valoare in kwargs.items():
# 		print(f'{cheie}:{valoare}')
#
# informatii_personale(nume="Mario",varsta=19)

# def exemplu(*args,**kwargs):
#     print(args)
#     print(kwargs)
# exemplu(1,2,3,4,5,6,nume="Mario",varsta=19)

# def cauta_numar(lista,numar_cautat):
#     index=0
#     while index<len(lista):
#         if index==numar_cautat:
#             print(f"Numarul cautat {numar_cautat} a fost gasit!")
#             break
#         index+=1
#     else:
#         print("Numarul nu este corect.")
# cauta_numar([1,2,3,4,5,6,7],5)

# def numele(nume):
#     print(f"Numele meu este {nume}")
# numele("Mario")

# def produs(*args):
#     total=1
#     for numere in args:
#         total*=numere
#     return total
#
#
#
# print(produs(1,2,3,4,5))

# def informatii_produs(**kwargs):
#     for cheie, valoare in kwargs.items():
#         print(f"{cheie.capitalize()}: {valoare}")
#
# informatii_produs(nume="Laptop", pret=2500, stoc=True)

#  Scrieți o funcție salut() care afișează "Salut, lume!" și apoi apelați această funcție.
# def salut():
#     print("Salut, lume!")
# salut()
# TODO 2.Funcție cu Parametri:
#  Definiți o funcție afiseaza_mesaj(mesaj) care primește un parametru și afișează acel mesaj. Testați funcția cu diferite mesaje.
# def afiseaza_mesaj(mesaj):
#     mesaj_doi="Buna dimineata, "+mesaj
#     return mesaj_doi
# print(afiseaza_mesaj("tuturor!"))
# TODO 3. Funcție cu Parametri Multipli:
#  Creați o funcție suma_doua_numere(a, b) care returnează suma a două numere date ca argumente.
# def suma(numar_1,numar_2):
#     total=numar_1+numar_2
#     return total
# print(suma(5,6))
# TODO 4. Funcție cu Parametri Default:
#  Scrieți o funcție descrie_animal(animal="câine") care afișează "Animalul meu preferat este [animal]." Testați funcția cu și fără a specifica argumentul.
# def descrie_animal(animal="caine"):
#     print(f"Animalul meu preferat este {animal}")
# descrie_animal()
# descrie_animal(animal="iepure")



# TODO 5. Funcție care Returnează Valoare:
#  Definiți o funcție este_par(numar) care returnează True dacă numărul este par și False dacă este impar.
# def este_par(numar):
#     if numar%2==0:
#         print("True")
#     else:
#         print("False")
# este_par(4)
# TODO 6. *Funcție cu args:
#  Creați o funcție suma_numerelor(*numere) care returnează suma tuturor numerelor date ca argumente.
# def suma_numerelor(*numere):
#     return sum(numere)
# print(suma_numerelor(321,231,32,4432))
# TODO 7. **Funcție cu kwargs:
#  Definiți o funcție afiseaza_date_personale(**date) care afișează datele personale primite sub forma de perechi cheie-valoare.
# def afiseaza_date_personale(**date):
#     for cheie,valoare in date.items():
#         print(f"{cheie}:{valoare}")
# afiseaza_date_personale(nume="Mario",varsta=19,oras="Bucuresti")
# TODO 8.Combinarea *args și kwargs într-o Funcție:
#  Scrieți o funcție combina_args_kwargs(*args, **kwargs) care afișează lista argumentelor poziționale și dicționarul argumentelor cheie-valoare.
# def combina_args_kwargs(*args,**kwargs):
#     print(args)
#     print(kwargs)
# combina_args_kwargs(1,2,3,4,5,6,7,8,9,nume="Serban",varsta=19)
# TODO 9.Funcție cu Instrucțiunea break într-un Loop:
#   Definiți o funcție cauta_in_lista(lista, element) care caută litera "x" într-o listă și oprește căutarea când elementul este găsit, afișând indexul acestuia.
lista = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "x", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s"]
# # rezultatul ar trebui să fie: "Elementul x a fost găsit la indexul 9"
# def cauta_in_lista(lista,element):
#     index=0
#     while index < len(lista):
#         if lista[index]==element:
#             print(f"Elementul {element} a fost găsit la indexul {index}")
#             break
#         index+=1
#     else:
#         print(f"Elementul nu a fost gasit in lista.")
# cauta_in_lista(lista,"x")
# def cauta_in_lista(lista,element):
#     for index,valoare in enumerate(lista):
#         if valoare == element:
#             print(f"{index}:{valoare}")
#             break
#     else:
#             print(f"Elementul {element} nu este in lista.")
# cauta_in_lista(lista,"x")


# Scrieți o funcție inversare_lista(lista) care primește o listă ca argument și returnează lista inversată. Testați funcția cu diferite liste.
# # def inversare_lista(lista):
# #     print(lista[::-1])
# # inversare_lista([1,2,3,4,5])
# Creați o funcție adauga_intrare(dictionar, cheie, valoare) care adaugă o nouă pereche cheie-valoare într-un dicționar. Testați funcția cu diferite dicționare și perechi cheie-valoare.
# # dictionarul_meu={"nume":"Cristian","varsta":99,"oras":"Iasi"}
# # def adauga_intrare(dictionar,cheie,valoare):
# #     dictionar[cheie]=valoare
# #     return dictionar
# # cheie_1="prenume"
# # valoare_1="Matei"
# # print(adauga_intrare(dictionarul_meu,cheie_1,valoare_1))
# Scrieți o funcție patratele_numerelor(lista) care primește o listă de numere și returnează o nouă listă care conține pătratele numerelor din lista originală, utilizând o listă comprehension.
# def patratele_numerelor(lista):
#     return[numar**2 for numar in lista]
# lista=[1,2,3]
# print(patratele_numerelor(lista))
# Creați o funcție adauga_student(nume, varsta, note) care primește ca argumente numele, vârsta și o listă de note ale unui student și returnează un dicționar care reprezintă acest student.

# def adauga_student(nume,varsta,note):
#     student={"nume":nume,"varsta":varsta,"note":note}
#     return student
# nume="Andrei"
# varsta=20
# note=[10,9,8]
# print(adauga_student(nume,varsta,note))

# Creați o funcție perimetru_dreptunghi(lungime, latime) care primește lungimea și lățimea dreptunghiului și returnează perimetrul acestuia.

# def perimetru_dreptunghi(lungime,latime):
#     perimetrul=2*(lungime+latime)
#     return perimetrul
# print(perimetru_dreptunghi(7,5))
# Creați o funcție lungime_string(text) care primește un string și afișează lungimea acestuia.

# def lungime_string(text):
#     lungime=len(text)
#     print(f"lungimea textului este: {lungime}")
# lungime_string("Buna dimineata!")

# Definiți o funcție este_positiv(numar) care primește un număr și afișează un mesaj dacă numărul este pozitiv sau nu (“Numărul este pozitiv” sau “Numărul nu este pozitiv”)

# def este_pozitiv(numar):
#     if numar>0:
#         print(f"Numarul {numar} este pozitiv.")
#     else:
#         print(f"Numarul {numar} nu este pozitiv.")
# este_pozitiv(4)
# import math
# print(math.sqrt(49))
# import random
# lista=["a", "b", "c", "d", "e", "f", "g", "h", "i", "x", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s"]
# def element_aleatoriu(min,max):
#     return random.randint(min,max)
# print(index(element_aleatoriu(0,20)))
# element_aleatoriu(0,20)

# def afiseaza_mesaj(mesaj):
#     print(mesaj)
# afiseaza_mesaj("Ce mai faci, Mario?")

# def suma_doua_numere(numarul_1, numarul_2):
#     total=numarul_1+numarul_2
#     return total
# print(suma_doua_numere(5,6))

# def descrie_animal(animal="caine"):
#     print(f"Animalul meu preferat este {animal}")
# descrie_animal()
# descrie_animal(animal="pisicuta")

# def este_par(numar):
#     if numar%2==0:
#         print("True")
#     else:
#         print("False")
# este_par(5)

# def suma_numerelor(*numere):
#     return sum(numere)
# print(suma_numerelor(13912,323))

# def afiseaza_date_personale(**date):
#     for cheie,valoare in date.items():
#         print(f"{cheie}: {valoare}")
# afiseaza_date_personale(nume="Mario",oras="Bucuresti")

# def combina_args_kwargs(*args, **kwargs):
#     print(args)
#     print(kwargs)
# combina_args_kwargs(1,2,3,"java",nume="Mario",oras="Bucuresti")

lista = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "x", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s"]
# def cauta_in_lista(lista, element):
#     index=0
#     while index < len(lista):
#         if lista[index]==element:
#             print(f"Elementul {element} a fost gasit pe pozitia {index}")
#             break
#         index+=1
#     else:
#         print(f"Elementul {element} nu a fost gasit in lista.")
# cauta_in_lista(lista, "y")
# def cauta_in_lista(lista, element):
#     for index,valoare in enumerate(lista):
#         if valoare==element:
#             print(f"{index}:{element}")
#             break
#     else:
#         print("Elementul nu a fost gasit")
# cauta_in_lista(lista, "y")
#
# import random
# print(random.choice(["a", "b", "c", "d", "e", "f", "g", "h", "i", "x", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s"]))

# def inmulteste_cu_doi(numar):
#     total=numar * 2
#     return total
# print(inmulteste_cu_doi(15))

# def calculeaza_perimetru(lungime, latime=None):
#     perimetru=2*(lungime+latime)
#     return perimetru
# print(calculeaza_perimetru(7,5))

# def verifica_palindrom(cuvant):
#     return cuvant==cuvant[::-1]
# print(verifica_palindrom("mamamamam"))
























# TODO 10.Selectarea Aleatorie a unui Element dintr-o Listă cu Modulul Random:
#  Creați o funcție element_aleatoriu(lista) care returnează un element aleatoriu din lista furnizată.
# lista_mea = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "x", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s"]
# import random
# def element_aleatoriu(lista_mea):
#     return random.choice(lista_mea)
# print(element_aleatoriu(lista_mea))
# TODO 11.Rotunjirea Numerelor cu Modulul Math:
#  Importați modulul math.
#  Creați o funcție rotunjeste_numar(numar) care folosește funcția math.round() pentru a rotunji numărul la cel mai apropiat întreg și returnează rezultatul.
# import math
# def rotunjeste_numar(numar):
#     return round(numar)
# print(rotunjeste_numar(2.7))
# TODO 12.Afișarea Zilei din Săptămână a unei Date Specifice cu Modulul Datetime:
#  Importați datetime din modulul datetime.
#  Creați o funcție ziua_saptamanii(an, luna, zi) care primește o dată specifică și returnează ziua săptămânii pentru acea dată (ex: "Luni", "Marți", etc.).
#   Hint: Folositi date.strftime("%A") pentru a afișa ziua din săptămână.
# import datetime
# def ziua_saptamanii(an,luna,zi):
#     data=datetime.date(an,luna,zi)
#     return data.strftime("%A")
# print(ziua_saptamanii(2024,8,28))

# class Elev:
#     def __init__(self,nume,varsta):
#         self.nume=nume
#         self.varsta=varsta
#     def print_details(self):
#         print(f"{self.nume} {self.varsta}")
# primul_elev=Elev("Mario",19)
# print(primul_elev.varsta,primul_elev.nume)
# primul_elev.print_details()
#
# class Elev:
#     def __init__(self,nume,varsta):
#         self.nume=nume
#         self.varsta=varsta
#     def __gt__(self,other):
#         return self.varsta > other.varsta
#     def __lt__(self,other):
#         return self.varsta < other.varsta
# elev_1=Elev("Mario",19)
# elev_2=Elev("Mario",17)
# print(elev_1>elev_2)
# class Elev:
#     def __init__(self,nume,varsta):
#     self.nume=nume
#     self.varsta=varsta
#     def __len__(self):                                   #__gt__ #__ge__ #__le__ #__lt__ #__eq__ #__ne__
#
#         print(len(self.varsta))

# class Animal:
#     def __init__(self,nume,varsta):
#         self.nume=nume
#         self.varsta=varsta
#     def __len__(self):
#         return len(self.varsta)
# animal_1=Animal("Mario",19)
# print(len(animal_1.nume))

# class Animal:
#     def __init__(self,name,age):
#         self.__name = name
#         self.__age = age
#     def age(self):
#         return self.__age
# # animal_1=Animal("Mario",19)
# # print(animal_1.age())
#     def age(self,age):
#         if age>0:
#             self.__age=age
#         else:
#             print("Varsta")



# class Animal:
# 	def __init__(self, nume, varsta):
# 		self.nume = nume
# 		self.varsta = varsta
#
# 	def __add__(self, other):
# 		return Animal(self.nume, self.varsta + int(other))
#
# 	def __str__(self):
# 		return f'{self.nume} are varsta de {self.varsta} ani.'
#
# 	def __int__(self):
# 		return self.varsta
#
# animal = Animal("Max",1)
# print(animal+100)

# TODO
# 1.
# Creati
# o
# clasa
# Vehicul
# astfel
# incat, 'Exemplu de utilizare a clasei Vehicul sa functioneze':
#   Se creează o clasă Vehicul cu atribute pentru marca, model și anul fabricației.
# #   Adaugăm o metodă care returnează vârsta vehiculului în ani.Hint: folositi modulul datetime
# import datetime
# class Vehicul:
#     def __init__(self,marca,model,an):
#         self.marca=marca
#         self.model=model
#         self.an=an
#     # def varsta(self):             #metoda 1
#     #     return 2024-self.an
#     def varsta(self):               #metoda 2
#         an_curent=datetime.datetime.now().year
#         return an_curent-self.an
#
# # Exemplu de utilizare a clasei Vehicul
# vehicul = Vehicul('Ford', 'Mustang', 1967)
# varsta_vehicul = vehicul.varsta()
# print(varsta_vehicul)





#  TODO 1.1 Adaugati in clasa Vehicul astfel încât să includă o metodă care determină dacă vehiculul este considerat
#   un vehicul clasic (vârsta mai mare de 30 de ani). De asemenea, adăugați o metodă care returnează un șir de
#   caractere formatat, care să includă și informația dacă vehiculul este clasic.
# import datetime
# class Vehicul:
#     def __init__(self,marca,model,an):
#         self.marca=marca
#         self.model=model
#         self.an=an
#     def varsta(self):               #metoda 2
#         an=datetime.datetime.now().year
#         return an-self.an
#     def vehicul_clasic(self):
#         return self.varsta()>30
#     def __str__(self):
#         return f"Vehiculul {self.marca} {self.model} este un vehicul clasic."
# vehicul=Vehicul("Audi","rs3","1990")
# varsta_vehicul=vehicul_clasic()
# print(vehicul.vehicul_clasic())
# TODO 2. Creati o clasă MasinaUnu în Python care să îndeplinească următoarele cerințe:
#  Clasa trebuie să aibă un constructor __init__ care să accepte trei argumente: marca, culoare, și an_fabricatie.
#  Fiecare dintre aceste argumente ar trebui să aibă o valoare implicită, respectiv 'Audi' pentru marca, 'verde' pentru culoare și 1990 pentru anul fabricației.
#  Definește o metodă descriere care returnează un șir de caractere ce descrie mașina folosind atributele sale, în formatul: "Masina este un [marca] din anul [an_fabricatie], de culoare [culoare]."
#   Creați o instanță a clasei Masina folosind valorile implicite și afișați descrierea acesteia folosind metoda magica __str__.
#   Creați o instanță a clasei Masina cu marca 'BMW', culoarea 'albastru' și anul fabricației 2020, și afișați descrierea acesteia.
# class Masina:
#     def __init__(self,marca, culoare, an_fabricatie):
#         self.marca=marca
#         self.culoare=culoare
#         self.an_fabricatie=an_fabricatie
#     def descriere(self):
#         return f"Masina este un {self.marca} din anul {self.an_fabricatie}, de culoare {self.culoare}."
#     def print_details(self):
#         print(f"Masina este un {self.marca} din anul {self.an_fabricatie}, de culoare {self.culoare}.")
#     def __str__(self):
#         return f"Masina este un {self.marca} din anul {self.an_fabricatie}, de culoare {self.culoare}."
#     def __repr__(self):
#         return f"marca={self.marca!r}, culoare={self.culoare!r}, an_fabricatie={self.an_fabricatie!r}"
# masina_mea=Masina("Audi","verde",1990)
# masina_doi=Masina("BMW","albastru",2020)
# print(masina_mea.descriere())
# masina_mea.print_details()
# print(str(masina_mea))
# print(repr(masina_doi))
# TODO 2.1 Modificați clasa MasinaUnu pentru a include un atribut este_electrica, cu valoarea implicită False.
#  Adăugați logica necesară astfel încât metoda descriere să includă și informația despre propulsia mașinii (
#  electrică sau convențională).
# class Masina:
#     def __init__(self,marca="Audi",culaore="verde",an=1990,este_electrica=False):
#         self.marca=marca
#         self.culaore=culaore
#         self.an=an
#         self.este_electrica=este_electrica
#     def descriere(self):
#         if self.este_electrica:
#             tip_propulsie="electric"
#         else:
#             tip_propulsie="benzina"
#         return f"Masina este un {self.marca} din anul {self.an}, de culoare {self.culaore}, cu propulsie {tip_propulsie}."
# masina_mea=Masina()
# print(masina_mea.descriere())


# TODO 3. Creati o clasa numita "MasinaDoi" care sa aiba ca proprietati marca, model, an fabricatie, culoare,
#  pret. Instantiati 3 obiecte de tipul Masina. Utilizati metoda __str__ pentru a afisa toate proprietatile
#  obiectelor create(eg. Audi A4 din 2019, culoare neagra, pret 20000 euro).
# class MasinaDoi:
#     def __init__(self,marca,model,an_fabricatie,culoare,pret):
#         self.marca=marca
#         self.model=model
#         self.an_fabricatie=an_fabricatie
#         self.culoare=culoare
#         self.pret=pret
#     def __str__(self):
#         return f"{self.marca} {self.model} din {self.an_fabricatie}, culoare {self.culoare},pret  {self.pret} euro."
# masina_mea=MasinaDoi("Audi","A4","2019","neagra", 20000)
# print(masina_mea)
# masina_doi=MasinaDoi("BMW","X5","2019","alba",18800)
# print(masina_doi)
# masina_trei=MasinaDoi("Ford","Mustang","2020","galbena",21000)

# TODO 3.1  Implementați o clasă FlotaAuto care să gestioneze un set de obiecte MasinaDoi. Clasa ar trebui să permită
#  adăugarea și ștergerea mașinilor din flotă și să ofere o metodă pentru a afișa cea mai scumpă mașină din flotă.
#   Hint. In constructorul Clasei Flota nu oferiti atribute la instanta clasei, ci doar initializati un atribut gol

# class FlotaAuto:
#   def __init__(self):
#      self.flota = []
# .....
# class FlotaAuto:
#     def __init__(self):
#         self.flota=[]
# flota_1=FlotaAuto()
# print(flota_1.flota)
#
# class FlotaAuto2:
#     def __init__(self,flota):
#         self.flota=flota
# flota_2=FlotaAuto2(flota=[])
# print(flota_2.flota)

# class FlotaAuto:
#     def __init__(self):
#         self.flota=[]
#     def adauga_masini(self,masina):
#         self.flota.append(masina)
#     def stergere_masini(self,masina):
#         if masina in self.flota:
#             self.flota.remove(masina)
#         else:
#             print(f"Masina {masina} nu exista in flota")
#     def masina_scumpa(self):
#         if not self.flota:
#             return "Flota este goala"
#         masina_scumpa=self.flota[0] #presupunem ca prima masina este cea mai scumpa
#         for masina in self.flota[1:]: #parcurgem restul indexilor din lista de la indexul 1 pana la final
#             if masina.pret>masina_scumpa.pret:
#                 masina_scumpa=masina
#          return masina_scumpa
# flota=FlotaAuto() #Instantiere/creare de obiecte din clasa de FlotaAuto
# flota.adauga_masini(masina_mea)
# flota.adauga_masini(masina_doi)
# flota.adauga_masini(masina_trei)
# flota.masina_scumpa()
# print(flota.masina_scumpa())



# TODO 4.Creati o clasa numita "Account" ca are 2 atribute: nume si sold si 2 metode: deposit si retragere. Ca si
#  cerita aditonala, retragerile nu pot fi mai mari decat soldul. Instantiati clasa, efectuati cateva operatiuni de
#  depunere si retragere si afisati soldul final, dar asigurati-va ca nu se pot efectua retrageri mai mari decat
#  soldul. Utilizati metoda __str__ pentru a afisa toate proprietatile obiectelor create. (eg. Contul lui Ion are 1000 lei)
# class Account:
#     def __init__(self,nume,sold):
#         self.nume=nume
#         self.sold=sold
#     def deposit(self,suma):
#         self.sold+=suma
#         print(f"{self.nume} a depus {suma} lei. Soldul actual este {self.sold} lei.")
#     def retragere(self,suma):
#         if suma>self.sold:
#             print(f"{suma} este mai mare decat soldul curent.")
#         else:
#             self.sold=self.sold-suma
#             print(f"{suma} a fost retrasa din cont. Soldul actual este de {self.sold} lei.")
#     def __str__(self):
#         return f"Contul lui {self.nume} are {self.sold} lei."
# contul_meu=Account("Maria",70000)
# print(contul_meu.deposit(50000))
# print(contul_meu.retragere(70000))

# TODO 4.1 Îmbunătățiți clasa Account pentru a include o verificare a parolei la fiecare depunere și retragere,
#  asigurându-vă că numai persoanele autorizate pot accesa fondurile. Adăugați de asemenea o metodă de schimbare a
#  parolei.Hint: Adăugați un atribut privat pentru a stoca parola și verificați parola înainte  de a efectua o operațiune.
# class Account:
#     def __init__(self, nume, sold, parola):
#         self.nume = nume
#         self.sold = sold
#         self.__parola = parola  # Atribut privat pentru a stoca parola
#
#     def verifica_parola(self, parola):
#         return self.__parola == parola
#
#     def deposit(self, suma, parola):
#         if self.verifica_parola(parola):
#             self.sold += suma
#             print(f"{self.nume} a depus {suma} lei. Soldul actual este {self.sold} lei.")
#         else:
#             print("Parolă incorectă! Depunerea nu a fost efectuată.")
#
#     def retragere(self, suma, parola):
#         if self.verifica_parola(parola):
#             if suma > self.sold:
#                 print(f"Retragere esuată! {self.nume} nu are suficienți bani în cont pentru a retrage {suma} lei. Soldul curent este {self.sold} lei.")
#             else:
#                 self.sold -= suma
#                 print(f"{self.nume} a retras {suma} lei. Soldul actual este {self.sold} lei.")
#         else:
#             print("Parolă incorectă! Retragerea nu a fost efectuată.")
#
#     def schimba_parola(self, parola_veche, parola_noua):
#         if self.verifica_parola(parola_veche):
#             self.__parola = parola_noua
#             print(f"Parola a fost schimbată cu succes pentru contul lui {self.nume}.")
#         else:
#             print("Parolă incorectă! Parola nu a fost schimbată.")
#
#     def __str__(self):
#         return f"Contul lui {self.nume} are {self.sold} lei."
#
# contul_meu = Account("Maria", 1000, "Maria2006")
# # contul_meu.deposit(500, "Maria2006")
# # contul_meu.retragere(300, "parola123")
# # contul_meu.retragere(1500, "Maria2006")
# contul_meu.schimba_parola("Maria2006", "nouaParola456")
# contul_meu.retragere(200, "nouaParola456")
# print(contul_meu)


# TODO 5. Creati o clasa numita "Student" care sa aiba ca proprietati nume, prenume, varsta, note (lista cu note).
#  Instantiati 3 obiecte de tipul Student. Utilizati metoda __str__ pentru a afisa toate proprietatile obiectelor
#  create.
#  Ca si cerinta aditionala, adaugati o metoda numita "medie" care sa calculeze media notelor si sa o returneze.
# class Student:
#     def __init__(self, nume, prenume, varsta, note):
#         self.nume = nume
#         self.prenume = prenume
#         self.varsta = varsta
#         self.note = note
#
#     def medie(self):
#         return sum(self.note) / len(self.note)
#
#     def __str__(self):
#         return (f"Student: {self.nume} {self.prenume}, Varsta: {self.varsta}, "
#                 f"Note: {self.note}, Media: {self.medie():.2f}")
# student1 = Student("Popescu", "Ion", 20, [8, 9, 10, 7])
# student2 = Student("Ionescu", "Maria", 22, [10, 10, 9, 10])
# student3 = Student("Georgescu", "Andrei", 19, [7, 8, 9, 8])



# print(student1)
# print(student2)
# print(student3)
# TODO 6.
#  1 . Creați o clasă numită Angajat cu următoarele atribute private:
#  nume: Numele complet al angajatului.
#  salariu: Salariul lunar al angajatului .
#  2 . Utilizați decoratorul @property pentru a crea un getter pentru fiecare atribut(nume și salariu)
#  3 . Utilizați decoratorul @<property_name>.setter pentru a crea un setter pentru fiecare atribut(nume și salariu)
#  În setter:
#   Asigurați-vă că nume nu este un șir gol sau None ("" sau None). Dacă este, printati mesajul "Numele nu poate fi gol".
#   Asigurați-vă că salariu este un număr pozitiv. Dacă nu este, printati mesajul "Salariul nu poate fi negativ".
#  4 . În metoda __str__ afișați un mesaj de forma "Angajatul <nume> are salariul <salariu> lei.".
#  5 Creați o instanță a clasei Angajat cu numele "Ion Popescu" și salariul 3000 lei.
#  6 . Accesați și modificați atributele instanței folosind getterele și setterele create.
#  7 . Bonus : creati delete-eri pentru atributul salariu

# class Angajat:
#     def __init__(self,nume,salariu):
#         self.__nume=nume
#         self.__salariu=salariu
#     @property
#     def nume(self):
#         return self.__nume
#     @property
#     def salariu(self):
#         return self.__salariu
#     @nume.setter
#     def nume(self,nume):
#         if nume=="" or nume is None:
#             print("Numele introdus nu poate fi gol.")
#         else:
#             self.__nume=nume
#
#     @salariu.setter
#     def salariu(self,salariu):
#         if salariu>0:
#             self.__salariu=salariu
#         else:
#             print("Salariul introdus trebuie sa fie mai mare decat 0.")
#
#     @salariu.deleter
#     def salariu(self):
#         del self.__salariu
#
#     def __str__(self):
#         return f"Angajatul {self.__nume} are salariul {self.__salariu} lei."
#
#
# angajat1=Angajat("Mihai Mario",25000)
# print(angajat1)
# print(f"Nume actual: {angajat1.nume}")
# angajat1.nume = "Maria Ionescu"
# print(f"Nume modificat: {angajat1.nume}")
# print(f"Salariu actual: {angajat1.salariu}")
# angajat1.salariu = 4000
# print(f"Salariu modificat: {angajat1.salariu}")
# del angajat1.salariu
# # print(angajat1)
# print(angajat1.__dict__)




# import datetime
# class Persoana:
#     def __init__(self,nume,prenume,anul_nasterii,ocupatie="student"):
#         self.nume=nume
#         self.prenume=prenume
#         self.anul_nasterii=anul_nasterii
#         self.ocupatie=ocupatie
#     def varsta(self):
#         anul_curent=datetime.datetime.now().year
#         return anul_curent-self.anul_nasterii
#     def descriere(self):
#         return f"Nume:{self.nume} Prenume:{self.prenume} Varsta:{self.varsta()} Ocupatie:{self.ocupatie}"
# eu=Persoana("Mihai","Mario",2005)
# print(eu.descriere())
# eu.ocupatie="sofer"
# print(eu.descriere())


# TODO 7. Creează o clasă PlaylistMuzical care să gestioneze o listă de melodii și să aibă metode pentru a adăuga, a scoate și a schimba ordinea melodiilor.
#  Presupunem că fiecare melodie este un dicționar ce conține numele și durata sa. Exemplu: {"nume": "melodie1", "durata": 3.5}.
#  Adaugati urmatoarele functionalitati pentru a extinde functionalitatea clasei "PLaylistMuzical":
#  0. Adaogă melodie: Adaugă o metodă care permite adăugarea unei melodii în playlist.
#  1. Caută melodie: Adaugă o metodă care permite căutarea unei melodii după nume și returnează poziția acesteia în playlist.
#  2. Redă melodie: Implementează o metodă care "redă" o melodie, afișând un mesaj că melodia respectivă se redă.
#  3. Număr de melodii: Adaugă o metodă care returnează numărul total de melodii din playlist.
#  4. Melodie aleatoare: Creează o metodă care selectează și redă o melodie la întâmplare din playlist.
#  5. Elimină după poziție: Adaugă o metodă pentru a elimina o melodie bazat pe poziția sa în playlist.
#  6. Curăță playlistul: Implementează o metodă pentru a goli întregul playlist.
#  7. Shuffle: Creează o metodă pentru a amesteca ordinea melodiilor din playlist.
#  8. Redă în ordine: Creează o metodă care redă melodiile în ordine, de la început până la sfârșit.
#  9. Redă invers: Adaugă o metodă pentru a reda melodiile în ordine inversă.
#  10. Lista de redare repetitivă: Implementează o opțiune care permite redarea repetitivă a playlistului.
#   Optional:
#  11. Durata totală a playlistului: Adaugă o metodă care calculează și returnează durata totală a playlistului, presupunând că fiecare melodie are o durată specificată.
#  12. Implementati o metoda de comparare a 2 playlisturi (Compară playlistul curent cu un alt playlist în funcție de durata totală) - hint: folositi metoda magica __gt__
#  14. Implementati conceptul de variabila privata in clasa PlaylistMuzical (hint: folositi decoratorul @property si setter pentru a seta valoarea variabilei private).
#  15. In constructorul clasei PlaylistMuzical, adaugati un atribut privat care reprezinta numele playlistului.
#  16. Implementati getter si setter pentru atributul privat nume_playlist( testati functionalitatea getterului si setterului accesand si modificand valoarea variabilei private nume_playlist).
# import random
# class PlaylistMuzical:
#     def __init__(self,nume="playlisy anonim"):
#         self.playlist=[]
#         self.__nume=nume
#     def adauga_melodie(self,melodie):
#         self.playlist.append(melodie)
#     def cauta_melodie(self,nume_melodie):
#         for index,melodie in enumerate(self.playlist):
#             if melodie["nume"]==nume_melodie:
#                 return f"Melodia a fost gasita la {index}."
#         else:
#             return ("Melodia nu a fost gasita.")
#     def reda_melodie(self,index):
#         if 0<=index<len(self.playlist):
#             print(f"Redare: {self.playlist[index]["nume"]}.")
#         else:
#             print("Melodia nu a fost gasita in playlist.")
#     def numar_melodii(self):
#         return len(self.playlist)
#     def melodie_aleatoare(self):
#         if self.playlist:
#             melodie_aleatorie=random.randint(0,len(self.playlist)-1)
#             self.reda_melodie(melodie_aleatorie)
#     def scoate_melodie(self,pozitie):
#         if 0<=pozitie<len(self.playlist):
#             melodie_eliminata = self.playlist.pop(pozitie)
#             print(f"Melodia '{melodie_eliminata}' a fost eliminată din playlist.")
#         else:
#             print("Poziție invalidă. Nu există melodie la această poziție.")
#     def curata_playlistul(self):
#         self.playlist.clear()
#         print("Playlistul a fost curățat.")
#     def amesteca_melodiile(self):
#         if self.playlist:
#             amesteca_melodii=random.shuffle(self.playlist)
#             self.redae_melodie(amesteca_melodii)
#     def reda_in_ordine(self):
#         for melodie in self.playlist:
#             print(f"Redare: {melodie['nume']}.")
#     def reda_in_ordine_inversa(self):
#         for melodie in reversed(self.playlist):
#             print(f"Redare: {melodie['nume']}.")
#     def redare_repetitiva(self,numar_redari):
#         for melodie in range(numar_redari):
#             self.reda_in_ordine()
#     def durata_playlist(self):
#         return f"Durata totala: {sum(melodie["durata"] for melodie in self.playlist)}"
#     def __gt__(self,other):
#         return self.durata_playlist() > other.durata_playlist()
#     @property
#     def nume(self):
#         return self.__nume
#     @nume.setter
#     def nume(self,nume):
#         if nume=="" or nume==None:
#             print("Nu a fost gasita nici o melodie.")
#         else:
#             self.__nume=nume
# #Cream o instanta a clasei
# playlist1=PlaylistMuzical(nume="playlist 1")
# print(playlist1.playlist)
# #adaugam melodii
# melodie1={"nume":"melodie1","durata":5.3}
# melodie2={"nume":"melodie2","durata":1.4}
# melodie3={"nume":"melodie3","durata":2.9}
# playlist1.adauga_melodie(melodie1)
# playlist1.adauga_melodie(melodie2)
# print(playlist1.playlist)
# #scoatem o melodie
# playlist1.scoate_melodie(1)
# playlist1.adauga_melodie(melodie2)
# playlist1.adauga_melodie(melodie3)
#
# print(playlist1.playlist)
# #cautam o melodie
# print(playlist1.cauta_melodie("melodie1"))
# #redarea melodiei
# playlist1.reda_melodie(1)
# #numar melodii
# print(playlist1.numar_melodii())
# #melodie aleatoare
# print(playlist1.melodie_aleatoare())
# #curata playlistu
# # playlist1.curata_playlistul()
# # print(playlist1.playlist)
# playlist1.reda_in_ordine()
# playlist1.reda_in_ordine_inversa()
# print(playlist1.redare_repetitiva(3))
# print(playlist1.durata_playlist())
# playlist2=PlaylistMuzical(nume="playlist 2")
# melodie4={"nume":"melodie4","durata":4.2}
# melodie5={"nume":"melodie5","durata":1.2}
# melodie6={"nume":"melodie6","durata":3.3}
# print(playlist1>playlist2)
# print(playlist1.nume)
# playlist1.nume="alt nume"
# print(playlist1.nume)

# print(float(1))

#  TODO 1. Creati o clasa Vehicul astfel incat, 'Exemplu de utilizare a clasei Vehicul sa functioneze':
#   Se creează o clasă Vehicul cu atribute pentru marca, model și anul fabricației.
#   Adaugăm o metodă care returnează vârsta vehiculului în ani.Hint: folositi modulul datetime
# import datetime
# class Vehicul:
#     def __init__(self,marca,model,an):
#         self.marca=marca
#         self.model=model
#         self.an=an
#     def varsta_vehicul(self):
#         an_curent=datetime.datetime.now().year
#         varsta=an_curent-self.an
#         return varsta
# vehicul_1=Vehicul("Ford","Mustang",2017)
# print(vehicul_1.varsta_vehicul())
# # Exemplu de utilizare a clasei Vehicul
# vehicul = Vehicul('Ford', 'Mustang', 1967)
# varsta_vehicul = vehicul.varsta()
# print(varsta_vehicul)

#  TODO 1.1 Adaugati in clasa Vehicul astfel încât să includă o metodă care determină dacă vehiculul este considerat
#   un vehicul clasic (vârsta mai mare de 30 de ani). De asemenea, adăugați o metodă care returnează un șir de
#   caractere formatat, care să includă și informația dacă vehiculul este clasic.
# import datetime
# class Vehicul:
#     def __init__(self,marca,model,an):
#         self.marca=marca
#         self.model=model
#         self.an=an
#     def varsta_vehicul(self):
#         an_curent=datetime.datetime.now().year
#         varsta=an_curent-self.an
#         return varsta
#     def vehicul_clasic(self):
#         return self.varsta_vehicul()>30
#     def descriere(self):
#         clasic="clasic" if self.vehicul_clasic() else "nonclasic"
#         return f"Vehiculul {self.marca} {self.model} din anul {self.an} este un vehicul {clasic}"
# vehicul_1=Vehicul("Ford","Mustang",1917)
# print(vehicul_1.varsta_vehicul())
# print(vehicul_1.descriere())
# Exemplu de utilizare a clasei Vehicul
# TODO 2. Creati o clasă MasinaUnu în Python care să îndeplinească următoarele cerințe:
#  Clasa trebuie să aibă un constructor __init__ care să accepte trei argumente: marca, culoare, și an_fabricatie.
#  Fiecare dintre aceste argumente ar trebui să aibă o valoare implicită, respectiv 'Audi' pentru marca, 'verde' pentru culoare și 1990 pentru anul fabricației.
#  Definește o metodă descriere care returnează un șir de caractere ce descrie mașina folosind atributele sale, în formatul: "Masina este un [marca] din anul [an_fabricatie], de culoare [culoare]."
#   Creați o instanță a clasei Masina folosind valorile implicite și afișați descrierea acesteia folosind metoda magica __str__.
#   Creați o instanță a clasei Masina cu marca 'BMW', culoarea 'albastru' și anul fabricației 2020, și afișați descrierea acesteia.
# class MasinaUnu:
#     def __init__(self,marca="Audi",culoare="Alba",an_fabricatie=1990):
#         self.marca=marca
#         self.culoare=culoare
#         self.an_fabricatie=an_fabricatie
#     def descriere(self):


# TODO 2.1 Modificați clasa MasinaUnu pentru a include un atribut este_electrica, cu valoarea implicită False.
#  Adăugați logica necesară astfel încât metoda descriere să includă și informația despre propulsia mașinii (
#  electrică sau convențională).
# class MasinaUnu:
#     def __init__(self,marca="Audi",culoare="Alba",an_fabricatie=1990,este_electrica=False):
#         self.marca=marca
#         self.culoare=culoare
#         self.an_fabricatie=an_fabricatie
#         self.este_electrica=este_electrica
#     def descriere(self):
#         if self.este_electrica:
#             combustibil="Electrica"
#         else:
#             combustibil="Petrol"
#         return f"{self.marca} {self.culoare} {combustibil}"
# vehicul=MasinaUnu()
# print(vehicul.descriere())



# TODO 3. Creati o clasa numita "MasinaDoi" care sa aiba ca proprietati marca, model, an fabricatie, culoare,
#  pret. Instantiati 3 obiecte de tipul Masina. Utilizati metoda __str__ pentru a afisa toate proprietatile
#  obiectelor create(eg. Audi A4 din 2019, culoare neagra, pret 20000 euro).

# class MasinaDoi:
#     def __init__(self,marca,model,an_fabricatie,culoare,pret):
#         self.marca=marca
#         self.model=model
#         self.an_fabricatie=an_fabricatie
#         self.culoare=culoare
#         self.pret=pret
#     def __str__(self):
#         return f"{self.marca} {self.model} din anul {self.an_fabricatie}, culoare {self.culoare}, pret {self.pret} euro"
# vehicul1=MasinaDoi("Audi","A4",2019,"neagra",20000)
# vehicul2=MasinaDoi("Audi","A5",2020,"alba",39090)
# vehicul3=MasinaDoi("BMW","M4",2023,"gri",90000)
# print(vehicul1)
# print(vehicul2)
# print(vehicul3)

# TODO 3.1  Implementați o clasă FlotaAuto care să gestioneze un set de obiecte MasinaDoi. Clasa ar trebui să permită
#  adăugarea și ștergerea mașinilor din flotă și să ofere o metodă pentru a afișa cea mai scumpă mașină din flotă.
#   Hint. In constructorul Clasei Flota nu oferiti atribute la instanta clasei, ci doar initializati un atribut gol

# class FlotaAuto:
#     def __init__(self):
#         self.flota=[]
#     def adaugare_masini(self,masina):
#         self.flota.append(masina)
#     def stergere_masini(self,masina):
#         self.flota.remove(masina)
#     def masina_scumpa(self):
#         if not self.flota:
#             return "flota este goala"
#         masina_scumpa=self.flota[0]
#         for masina in self.flota[1:]:
#             if masina.pret>masina_scumpa.pret:
#                 masina_scumpa=masina
#         return f"Cea mai scumpa masina din flota este urmatoarea: {masina_scumpa}"
#
# flota=FlotaAuto()
# flota.adaugare_masini(vehicul1)
# flota.adaugare_masini(vehicul2)
# flota.adaugare_masini(vehicul3)
# print(flota.masina_scumpa())


# TODO 4.Creati o clasa numita "Account" ca are 2 atribute: nume si sold si 2 metode: deposit si retragere. Ca si
#  cerita aditonala, retragerile nu pot fi mai mari decat soldul. Instantiati clasa, efectuati cateva operatiuni de
#  depunere si retragere si afisati soldul final, dar asigurati-va ca nu se pot efectua retrageri mai mari decat
#  soldul. Utilizati metoda __str__ pentru a afisa toate proprietatile obiectelor create. (eg. Contul lui Ion are 1000 lei)
# class Accout:
#     def __init__(self,nume,sold):
#         self.nume=nume
#         self.sold=sold
#     def depositare(self,suma):
#         self.sold+=suma
#         return f"A fost depozitata suma de {suma},soldul curent este {self.sold}"
#     def retragere(self,suma):
#         if self.sold<suma:
#             return f"Fonduri insuficiente!"
#         else:
#             self.sold-=suma
#             return f"A fost retrasa suma de {suma},soldul curent este {self.sold}"
#     def __str__(self):
#         return f"Contul lui {self.nume} are {self.sold} lei"
# persoana=Accout("Mario",20000)
# print(persoana.depositare(100000))
# print(persoana.retragere(40000))

# TODO 4.1 Îmbunătățiți clasa Account pentru a include o verificare a parolei la fiecare depunere și retragere,
#  asigurându-vă că numai persoanele autorizate pot accesa fondurile. Adăugați de asemenea o metodă de schimbare a
#  parolei.Hint: Adăugați un atribut privat pentru a stoca parola și verificați parola înainte  de a efectua o operațiune.
# class Accout:
#     def __init__(self,nume,sold,parola):
#         self.nume=nume
#         self.sold=sold
#         self.__parola=parola
#     def verificare_parola(self,parola):
#         return self.__parola == parola
#     def depositare(self,suma,parola):
#         if self.verificare_parola(parola):
#             self.sold += suma
#             return f"A fost depozitata suma de {suma},soldul curent este {self.sold}"
#         else:
#             return "Parola introdusa este incorecta!"
#
#     def retragere(self,suma,parola):
#         if self.verificare_parola(parola):
#             if self.sold < suma:
#                 return f"Fonduri insuficiente!"
#             else:
#                 self.sold -= suma
#                 return f"A fost retrasa suma de {suma},soldul curent este {self.sold}"
#         else:
#             return "Parola introdusa este incorecta!"
#     def schimbare_parola(self,parola_veche,parola_noua):
#         if self.verificare_parola(parola_veche):
#             self.__parola=parola_noua
#     def __str__(self):
#         return f"Contul lui {self.nume} are {self.sold} lei"
# persoana=Accout("Mario",20000,"Mario2005")
# print(persoana.depositare(100000,"Mario2005"))
# print(persoana.retragere(40000,"Mario2005"))
# persoana.schimbare_parola("Mario2005","Maria2006")
# print(persoana.retragere(40000,"Maria2006"))
# TODO 5. Creati o clasa numita "Student" care sa aiba ca proprietati nume, prenume, varsta, note (lista cu note).
#  Instantiati 3 obiecte de tipul Student. Utilizati metoda __str__ pentru a afisa toate proprietatile obiectelor
#  create.
#  Ca si cerinta aditionala, adaugati o metoda numita "medie" care sa calculeze media notelor si sa o returneze.
# class Student:
#     def __init__(self,nume,prenume,varsta,note):
#         self.nume=nume
#         self.prenume=prenume
#         self.varsta=varsta
#         self.note=note
#     def media_notelor(self):
#         return sum(self.note)/len(self.note)
#     def __str__(self):
#         return f"Elevul {self.nume} {self.prenume} cu varsta de {self.varsta} ani, are media {self.media_notelor():.2f}"
# elev_1=Student("Mihai","Maria",19,[10,9,9,10,10])
# elev_2=Student("Raducanu","Maria",18,[10,10,10,10,9])
# elev_3=Student("Mihai","Mario",19,[10,8,10,10,10])
# print(elev_1)
# print(elev_2)
# print(elev_3)
# TODO 6.
#  1 . Creați o clasă numită Angajat cu următoarele atribute private:
#  nume: Numele complet al angajatului.
#  salariu: Salariul lunar al angajatului .
#  2 . Utilizați decoratorul @property pentru a crea un getter pentru fiecare atribut(nume și salariu)
#  3 . Utilizați decoratorul @<property_name>.setter pentru a crea un setter pentru fiecare atribut(nume și salariu)
#  În setter:
#   Asigurați-vă că nume nu este un șir gol sau None ("" sau None). Dacă este, printati mesajul "Numele nu poate fi gol".
#   Asigurați-vă că salariu este un număr pozitiv. Dacă nu este, printati mesajul "Salariul nu poate fi negativ".
#  4 . În metoda __str__ afișați un mesaj de forma "Angajatul <nume> are salariul <salariu> lei.".
#  5 Creați o instanță a clasei Angajat cu numele "Ion Popescu" și salariul 3000 lei.
#  6 . Accesați și modificați atributele instanței folosind getterele și setterele create.
#  7 . Bonus : creati delete-eri pentru atributul salariu
# class Angajat:
#     def __init__(self,nume,salariu):
#         self.__nume=nume
#         self.__salariu=salariu
#     @property
#     def nume(self):
#         return self.__nume
#     @property
#     def salariu(self):
#         return self.__salariu
#     @nume.setter
#     def nume(self,nume):
#         if nume==" " or nume is None:
#             return "Numele nu poate fi gol"
#         else:
#             self.__nume=nume
#     @salariu.setter
#     def salariu(self,salariu):
#         if salariu <= 0:
#             return "Salariul trebuie sa fie mai mare decat 0"
#         else:
#             self.__salariu=salariu
#     def __str__(self):
#         return f"Angajatul {self.nume} are salariul {self.salariu} lei."
#     @salariu.deleter
#     def salariu(self):
#         del self.__salariu
#
#
# angajat1 = Angajat("Mihai Mario", 25000)
# print(angajat1)
# print(angajat1.salariu)

#
# TODO: Creează o clasă "Biblioteca" care să gestioneze o colecție de cărți și să aibă metode pentru a adăuga, a elimina și a căuta cărți.
#
# Fiecare carte este reprezentată printr-un dicționar care conține următoarele informații: titlu, autor și număr de pagini. Exemplu: {"titlu": "carte1", "autor": "autor1", "pagini": 250}.
#
# Extinde funcționalitatea clasei "Biblioteca" cu următoarele cerințe:
#
# 1.Adaugă carte: Creează o metodă care permite adăugarea unei cărți în bibliotecă.
# 2.Caută carte: Implementează o metodă care permite căutarea unei cărți după titlu și returnează poziția acesteia în colecție.
# 3.Detalii carte: Creează o metodă care afișează detalii despre o carte (titlu, autor, număr de pagini) pe baza titlului.
# 4.Număr de cărți: Adaugă o metodă care returnează numărul total de cărți din bibliotecă.
# 5.Elimină carte: Creează o metodă pentru a elimina o carte bazată pe poziția sa în colecție.
# 6.Listă de cărți: Implementează o metodă care afișează toate cărțile din bibliotecă, împreună cu autorii și numărul de pagini.
# 7.Curăță biblioteca: Adaugă o metodă care golește întreaga bibliotecă.
# 8.Afișează cărțile după autor: Creează o metodă care afișează toate cărțile scrise de un anumit autor.
# 9.Sortează cărțile după titlu: Implementează o metodă care sortează cărțile în ordine alfabetică după titlu.
# 10.Sortează cărțile după număr de pagini: Creează o metodă care sortează cărțile în funcție de numărul de pagini (crescător).
# 11.Compară două biblioteci: Adaugă o metodă care compară două biblioteci în funcție de numărul total de pagini.
# 12Durata totală de citit: Creează o metodă care calculează timpul total necesar pentru a citi toate cărțile din bibliotecă, presupunând că o persoană citește 30 de pagini pe oră.
# 13.Variabilă privată pentru numele bibliotecii: În constructorul clasei "Biblioteca", adaugă un atribut privat care reprezintă numele bibliotecii și implementează getter și setter pentru acesta (hint: folosește decoratorul @property).
# 14.Comparare după numărul de cărți: Implementează o metodă de comparare între două biblioteci în funcție de numărul de cărți (hint: folosește metoda magică __lt__).

# class Biblioteca:
#     def __init__(self):
#         self.biblioteca=[]
#     def adauga_carte(self,carte):
#         return self.biblioteca.append(carte)
#     def cauta_carte(self,nume_carte):
#         for index,carte in enumerate(self.biblioteca):
#             if carte["titlu"]==nume_carte:
#                 return f"Cartea a fost gasita pe pozitia {index}"
#         else:
#             return "Cartea nu a fost gasita."
#     def detalii_carte(self,nume_carte):
#             if self.cauta_carte(nume_carte):
#                 print(f"Titlu: {carte1['titlu']}, Autor: {carte1['autor']}, Pagini: {carte1['numar pagini']}")
#             else:
#                 print("Cartea nu a fost gasita.")
#     def numar_carti(self):
#         return len(self.biblioteca)
#     def elimina_carte(self,pozitie):
#         if 0<=pozitie<len(self.biblioteca):
#             del self.biblioteca[pozitie]
#         else:
#             print("pozitie invalida.")
#     def lista_carti(self):
#         if self.biblioteca:
#             for carte in self.biblioteca:
#                 print(f"Titlu: {carte['titlu']}, Autor: {carte['autor']}, Pagini: {carte['numar pagini']}")
#         else:
#             print("Cartea nu a fost gasita.")
#     def carti_autor(self):



# librarie=Biblioteca()
# carte1={"titlu":"Tom Gates","autor":"Jone Stone","numar pagini":745}
# carte2={"titlu":"Lebada Albastra","autor":"Jone Cena","numar pagini":445}
# librarie.adauga_carte(carte1)
# librarie.adauga_carte(carte2)
# print(librarie.cauta_carte("Tom Gates"))
# librarie.detalii_carte("Tom Gates")
# librarie.lista_carti()

# Creează o clasă numită Book care are trei atribute: title (titlu), author (autor) și pages (număr de pagini).
# Include o metodă read_pages(num) care crește un contor intern de pagini citite.
# Asigură-te că numărul total de pagini citite nu poate depăși numărul total de pagini al cărții.
# Folosește metoda __str__ pentru a afișa titlul cărții, autorul și numărul de pagini citite.
# Creează mai multe instanțe și simulează citirea unor pagini.

# class Book:
#     def __init__(self,titlu,autor,numar_pagini):
#         self.titlu=titlu
#         self.autor=autor
#         self.numar_pagini=numar_pagini
#         self.pagini_citite=0
#     def read_pages(self,num):
#         if self.pagini_citite>self.numar_pagini:
#             print("Numarul de pagini citite...")
#         else:
#             self.pagini_citite+=num
#
#     def __str__(self):
#         return f"{self.titlu} de {self.autor}, Pagini citite: {self.pagini_citite}/{self.numar_pagini}"

# Creează o clasă numită Student care are trei atribute: name (nume), age (vârstă) și grades (note).
# Include două metode: add_grade(grade) pentru a adăuga o notă la listă și average_grade() pentru a calcula media notelor.
# Utilizează metoda __str__ pentru a afișa numele, vârsta și media notelor.
# Creează câțiva studenți și adaugă note, apoi afișează media pentru fiecare student.

# class Student:
#     def __init__(self,nume,varsta):
#         self.nume=nume
#         self.varsta=varsta
#         self.note=[]
#     def adauga_note(self,note):
#         self.note.append(note)
#     def average_grade(self):
#         return sum(self.note)/len(self.note)
# student1=Student("Mario",19)
# student1.adauga_note(10)
# student1.adauga_note(10)
# student1.adauga_note(10)
# student1.adauga_note(10)
# student1.adauga_note(7)
# print(student1.note)
# print(student1.average_grade())


# Creează o clasă numită Library care are un atribut books (o listă de cărți).
# Include metodele add_book(book) pentru a adăuga o carte la bibliotecă, remove_book(book) pentru a șterge o carte,
# și find_book(title) pentru a căuta o carte după titlu. Folosește metoda __str__ pentru a afișa toate cărțile din bibliotecă.
# Creează o bibliotecă, adaugă și elimină cărți, și testează căutarea unei cărți.

# class Library:
#     def __init__(self):
#         self.books=[]
#     def add_book(self,book):
#         self.books.append(book)
#     def remove_book(self,book):
#         self.books.remove(book)
#     def gaseste_carte(self,titlu):
#         for index,carte in enumerate(self.books):
#             if carte["titlu"]==titlu:
#                 return f"Cartea a fost gasita la indexul {index}"
#         else:
#             return f"Cartea non fost gasita."
# colectie=Library()
# carte1={"titlu":"Tom Gates","autor":"Jone Stone","numar pagini":745}
# carte2={"titlu":"Lebada Albastra","autor":"Jone Cena","numar pagini":445}
# colectie.add_book(carte1)
# colectie.add_book(carte2)
# print(colectie.gaseste_carte("Lebada Albastra"))

# # Exercițiul 1: Crearea și importarea unui modul simplu
# # Pasul 1: Creează un fișier math_util.py care să conțină funcții de bază pentru adunare și scădere.
# # Pasul 2: Într-un alt fișier main.py, importă și folosește funcțiile din math_util.py.
# # Exercițiul 2: Crearea unui modul cu variabile și funcții
# # Pasul 1: Creează un fișier greetings.py care să conțină o variabilă și o funcție pentru afișarea unui mesaj.
# # Pasul 2: În main.py, importă greetings.py și folosește conținutul său.
# # Exercițiul 3: Importarea specifică a funcțiilor dintr-un modul
# # Pasul 1: Creează un fișier math_operations.py care conține mai multe funcții matematice.
# # Pasul 2: În main.py, importă doar funcția inmultire și folosește-o.
# Exercițiul 4: Crearea unui pachet cu module multiple
# Pasul 1: Creează un director calculations/ cu fișierele __init__.py, add.py, și multiply.py.
# # Pasul 2: În main.py, importă și folosește funcțiile din pachetul calculations.
# # Exercițiul 5: Utilizarea unui modul cu importuri din alte module
# # Pasul 1: Creează un fișier geometry.py care să folosească funcții din math_util.py pentru a calcula aria unui dreptunghi.

#  TODO 1.1 Adaugati in clasa Vehicul astfel încât să includă o metodă care determină dacă vehiculul este considerat
#   un vehicul clasic (vârsta mai mare de 30 de ani). De asemenea, adăugați o metodă care returnează un șir de
#   caractere formatat, care să includă și informația dacă vehiculul este clasic.

# 1.Sa facem o aplicatie in care sa ne calculeze nota, si sa ne afiseze toate produsele pe care le-am cumparat, cantitatea
# si pretul lor. La final sa afiseze totalul.
#nota = pret_produs1 * nr_produs1 + pret_prod2 * nr_prod2 + ... + pret_prodn * nr_prodn

# def adaugare_produse():
#     lista_nume_prod = []
#     lista_pret_prod = []
#     lista_cantitate_prod = []
#     while True:
#         while True:
#             nume = input("Introduceti numele produsului: ").strip()
#             if not nume:
#                 print("Numele produsului nu poate fi gol. Va rugam sa introduceti un nume valid.")
#             elif nume in lista_nume_prod:
#                 print("Acest produs a fost deja introdus. Va rugam sa introduceti un alt nume.")
#             else:
#                 break
#         pret = input("Introduceti pretul: ")
#         while not pret.isdigit():
#             print("Valoarea introdusa este invalida.")
#             pret = input("Introduceti pretul: ")
#         pret=int(pret)
#         cantitate = input("Introduceti cantitatea: ")
#         while not cantitate.isdigit():
#             print("Valoarea introdusa este invalida.")
#             cantitate = input("Introduceti cantitatea: ")
#         cantitate = int(cantitate)
#         lista_nume_prod.append(nume)
#         lista_pret_prod.append(pret)
#         lista_cantitate_prod.append(cantitate)
#         conditie = input("Daca vreti sa incheiati cumparaturile apasati tasta X: ")
#         if conditie.upper() == "X":
#             break
#     return lista_nume_prod, lista_pret_prod, lista_cantitate_prod
# def calculare_nota(pret,cantitate):
#     total=0
#     for index in range(len(pret)):
#         total+=pret[index]*cantitate[index]
#     return total
#
# def afisare_nota():
#     nume,pret,cantitate = adaugare_produse()
#     total=calculare_nota(pret,cantitate)
#     for index in range(len(nume)):
#         print(f"{nume[index]} {pret[index]} lei * {cantitate[index]}")
#     # print()
#     print(f"\nTotal de plata:{total}")
#
# afisare_nota()

# my_var=100
# my_list=[1,2,3,4,0,5,"6"]
# for element in my_list:
                           # #     if element==0:
                           # #         continue
                           # #     else:
                           # #         rezultat= my_var / element
                           # #         print(rezultat)
#     try:
#         rezultat = my_var / element
#     except ZeroDivisionError:
#         print("...")
#     except TypeError:
#         print("..........")
#     else:
#         print(rezultat)

# TODO 1. Trateaza exceptia generata de codul de mai jos folosing blocuri try-except.
# for i in ['a','b','c']:
#     print(i**2)

# TODO 2. Scrie o functie care cere un numar intreg de la tastatura si returneaza patratul acestuia.
#  Foloseste un while loop cu un try, except, else block pentru a verifica inputul de la tastatura.

# TODO 3.: Creați o listă cu 5 elemente și apoi încercați să accesați un element de la
#  indexul 10. Gestionati eroarea IndexError pentru a afișa un mesaj corespunzător. Optional : Afisati lungimea
#  listei in mesajul de eroare.

# TODO 4. Creați un dicționar cu 3 elemente și apoi încercați să accesați o cheie care nu
#  există în dicționar. Gestionati eroarea KeyError pentru a afișa un mesaj corespunzător. Optional : Afisati cheile
#  din dictionar in mesajul de eroare.

# TODO 5.: Scrieți un program care solicită utilizatorului să introducă un număr și
#  încercați să îl convertească într-un întreg folosind int(). Gestionati exceptia ValueError care poate apărea dacă
#  utilizatorul introduce un text în loc de număr. Afișați un mesaj corespunzător în cazul în care apare o excepție.

# TODO 6 Exercițiu cu ZeroDivisionError : Creați un program care primește de la tastatură două numere întregi și
#  împarte primul număr la al doilea. Gestionati eroarea ZeroDivisionError pentru a afișa un mesaj corespunzător în
#  cazul în care utilizatorul introduce 0 ca al doilea număr.

# for i in ['a','b','c']:
#     try:
#         print(i**2)
#     except TypeError:
#         print('Nu se poate ridica la o putere un string.')

# def numar_tastatura():
#     while True:
#         try:
#             numar = int(input("Introduceti un numar: "))
#         except ValueError:
#             print("Eroare! Nu ai introdus un numar intreg")
#         except TypeError:
#             print("Eroare! Incearca iar.")
#         else:
#             print(f"Patratul numarului {numar} este: {numar**2}")
#             break
#
# numar_tastatura()

# def acceseaza_lista(parametru):
#     try:
#         index=int(input("Introduceti indexul pe care doriti sa-l accesati: "))
#     except IndexError:
#         print(f"Eroare. Introduceti un index care se afla in lungimea listei.Lungimea listei este {len(parametru)}")
#     else:
#         print(f"Elementul de la indexul introdus {index} este {parametru[index]}")
# acceseaza_lista([1,2,3,4,5])

# def acceseaza_dictionar():
#     dictionar={"nume":"Mario","varsta":19,"oras":"Bucuresti"}
#     try:
#         cheie=input("Introduceti cheia pe care doriti sa o accesati: ")
#         valoare = dictionar[cheie]
#     except KeyError:
#         print(f"Eroare. Cheia {cheie} nu exista in dictionar. Cheile din dictionar sunt: {dictionar.keys()}")
#     else:
#         print(f"Valoarea pentru cheia {cheie} este: {valoare}")
# acceseaza_dictionar()

# def solicita_numar():
#     try:
#         numar=int(input("Introduceti un numar: "))
#     except ValueError:
#         print("Eroare.Ati introdus un text sau un numar invalid.")
#     else:
#         print(f"Ati introdus numarul: {numar}")
#
# solicita_numar()

# def imparte_numere():
#     try:
#         numarul1=int(input("Introduceti un numar: "))
#         numarul2 = int(input("Introduceti un numar: "))
#         rezultat=numarul1 / numarul2
#     except ZeroDivisionError:
#         print("Eroare. Impartirea la 0 nu se poate efectua.")
#     else:
#         print(f"Rezultatul impartirii numerelor: {numarul1} si {numarul2} este {rezultat}")
# imparte_numere()

# TODO 7. Exercitiu cu FileNotFoundError: Creați o funcție numită citeste_fisier(nume_fisier) care primește numele
#  unui fișier și încearcă să deschidă și să citească fișierul. Gestionati excepția FileNotFoundError și afișați un
#  mesaj corespunzător dacă fișierul nu există.

# TODO 8. Exercițiu cu AssertionError: Creați o funcție numită verifica_numar(numar) care primește un număr întreg și
#  verifică dacă numărul este mai mare decât 10.

# TODO 9. Exercițiu cu NameError: Creați o funcție numită afiseaza_variabila(). In cadrul functiei incercati sa accesati si sa afisati o variabila numita
#  "variabila_nedefinita" care nu a fost definita anterior. Utilizati un bloc try-except pentru a gestiona exceptia NameError si afisati un mesaj corespunzator.

# def citeste_fisier(nume_fisier):
#     try:
#         with open(nume_fisier,"r") as f:
#             continut=f.read()
#     except FileNotFoundError:
#         print(f"Eroare. Fisierul {nume_fisier} nu a fost gasit.")
#     else:
#         print(f"Continutul fisierului {nume_fisier}:{continut}")
# citeste_fisier("fisier_python.txt")

# def verifica_numar(numar):
#     try:
#         assert numar>10
#     except AssertionError:
#         print(f"Eroare. Numarul {numar} nu este mai mare decat 10.")
#     else:
#         print(f"Numarul {numar} este valid.")
# verifica_numar(-12)

# def afiseaza_variabila():
#     try:
#         print(variabila_nedefinita)
#     except NameError:
#         print("Eroare. Variabila nu a fost definita.")
# afiseaza_variabila()

# TODO 1. Exercițiu cu raise: Creati o functie care primeste un numar si utilizeaza o declaratie 'if' pentru a
#  verifica daca numarul este pozitiv. Daca numarul nu este pozitiv, aruncati o exceptie personalizata folosind
#  'raise', cu un mesaj corespunzator.Altfel calculeaza si returneaza radicalul numarului.

# import math
# def radical(numar):
#     if numar<=0:
#         raise ValueError("Numarul nu este pozitiv.")
#     return math.sqrt(numar)
# print(radical(0))

# TODO 2. Exercițiu cu raise: Creati o functie care sa primeasca un text de la utilizator si sa atunce o exceptie
#  'TypeError' daca textul nu este un sir de caractere.

# def sir_caractere(text):
#     if not isinstance(text,str):
#         raise TypeError("Textul trebuie sa fie un sir de caractere string.")
#     return text
# print(sir_caractere("43"))

# TODO 3. Exercitiu cu raise:. Creați o funcție care primește o listă și un index și returnează elementul de la
#  indexul specificat. Dacă indexul este în afara intervalului valid al listei, aruncați o excepție IndexError.

# def returneaza_index(lista,index):
#     if index>=len(lista) or index<0:
#         raise IndexError("Index-ul nu se afla in range-ul listei")
#     return lista[index]
# print(returneaza_index([1,2,3,4,5,6],6))

# TRY, EXCEPT, ELSE, FINALLY

# TODO 1. Exercițiu cu try, except: Creati o functie unde un utilizator introduce un sir de caractere care ar trebui
#  sa fie un numar. Utilizati 'try' pentru a incerca sa convertiti sirul de caractere in numar de tip intreg (int()).
#  Daca conversia nu se poate efectua, utilizam blocul except pentru a afisa un mesaj de eroare

# def convertire_sir_caractere():
#     try:
#         numar=int(input("Introduceti un numar: "))
#     except ValueError:
#         print("Valoarea introdusa trebuie sa fie un int.")
#     else:
#         print(f"Numarul introdus este {numar}")
# convertire_sir_caractere()
# TODO 2. Exercițiu cu try, except, else: Creati un program/functie unde utilizatorul introduce un numar. Utilizati
#  'try' oentru a incerca impartirea la 10 a numarului introdus de utilizator. Daca numarul este 0 sau apare orice
#  alta exceptie, se utilizeaza blocul 'except' si se afiseaza un mesaj de eroare. Daca nu apare nicio exceptie,
#  se utilizeaza blocul 'else' pentru a afisa rezultatul impartirii la 10.

# def impartire(numar1):
#     try:
#         numar2=10
#         rezultat=numar1/numar2
#     except ZeroDivisionError:
#         print("Numarul introdus nu poate fi 0")
#     except TypeError:
#         print("Numarul treguie sa fie un int")
#     else:
#         print(f"Impartirea numerelor {numar1} si {numar2} este egala cu {rezultat}")
# impartire(0)

# TODO 3. Exercițiu cu try, except,finally: Creati un program/functie pentru deschierea unui fisier pentru citire.
#  Daca fisierul nu exista sau apare o alta exceptie, se utilizeaza blocul 'except' pentru a afisa un mesaj de eroare.
#  Indiferent de rezultatul blocului 'try', se utilizeaza blocul 'finally' pentru a inchide fisierul.

# def deschidere_fisier(nume_fisier):
#     try:
#         fisier=open(nume_fisier,"r")
#         continut=fisier.read()
#     except FileNotFoundError:
#         print("Fisierul nu a putut fi gasit!")
#     else:
#         print("Fisierul a fost gasit!")
#     finally:
#         try:
#             fisier.close()
#             print("Fisierul a fost inchis.")
#         except NameError:
#             print("Nu a fost deschis niciun fisier.")
# deschidere_fisier("requirements.txt")

# TODO 4. Exercițiu cu try, except, else : Creati o lista de elemente unde vom dori sa cautam un element specific.
#  Utilizam 'try' pentru a incerca sa cautam elementul in lista. Daca elementul nu este gasit, se utilizeaza blocul
#  'except' pentru a afisa un mesaj de eroare. In cazul in care elementul este gasit sau nu apare nicio exceptie,
#  se utilizeaza blocul 'else' pentru a afisa un mesaj corespunzator.

# def cautam_element(lista,element):
#     try:
#         index=lista.index(element)
#         print(index)
#     except ValueError:
#         print("Elementul nu se afla in lista.")
#     else:
#         print(f"Elementul a fost gasit in lista la indexul {index}.")
# cautam_element([1,2,3,4,5,6,7,8],7)

# TODO 5. Citirea și Scrierea în Fișiere
#  Încercați să deschideți un fișier pentru citire. Dacă fișierul nu există, creați-l și scrieți un mesaj în el.
# def deschidere_fisier(nume_fisier):
#     try:
#         fisier=open(nume_fisier,'r')

# TODO 6.Verificați dacă elementul cerut de utilizator este într-o listă. Dacă indexul este în afara intervalului, afișați un mesaj de eroare.

# TODO 7. Încercați să extrageți o valoare dintr-un dicționar folosind o cheie. Dacă cheia nu există, afișați un mesaj de eroare.

# TODO 1. **Funcții Lambda:**
#   - Scrie o funcție lambda care ridică un număr la pătrat.(a = 2 -> output = 4)
#   - Scrie o funcție lambda care returnează lungimea unui șir de caractere.(string = "abc" -> output = 3)
#   - Scrie o funcție lambda care inversează un șir de caractere.(string = "abc" -> output = "cba")


# print((lambda x:x**2)(2))

# lungime_sir=lambda x: len(x)
# print(lungime_sir("Mario scrie."))
#
# inversare=lambda x: x[::-1]
# print(inversare("Mario scrie."))

# TODO 2. **map:**
#   - Folosind `map` și o funcție lambda, transformă o listă de numere întregi într-o listă de string-uri.(input = [1, 2, 3] -> output = ["1", "2", "3"])
#   - Transformă o listă de cuvinte într-o listă care conține lungimile fiecărui cuvânt.(input = ["abc", "abcd", "abcde"] -> output = [3, 4, 5])

# lista=[1,2,3,4,5,6]
# print(list(map(lambda x: str(x),lista)))

# TODO 3. **reduce:**
#   - Folosește `reduce` pentru a determina cel mai lung cuvânt dintr-o listă de cuvinte. (input = ["abc", "abcd", "abcde"] -> output = "abcde").
#   - Folositi functia reduce() si o expresie lambda pentru a obtine suma tuturor elementelor dintr-o lista. (input = [1, 2, 3] -> output = 6)

# from functools import reduce
# # lista=["abc", "abcd", "abcde"]
# # print(reduce(lambda x,y:x if len(x)>len(y) else y, lista))
#
# lista=[1,2,3,42,53,64,75]
# print(reduce(lambda x,y:x+y,lista))
# TODO 4. **filter:**
#     - Folosind `filter`, extrage toate numerele pare dintr-o listă.(input = [1, 2, 3, 4, 5, 6] -> output = [2, 4, 6])
#     - Extrage cuvintele care încep cu o anumită literă dintr-o listă.(input = ["abc", "bcd", "cde"], litera = "b" -> output = ["bcd"])
# lista_mea=[1, 2, 3, 4, 5, 6,7,8,9,10]
# print(list(filter(lambda x:x%2==0,lista_mea)))
# TODO 5. **min/max:** hint: folosiți parametrul `key` al funcției `min`/`max`
#     - Găsește șirul de caractere cu cea mai mare si cea mai mica lungime dintr-o listă folosind funcția `max` și o funcție lambda.(input = ["abc", "abcd", "abcde"] -> output = "abcde")
#     - Găsește numărul cu cea mai mare si cea mai mica valoare dintr-o listă de string-uri care reprezintă numere, folosind funcția `max` și o funcție lambda.(input = ["1", "2", "3"] -> output = "3").
# input = ["abc", "abcd", "abcde"]
# input_max=max(input,key=lambda x: len(x))
# input_min=min(input,key=lambda x: len(x))
# print(input_max)
# print(input_min)
# input = ["1", "2", "3"]
# input_max=max(input,key=lambda x:int(x))
# input_min=min(input,key=lambda x:int(x))
# print(input_max)
# print(input_min)
# TODO 6. **sorted:** hint: folosiți parametrul `key` al funcției `sorted`
#     - Sortează o listă de cuvinte în funcție de lungimea lor, folosind funcția `sorted` și o funcție lambda.(input = ["abcde", "abcd", "abcdef"] -> output = ["abcd", "abcde", "abcdef"])
#     - Sortează o listă de tuple după al doilea element al fiecărei tuple.(input = [(1, 2), (3, 1), (2, 3)] -> output = [(3, 1), (1, 2), (2, 3)])
# lista = ["dulciuri", "fructe", "ou"]
# lista_sortata=sorted(lista,key=lambda x: len(x))
# print(lista_sortata)
# lista = [(1, 2), (3, 1), (2, 3)]
# lista_sortata=sorted(lista,key=lambda x: x[1])
# print(lista_sortata)
# TODO 7. Filtrare după un caracter specific: Folosim o funcție lambda pentru a filtra o listă de șiruri de caractere, păstrând doar acele șiruri care conțin un anumit caracter.
#  De exemplu, dacă filtrăm lista de cuvinte ["abc", "bcd", "cde"] pentru a păstra doar cuvintele care conțin caracterul "b", vom obține ["abc", "bcd"].
# cuvinte=["abc", "bcd", "cde"]
# caracter="b"
# print(list(filter(lambda cuvant:caracter in cuvant,cuvinte)))
# TODO 8. Transformare șiruri în majuscule: Folosim o funcție lambda pentru a transforma fiecare element dintr-o listă de șiruri de caractere în majuscule.
#  De exemplu, dacă avem lista ["abc", "bcd", "cde"], vom obține ["ABC", "BCD", "CDE"].
# lista=["abc", "bcd", "cde"]
#
# print(list(map(lambda cuvant:cuvant.upper(),lista)))

# TODO 1 : Creati un generator care genereaza patratele unor N numere
# def patratele_numerelor(N):
#     for numere in range(N):
#         yield numere**2
# nr_patrate=patratele_numerelor(5)
# print(next(nr_patrate))
# print(next(nr_patrate))
# print(next(nr_patrate))
# print(next(nr_patrate))
# print(next(nr_patrate))


# TODO 2 : Creati un generator care genereaza numere random intre un minim si un maxim date ca parametru (nota folositi random.randint)
# import random
# def numere_random(min,max):
#     yield random.randint(min,max)
#
# min=5
# max=150
# numar_random=numere_random(5,100)
# for numar in numar_random:
#     print(f"Numarul random intre {min} si {max}: {numar}")

# TODO 3 : Utilizant functia iter() si next() convertiti un string intr-un iterator si afisati fiecare caracter din string
# string="Ana are mere"
# iterator=iter(string)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# TODO 4: Generati o secventa de numere pare si divizibile cu 3. (generator)
# def generator_pare_div_3(min,max):
#     for numere in range(min,max+1):
#         if numere%3==0 and numere%2==0:
#             yield numere
# nr_pare=generator_pare_div_3(5,80)
# print(next(nr_pare))
# print(next(nr_pare))
# print(next(nr_pare))
# print(next(nr_pare))
# print(next(nr_pare))
# print(next(nr_pare))
# print(next(nr_pare))
# print(next(nr_pare))
# print(next(nr_pare))
# print(next(nr_pare))
# print(next(nr_pare))
# print(next(nr_pare))
# print(next(nr_pare))
# print(next(nr_pare))
# TODO 5: Generați o secvență de numere aleatoare între 1 și 100.(generator)
# import random
# def numere_random(N):
#     for numar in range(N):
#         yield random.randint(1,100)
# N=10
# generator=numere_random(N)
# for numar in generator:
#     print(numar)





# TODO 6: Generați cuvintele dintr-o propozitie.(generator)
# string2 = "Ana are mere si pere"
# def cuvinte(string2):
#     cuvinte=string2.split()
#     for cuvant in cuvinte:
#         yield cuvant
# generator=cuvinte(string2)
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))

# TODO 7 : Generator de Numere Impare: Implementează un generator care produce numere impare, începând de la 1 și continuând până la un limită specificată.

# def generator_numere(min,max):
#     for numere in range(min,max+1):
#         if numere%2!=0:
#             yield numere
# min=1
# max=100
# generator=generator_numere(min,max)
# for numere in generator:
#     print(numere)

# TODO 8: Generator de Caractere dintr-un Șir: Realizează un generator care parcurge fiecare caracter dintr-un șir dat. De exemplu, pentru șirul "hello", generatorul ar trebui să producă 'h', 'e', 'l', 'l', 'o'.

# sir="Ana are mere"
# def litera_sir(sir):
#     for caracter in sir:
#         yield caracter
# generator=litera_sir(sir)
# for caracter in generator:
#     print(caracter)
# TODO 1 . Compararea metodelor de concatenare a sirurilor de caractere.
#  Se cere sa comparati doua metode de concatenare a sirurilor de caractere in Python.
#   1. Concatenarea cu ajutorul operatorului +
#   2. Concatenarea cu ajutorul metodei join() a sirurilor de caractere.
#  Instructiuni:
#   1. Generati o lista cu 10000 de siruri de caractere (importati modulul random si string pentru a genera siruri aleatoare)
#   lista_siruri = [''.join(random.choices(string.ascii_lowercase, k=5)) for _ in range(10000)]
#   2. Pentru prima metoda, initiati un sir gol si concatenati fiecare sir din lista folosind operatorul "+"
#   3. Pentru a doua metoda, concatenati toate sirurile din lista folosind metoda join()
#   4. Comparati timpul de executie pentru fiecare metoda folosind modulul timeit
#
# import random
# import string
# import timeit
# lista_siruri = [''.join(random.choices(string.ascii_lowercase, k=5)) for _ in range(1000000)]
# def concatenare_plus():
#     sir_final=''
#     for sir in lista_siruri:
#         sir_final+=sir
#     return sir_final
#
# def concatenare_join():
#     return ''.join(lista_siruri)
# setup="""from __main__ import concatenare_plus, concatenare_join"""
# timp_plus=timeit.timeit("concatenare_plus()",setup=setup,number=1000000)
# timp_join=timeit.timeit("concatenare_join()",setup=setup,number=1000000)
# print(f'Timpul pentru concatenarea cu plus este de {timp_plus}')
# print(f'Timpul pentru concatenarea cu join este de {timp_join}')


# TODO 2:Comparați două metode de inversare a șirurilor de caractere în Python.
#  Metode de Inversare:
#  1. Folosirea slicing-ului.
#  2. Folosirea unei bucle for.
#  Instrucțiuni:
#  Generați un șir de caractere lung (de exemplu, 1000 de caractere). Puteți folosi modulul random și string pentru a genera un șir aleatoriu.
#  import random
#  import string
#  sir_lung = ''.join(random.choices(string.ascii_letters + string.digits, k=1000))
#  Pentru prima metodă, inversați șirul folosind slicing (sir_inversat = sir_lung[::-1]).
#  Pentru a doua metodă, creați un șir gol și adăugați caracterele unul câte unul în ordine inversă folosind o buclă for.
#  Comparați timpul de execuție pentru fiecare metodă folosind modulul timeit.
# import random
# import string
# import timeit
# sir_lung = ''.join(random.choices(string.ascii_letters + string.digits, k=1000))
#
# def inversare_slicing():
#     return sir_lung[::-1]
#
# # Funcția pentru inversare folosind bucla for
#
#
# def inversare_for():
#     sir_inversat_for = ''
#     for caracter in sir_lung:
#         sir_inversat_for = caracter + sir_inversat_for
#     return sir_inversat_for
#
#
# # Timpul pentru metoda slicing
# timp_slicing = timeit.timeit(stmt=inversare_slicing, number=1000)
#
# # Timpul pentru metoda cu bucla for
# timp_for = timeit.timeit(stmt=inversare_for, number=1000)
# print(f"Timpul pentru slicing: {timp_slicing}")
# print(f"Timpul pentru bucla for: {timp_for}")

# TODO 1 Decorator pentru afișarea unui mesaj înainte și după o funcție.
#  Cerințe:
#  1. Creați un decorator numit afișare_mesaje care afișează un mesaj înainte și după apelul funcției invelite.
#  2. Utilizați decoratorul pentru a inveli o funcție și afișați mesaje înainte și după apelul acesteia.
# def decorator_mesaj(functie):
#     def wrapper(*args,**kwargs):
#         print("Mesaj inainte de apelul functiei.")
#         rezultat=functie(*args,**kwargs)
#         print("Mesaj dupa apelul functiei.")
#         return rezultat
#     return wrapper
# @decorator_mesaj
# def functie_exemplu():
#     print("Functia este apelata.")
#
# functie_exemplu()

# TODO 2 : Decorator verificare argumente.
#  Cerinte:
#  Creati un decorator care verifica daca argumente unei functii sunt mai mari ca 5 si daca nu aruncam o exceptie.
#  Va functiona doar pentru functii care primesc excat 2 argumente.
# def decorator_verificare(functie):
#     def wrapper(a,b):
#         if a>5 and b>5:
#             raise ValueError("Argumentele primite nu pot fi mai mari decat 5.")
#         return functie(a,b)
#
#     return wrapper
# @decorator_verificare
# def functie_exemplu(arg1,arg2):
#     print(f"Arg1: {arg1}, Arg2: {arg2}")
#
# functie_exemplu(6,6)



# TODO 3 Decorator pentru autentificare.
#  Cerințe:
#  Creați un decorator numit autentificare care verifică dacă utilizatorul este autentificat înainte de a accesa o funcție.
#  Definiți o funcție pagina_protejată care necesită autentificarea și utilizați decoratorul autentificare pentru a proteja funcția.
# utilizator_autentificat=True
# def decorator_autentificare(functie):
#     def wrapper(*args,**kwargs):
#         if utilizator_autentificat:
#             return functie(*args,**kwargs)
#         else:
#             return "Acces nepermis"
#     return wrapper
# @decorator_autentificare
# def autentificare_exemplu():
#     return "Bine ai venit!"
# print(autentificare_exemplu())



# TODO 4 Decorator pentru măsurarea timpului de execuție.
#  Cerințe:
#  Creați un decorator numit măsură_timpul care măsoară timpul de execuție al unei funcții și îl afișează. Daca timpul de execuție depășește 3 secunde,
#  se va afisa o eroare.
#  Folosiți decoratorul pentru a măsura timpul de execuție al unei funcții de 4 secunde și afișați rezultatul.

# import time
# def decorator_masura_timpul(functie):
#     def wrapper(*args,**kwargs):
#         start=time.time()
#         rezultat=functie(*args,**kwargs)
#         stop = time.time()
#         timp_executie=stop-start
#         if timp_executie>3:
#             raise Exception(f"Timpul {timp_executie} a fost depasit")
#         else:
#             print(f"Timpul de executie a fost de {timp_executie}")
#     return wrapper
# @decorator_masura_timpul
# def functia_mea():
#     time.sleep(5)
# functia_mea()



"""clase de baza si mosteniri"""
# class Student:
#     def __init__(self,nume,varsta):
#         self.nume=nume
#         self.varsta=varsta
#
#     def __str__(self):
#         return f"{self.nume} {self.varsta}"
#
# class Angajat(Student):
#     def __init__(self, nume, varsta, salariu):
#         super().__init__(nume, varsta)
#         self.salariu=salariu
# student1=Student("Mario",19)
# print(student1)
# angajat1=Angajat("Mario",19,40000)
# print(angajat1)
# print(angajat1.salariu)

# TODO 1.Implementarea unei Ierarhii de Clase
#  Cerințe:
#  Creați o clasă de bază numită Vehicul care să conțină atribute pentru marca, modelul și anul unui vehicul, și o metodă detalii care să afișeze aceste informații.
#  Creați două clase derivate: Automobil și Motocicletă, care să moștenească clasa Vehicul. Fiecare clasă derivată ar trebui să aibă atribute adiționale și metode care sunt specifice tipului de vehicul (de exemplu, nr_usi pentru Automobil și are_coș pentru Motocicletă).
#  Suprascrieți metoda detalii în fiecare clasă derivată astfel încât să afișeze informații adiționale specifice fiecărui tip de vehicul.
#  Creați câteva instanțe ale claselor Automobil și Motocicletă, și apelați metoda detalii pentru fiecare instanță.
#  Adăugați în clasa Automobil o metodă numită accelereaza care să primească un parametru km_h și să afișeze mesajul "Automobilul accelerează cu X km/h", unde X este valoarea primită.
#  Adăugați în clasa Motocicletă o metodă numită wheelie care, atunci când este apelată, va afișa mesajul "Motocicleta face un wheelie!", reprezentând o manevră specifică motocicletelor.
#  Creați o clasă nouă derivată numită Camion, care moștenește de asemenea clasa Vehicul. Această clasă ar trebui să aibă atribute suplimentare precum capacitate_tonaj și o metodă incarca care să primească o valoare numerică reprezentând numărul de tone încărcate și să afișeze "Camionul a fost încărcat cu Y tone", unde Y este valoarea primită.

# class Vehicul:
#     def __init__(self,marca,model,an):
#         self.marca=marca
#         self.model=model
#         self.an=an
#
#     def detalii(self):
#         return f"Marca: {self.marca}, Model: {self.model}, An: {self.an}"
#
# class Automobil(Vehicul):
#     def __init__(self,marca,model,an,nr_usi):
#         super().__init__(marca,model,an)
#         self.nr_usi=nr_usi
#
#     def show_usi(self):
#         print(f'Numarul usilor: {self.nr_usi}')
#
#     def detalii(self):
#         return f"{super().detalii()},Numar usi: {self.nr_usi}"
#
#     def accelereaza(self,km_h):
#         return f'Automobilul {self.marca} accelerează cu {km_h} km/h'
#
# class Motocicleta(Vehicul):
#     def __init__(self,marca,model,an,nr_roti):
#         super().__init__(marca,model,an)
#         self.nr_roti=nr_roti
#
#     def show_roti(self):
#         print(f'Numarul rotilor: {self.nr_roti}')
#
#     def detalii(self):
#         return f"{super().detalii()}Numarul rotilor: {self.nr_roti}"
#
#     def wheelie(self):
#         return "Motocicleta face un wheelie!"
#
# class Camion(Vehicul):
#     def __init__(self,marca,model,an,capacitate_tonaj):
#         super().__init__(marca,model,an)
#         self.capacitate_tonaj=capacitate_tonaj
#
#     def incarcare_tone(self,y):
#         return f"Camionul a fost încărcat cu {y} tone"
#
# automobil1=Automobil("Audi","RS4",2024,2)
# motocicleta1=Motocicleta("Yamaha","1000r",2020,3)
# camion1=Camion("Mercedes","CLS200",2020,20)
# print(automobil1.detalii())
# print(motocicleta1.detalii())
# print(automobil1.accelereaza(500))
# print(motocicleta1.wheelie())
# print(camion1.incarcare_tone(15))

# TODO 2.Clase Abstracte și Metode Statice
#  Cerințe:
#  Creați o clasă abstractă numită Dispozitiv care să conțină o metodă abstractă operare și o metodă statică informatii_dispozitiv care să primească un parametru și să îl afișeze.
#  Creați două clase derivate: Telefon și Calculator, care să moștenească clasa Dispozitiv. Fiecare clasă derivată ar trebui să aibă o implementare proprie a metodei operare.
#  Apelați metoda statică informatii_dispozitiv cu diferite argumente și apelați metoda operare pentru câteva instanțe ale claselor Telefon și Calculator.
#  Adăugați o metodă de clasă numită informatii_generale în clasa Dispozitiv care să returneze un mesaj general despre dispozitive.
#  În clasa Telefon, adăugați o metodă specifică instaleaza_aplicatie care să primească numele unei aplicații ca parametru și să afișeze un mesaj că aplicația a fost instalată.
#  În clasa Calculator, implementați o metodă actualizeaza_sistemul care să afișeze un mesaj că sistemul de operare a fost actualizat.

# from abc import ABC,abstractmethod
# class Dispozitiv(ABC):
#     @abstractmethod
#     def operare(self):
#         pass
#     @staticmethod
#     def informatii_dispozitiv(value):
#         return f'Produsul are urmatorul pret: {value} lei'
#
# class Telefon(Dispozitiv):
#     def __init__(self,marca,model,sistem_operare):
#         self.marca=marca
#         self.model=model
#         self.sistem_operare=sistem_operare
#
#     def operare(self):
#         return f"{self.marca}-ul {self.model} are ca sistem de operare {self.sistem_operare}."
#
#     def instaleaza_aplicatie(self,nume_aplicatie):
#         return f"Aplicatia {nume_aplicatie} a fost instalata."
#
# class Calculator(Dispozitiv):
#     def __init__(self,placa_video,procesor,sist_operare):
#         self.placa_video=placa_video
#         self.procesor=procesor
#         self.sist_operare=sist_operare
#
#     def operare(self):
#         return f"Calculatorul cu componentele: {self.placa_video}, {self.procesor} are ca sistem de operare {self.sist_operare}."
#
#     def actualizeaza_sistemul(self):
#         return f"Sistemul a fost actualizat!"
#
# telefon1=Telefon("Iphone","16 PRO MAX","IOS")
# print(telefon1.operare())
# print(telefon1.informatii_dispozitiv(7200))
# print(telefon1.instaleaza_aplicatie("Clash Royale"))
# calculator1=Calculator("Rtx 4090","I9 14900k","Windows")
# print(calculator1.operare())
# print(calculator1.informatii_dispozitiv(40000))
# print(calculator1.actualizeaza_sistemul())

# TODO 3. Exercitiu cu dataclasses
#  Cerințe:
#  1. Să se creeze o clasă numită Student cu atributele nume, prenume, varsta și note (o listă cu note).
#  2. Să se creeze câteva instanțe ale clasei Student și să se afișeze informațiile despre acestea.
#  3. Accesati si modificati campurile instantelor create (ex: modificati numele)

# from dataclasses import dataclass
# @dataclass
# class Student():
#     nume:str
#     prenume:str
#     varsta:int
#     note:[]
#
# student1=Student("Mihai","Mario",19,[10,9,9,10])
# print(student1)
# student1.nume="Cristian"
# student1.varsta=20
# student1.note=[10,9,10,10]
# print(student1)

# TODO 4.Exercitiu combinat
#   Sistem de Gestionare pentru o Clinică Veterinară
#   În această temă, veți explora conceptele de bază ale Programării Orientate Obiect (OOP) utilizând un scenariu real: gestionarea unei clinici veterinare.
#   Veți defini și manipula clase, obiecte, metode de instanță, metode statice, metode de clasă și moștenire.
#   Cerințe:
#   1. **Clasa Animal:**
#     - Creați o clasă abstractă denumită `Animal` care va servi ca șablon pentru diferite tipuri de animale.
#     - Clasa `Animal` trebuie să aibă o metodă abstractă `display_info` care va afișa informații despre animal.
#     - Clasa `Animal` trebuie să aibă o metodă statică `next_checkup` care va calcula data următorului control veterinar, bazată pe un număr de zile dat ca argument.
#   2. **Clasele Dog și Cat:**
#     - Creați două clase, `Dog` și `Cat`, care moștenesc clasa `Animal`.
#     - Fiecare clasă derivată trebuie să aibă un constructor care acceptă și inițializează numele și rasa animalului.
#     - Fiecare clasă derivată trebuie să implementeze metoda `display_info`.
#   3. **Clasa Owner:**
#     - Creați o clasă denumită `Owner` pentru a reprezenta proprietarii animalelor.
#     - Clasa `Owner` trebuie să aibă un atribut `name` și un atribut `pets` (o listă care va stoca animalele deținute de proprietar).
#     - Clasa `Owner` trebuie să aibă o metodă `add_pet` care va adăuga un animal la lista de animale deținute.
#   4. **Clasa Veterinarian:**
#     - Creați o clasă denumită `Veterinarian` pentru a reprezenta veterinarii din clinică.
#     - Clasa `Veterinarian` trebuie să aibă o metodă de clasă `schedule_checkup` care va programa un control veterinar pentru un anumit animal.
#   5. **Crearea și Manipularea Obiectelor:**
#     - Creați obiecte pentru fiecare clasă și demonstrați funcționalitatea sistemului prin manipularea acestor obiecte.
#     - Exemplu: creați un obiect `Dog`, un obiect `Owner`, adăugați câinele la lista de animale deținute de proprietar, și programați un control veterinar pentru câine.
# from abc import ABC, abstractmethod
# from datetime import datetime,timedelta
#
# class Animal():
#     @abstractmethod
#     def display_info(self):
#         pass
#     @staticmethod
#     def next_checkup(days):
#         next_date=datetime.now() + timedelta(days = days)
#         return next_date.strftime("%Y-%m-%d")
#
# class Dog(Animal):
#     def __init__ (self,nume,rasa_animal):
#         self.nume=nume
#         self.rasa_animal=rasa_animal
#
#     def display_info(self):
#         return f"Numele cainelui {self.nume} de rasă {self.rasa_animal} "
#
# class Cat(Animal):
#     def __init__ (self,nume,rasa_animal):
#         self.nume=nume
#         self.rasa_animal=rasa_animal
#
#     def display_info(self):
#         return f"Numele pisicii {self.name} de rasă {self.rasa_animal} "
#
# class Owner(Animal):
#     def __init__(self,nume):
#         self.nume=nume
#         self.animale=[]
#
#     def add_pet(self,animal):
#         self.animale.append(animal)
#         return f"{self.nume} detine {animal.display_info()}"
#
# class Veterinar():
#     nume="Andrei"
#
#     @classmethod
#     def schedule_checkup(cls,animal,owner,vet_name):
#         return f"Controlul veterinar pentru {animal.display_info()} a fost programat cu veterinarul {vet_name}"
#
# animal1=Animal()
# catel=Dog("Rex","Husky")
# pisica=Cat("ASD","Munchkin")
# proprietar=Owner("Mario")
# veterinar1=Veterinar()
# print(proprietar.add_pet(catel))
# print(veterinar1.schedule_checkup(catel,proprietar,"Doctor Andrei"))

# TODO 5
#  Să ne imaginăm că dezvoltăm un sistem mai avansat pentru gestionarea echipamentelor într-o companie de închirieri echipamente sportive.
#  Vom proiecta o clasă abstractă pentru a reprezenta diferite tipuri de echipamente sportive, care va include funcționalități pentru afișarea
#  informațiilor(abstracta), data de retur(statica),calculeaza_cost(statica)
#  Clase derivate specifice, precum Schiuri, Bicicleta, și CascaProtectie, vor implementa aceste metode și vor adăuga atribute relevante pentru
#  fiecare tip de echipament(schiuri - marca si model; bicicleta - tip(ex munte,strada,etc)/marime; casca protectie - marime,culoare).
#  Pe lângă acestea, vom construi o clasă pentru clienți, care pot închiria echipamente si vor fi adaugate  la o lista de echipeamente inchiriate.
#  De asemenea, va exista o clasă pentru angajații companiei, care vor putea procesa închirierile.
#  Fiecare echipament sportiv va avea asociat un cost de închiriere pe zi și sistemul va calcula costul total bazat pe durata închirierii.
#  Pentru a testa fiecare metodă din clasa Angajat, vom urmări următorii pași:
#  Crearea unui Client și a unor Echipamente Sportive: Înainte de a testa metoda proceseaza_inchiriere, trebuie să avem un client și câteva echipamente sportive.
#  Testarea metodei proceseaza_inchiriere:
#  Instanțierea unui client (să zicem Ion Popescu) și a unor echipamente sportive (de exemplu, schiuri, o bicicletă, și o cască de protecție).
#  Crearea unui obiect Angajat.
#  Apelarea metodei proceseaza_inchiriere pentru diferite combinații de client, echipament, număr de zile și preț pe zi.
#  OPTIONAL : Introduceti o variabila privata impreuna cu implementarea de setter,getter si deleter in exercitiu. Modificati clasa Client pentru a include
#  o astfel de variabila (putem face 'nume' o variabila privata)
# from abc import ABC,abstractmethod
# from datetime import datetime,timedelta
#
# class Echipamente_sportive():
#     @abstractmethod
#     def afisarea_informatiilor(self):
#         pass
#     @staticmethod
#     def data_de_retur(nr_zile):
#         data_retur=datetime.now() + timedelta(nr_zile=nr_zile)
#         return data_retur
#     @staticmethod
#     def calculeaza_cost(pret_pe_zi,nr_zile):
#         return f"Costul echipamentului pe {nr_zile} zile este {pret_pe_zi*nr_zile} lei"
# class Schiuri(Echipamente_sportive):
#     def __init__(self,marca,model):
#         self.marca=marca
#         self.model=model
#
#     def afisarea_informatiilor(self):
#         return f"Schiurile sunt {self.marca} {self.model}"
#
# class Bicicleta(Echipamente_sportive):
#     def __init__(self,tip,marime):
#         self.tip=tip
#         self.marime=marime
#
#     def afisarea_informatiilor(self):
#         return f"Bicicleta de {self.tip} este marimea {self.marime}"
#
# class Casca_protectie(Echipamente_sportive):
#     def __init__(self,marime,culoare):
#         self.marime=marime
#         self.culoare=culoare
#
#     def afisarea_informatiilor(self):
#         return f"Casca de protecie este: marimea {self.marime}, culoarea {self.culoare}"
#
# class Clienti():
#     def __init__(self):
#         self.echipamente_inchiriate=[]
#
#     def inchirieri_echipamente(self,echipament):
#         self.echipamente_inchiriate.append(echipament)
#         return f"Au fost inchiriate urmatoarele echipamente: {self.echipamente_inchiriate}"
#
# class Angajatii_companiei():
#     def __init__(self,cost_inchiriere):

# TODO 6.Să presupunem că avem două clase de bază, Animal și Robot, și dorim să creăm o clasă derivată, CyborgAnimal, care să moștenească proprietăți și metode de la ambele clase.
#  Clasele de Bază:
#  Clasa Animal - aceasta reprezintă un animal obișnuit, cu atribute și metode specifice.
#  Clasa Robot - reprezintă un robot, cu atribute și metode diferite.
#  Clasa Derivată:
#  Clasa CyborgAnimal - combină caracteristicile unui animal și ale unui robot.



# class Animal():
#     def __init__(self,tip_animal,nume,varsta):
#         self.tip_animal=tip_animal
#         self.nume=nume
#         self.varsta=varsta
#
#     def descrie_animal(self):
#         return f"Animalul {self.tip_animal} cu numele {self.nume} are varsta de {varsta} saptamani"
#
# class Robot():
#     def __init__(self,culoare,an_fabricatie):
#         self.culoare=culoare
#         self.an_fabricatie=an_fabricatie
#
#     def prezentare_robot(self):
#         return f'Robotul de culoare {self.culoare} a fost fabricat in anul {self.an_fabricatie}'
#
# class CyborgAnimal(Animal,Robot):
#     def __init__(self,tip_animal,nume,varsta,culoare,an_fabricatie):
#         Animal.__init__(self,tip_animal,nume,varsta)
#         Robot.__init__(self,culoare,an_fabricatie)
#
#     def combina_caracteristicile(self):
#         return f"Cyborgul animal este un robot de culoare {self.culoare} fabricat in anul {self.an_fabricatie} dar totodata este si o {self.tip_animal} cu numele {self.nume}.Acesta are varsta de {self.varsta} saptamani"
#
# CyborgAnimal1=CyborgAnimal("Pisicuta","Milky",2,"alba",2024)
# print(CyborgAnimal1.combina_caracteristicile())

# Extindeți clasele Animal, Caine și Pisica pentru a include un atribut nou care să reprezinte numărul de picioare.
# Apoi creați o metodă afisarePicioare() care să afișeze câte picioare are fiecare animal. Cainele are mereu 4 picioare, iar pisica la fel,
# însă un animal generic poate avea oricâte.

# class Animal():
#     def __init__(self,nume,varsta,numar_picioare):
#         self.nume=nume
#         self.varsta=varsta
#         self.numar_picioare=numar_picioare
#
#     def sunet_animal(self):
#         pass
#
#     def numar_picioare_animal(self):
#         return f"{self.nume} are {self.numar_picioare} picioare."
#
# class Caine(Animal):
#     def __init__(self,nume,varsta):
#         super().__init__(nume,varsta,4)
#
#     def sunet_animal(self):
#         return f"{self.nume} face woof!"
#
# class Pisica(Animal):
#     def __init__(self, nume, varsta):
#         super().__init__(nume, varsta, 4)
#
#     def sunet_animal(self):
#         return f"{self.nume} face miauuu!"
#
# rex = Caine("Rex", 5)
# mia = Pisica("Mia", 3)
# paianjen = Animal("Paianjen", 1, 8)
#
# print(rex.numar_picioare_animal())
# print(mia.numar_picioare_animal())
# # print(paianjen.numar_picioare_animal())
# #
# # print(rex.sunet_animal())
# # print(mia.sunet_animal())
#
# Creează o clasă GradinaZoologica care să conțină o listă de obiecte de tip Animal (folosind polimorfism).
# Implementează o metodă adaugaAnimal() pentru a adăuga animale noi și o metodă prezentare() care să afiseze sunetul fiecărui animal din grădină.

# class Animal:
#     def __init__(self, nume, varsta):
#         self.nume = nume
#         self.varsta = varsta
#
#     def sunet(self):
#         pass
#
#
# class Caine(Animal):
#     def __init__(self, nume, varsta):
#         super().__init__(nume, varsta)
#
#     def sunet(self):
#         print(f"{self.nume} latră!")
#
#
# class Pisica(Animal):
#     def __init__(self, nume, varsta):
#         super().__init__(nume, varsta)
#
#     def sunet(self):
#         print(f"{self.nume} miaună!")
# class GradinaZoologica():
#     def __init__(self):
#         self.animale=[]
#
#     def adauga_animale(self,animal):
#         self.animale.append(animal)
#
#     def prezentare(self):
#         for animal in self.animale:
#             animal.sunet()
#
# zoo = GradinaZoologica()
#
#
# zoo.adauga_animale(Caine("Rex", 5))
# zoo.adauga_animale(Pisica("Mia", 3))
#
#
# zoo.prezentare()
# REGULAR EXPRESSIONS

# TODO 1 Utilizați modulul re pentru a găsi toate aparițiile literei "a" într-un text.(findall)
# text_1 = "Python este un limbaj de programare."
#  import re
# rezultat=re.findall("a",text_1)
# print(rezultat)

# TODO 2 Utilizați modulul re pentru a găsi toate vocalele dintr-un text.(findall)
# text_2 = "Exemplu de propozitie sau text."
# rezultat=re.findall(r"[aeiouAEIOU]",text_2)
# print(rezultat)
# TODO 3 Găsiți toate cuvintele care au 3 litere.Hint: utilizați caracterul special "\b" pentru a indica începutul și sfârșitul unui cuvânt.(findall)
# text_3 = " Ana si Dan sunt prieteni buni."
# rezultat=re.findall(r"\b\w{3}\b",text_3)
# #rezultat=re.findall(r"\b[A-Z]{1}[a-z]{2}\b",text_3)
# print(rezultat)
# TODO 4. Exercitiu cu grupuri de caractere:
#  Cerințe:
#  Creați o expresie regulată pentru a găsi toate prefixele numerelor de telefon dintr-un text. Un număr de telefon poate avea unul din următoarele formate: "123-456-7890".
#  Utilizați grouping pentru a defini grupuri în expresia regulată pentru a izola codul de zonă(123,987,555)
# text_4="""
# Lista de contacte:
# - John: 123-456-7890
# - Jane: 987-654-3210
# - Alice: 555-123-4567
# """
# sablon=r"(\d{3})-\d{3}-\d{4}"
# rezultat=re.f(sablon,text_4)
# print(rezultat)
# TODO 5. Exercitiu cu grupuri de caractere:
#  Cerințe:
#  Creați o expresie regulată care să găsească toate datele în format "dd/mm/yyyy" dintr-un text.
#  Utilizați expresia regulată pentru a găsi toate datele dintr-un text dat și afișați-le separat.

# text_5 = """
# Lista de evenimente:
# 1. Ziua de naștere a lui John: 15/02/1990
# 2. Conferința anuală: 10/11/2022
# 3. Vacanță de vară: 30/07/2023
# """
# import re
# class DeschidereFisier:
#        def __init__(self,filename,mode):
#            self.filename=filename
#            self.mode=mode
#            self.file=None
#        def __enter__(self):
#            self.file=open(self.filename,self.mode)
#            return self.file
#        def __exit__(self, exc_type, exc_val, exc_tb):
#            if self.file:
#                self.file.close()
#            if exc_type is not None:
#                print(f"Exceptie de tip {exc_type} a aparut cu mesajul {exc_val}")
#            return True
# # Exemplu de testare
# with DeschidereFisier("context_manager.txt", "w") as fisier:  # pentru a testa eroarea, schimbati "w" cu "wb"
#    fisier.write("Aceasta este o linie de test .\n")
# #Verificam daca fisierul a fost inchis
# print("Fisierul este inchis ?", fisier.closed)
#
# # Simulam o exceptie
#
# try:
#    with DeschidereFisier('context_manager.txt', 'w') as file:
#       file.write("Vom avea o eroare")
#       raise ValueError("Eroare simulata")
# except Exception as e:
#    # Acest bloc de cod nu ar trebui executat pentru ca  __exit__ return TRUE, care suprima exceptia
#     print("Aceasta linie nu ar trebui printata", e)

# TODO 3.Salvați dicționarul într-un fișier folosind modulul pickle și apoi recuperați datele din fișier și afișați-le.
# import pickle
# studenti = {1: {'nume': 'Ion', 'varsta': 20, 'specializare': 'Informatica'},
#             2: {'nume': 'Maria', 'varsta': 21, 'specializare': 'Informatica'},
#             3: {'nume': 'Andrei', 'varsta': 22, 'specializare': 'Informatica'},
#             4: {'nume': 'Mihai', 'varsta': 23, 'specializare': 'Informatica'}}
#
# with open("studenti.pickle","wb") as file:
#     pickle.dump(studenti,file)
#
# with open("studenti.pickle","rb") as file:
#     studenti_recuperati=pickle.load(file)
#
# print(studenti_recuperati)

# TODO 4: Creati o listă de dicționare, fiecare reprezentând informații despre un student: nume, vârstă și specializare.
#   Exemplu listă: [{'nume': 'Ion Popescu', 'varsta': 20, 'specializare': 'Informatică'}, {'nume': 'Maria Ionescu', 'varsta': 19, 'specializare': 'Matematică'}]
#   Serializați lista într-un fișier numit studenti.csv, folosind ca anteturi cheile dicționarului.
#   Deserializați conținutul fișierului studenti.csv și afișați fiecare rând.
# import csv
# date = [
# 	{'nume': 'Ion Popescu', 'varsta': 20, 'specializare': 'Informatica'},
# 	{'nume': 'Maria Ionescu', 'varsta': 19, 'specializare': 'Matematica'}
# ]
#
# with open("studenti.csv","w",encoding='utf-8') as fisier_csv:
#     col_names=['nume','varsta','specializare']
#     writer=csv.DictWriter(fisier_csv,fieldnames=col_names)
#     writer.writeheader()
#     writer.writerows(date)
#
# with open("studenti.csv","r") as fisier_csv_2:
#     reader=csv.DictReader(fisier_csv_2)
#     for row in reader:
#         print(row)

# TODO 1: Verificați dacă un text conține un număr de telefon valid de tip "###-###-####".
# import re
# text_1 = "Contactati-ne la numarul 123-456-7890 pentru mai multe informatii."
# sablon=r"(\d{3}-\d{3}-\d{4})"
# rezultat=re.search(sablon, text_1)
# if rezultat:
#     numar_telefon=rezultat.group(1)
#     print(f"In text se afla urmatorul numar de telefon valid: {numar_telefon}")
# else:
#     print("Nu exista nici macar un numar de telefon valid.")
# TODO 2: Găsiți toate secvențele de cifre dintr-un text.
# import re
# text_2 = "Am castigat 1000 de puncte, dar am pierdut 250 ieri."
# sablon=r"(\d+)"
# rezultat=re.findall(sablon, text_2)
# print(rezultat)

# TODO 7: Găsiți toate sumele de bani în format "###.## RON" dintr-un text.
# import re
# text_7 = """
# Detalii despre costuri:
# 1. Produsul X: 123.45 RON
# 2. Produsul Y: 250.00 RON
# 3. Transportul: 25.30 RON
# """
# sablon=r"(\d{3}\.\d{2} \w{3})"
# rezultat=re.findall(sablon, text_7)
# print(rezultat)

# TODO 6: Extrageți toate orele în format "hh:mm" dintr-un text.
# import re
# text_6 = """
# Programul evenimentului:
# 1. Începerea: 09:30
# 2. Pauza de prânz: 12:45
# 3. Finalul zilei: 18:00
# """
# sablon=r"(\d{2}:\d{2})"
# rezultat=re.findall(sablon, text_6)
# print(rezultat)

# TODO 1: Serializati un fisier JSON (file_content.json)  cu continutul:
#  { "right_side":[ 3, 5, 3, 6, 4, 2, 3, 6, 8, 4, 3, 2 ], "left_side":[ 1.2, 4.3, 5.4, 6.9, 9.9, 7.2 ] }.
#  Scrieti un program care printeaza media numerelor in partea dreapta si media numerelor din partea stanga dar si media ambelor parti.
# import json
# object = {
#     "right_side": [3, 5, 3, 6, 4, 2, 3, 6, 8, 4, 3, 2],
#     "left_side": [1.2, 4.3, 5.4, 6.9, 9.9, 7.2]
# }
# with open('file_content.json', 'w') as file:
#     json.dump(object,file)
# with open('file_content.json', 'r') as file:
#     content = json.load(file)
# right_side = content["right_side"]
# left_side = content["left_side"]
# right_avg = sum(right_side) / len(right_side)
# left_avg = sum(left_side) / len(left_side)
# combined_avg = (sum(right_side) + sum(left_side)) / (len(right_side) + len(left_side))
# print(f"Right side average: {right_avg}")
# print(f"Left side average: {left_avg}")
# print(f"Combined average: {combined_avg}")
# Pas 1.Serializati un fisier JSON (file_content.json)  cu continutul:
#  { "right_side":[ 3, 5, 3, 6, 4, 2, 3, 6, 8, 4, 3, 2 ], "left_side":[ 1.2, 4.3, 5.4, 6.9, 9.9, 7.2 ] }.
# Pas 2.Apoi, veți scrie un program care realizează următoarele sarcini:
    # Citirea datelor din acest fișier JSON.
    # Calcularea mediei numerelor din lista right_side.
    # Calcularea mediei numerelor din lista left_side.
    # Calcularea mediei combinate a numerelor din ambele liste.
    # Rezultatul final va fi afișarea celor trei medii: media pentru partea dreaptă, media pentru partea stângă și media combinată a ambelor părț

# TODO 2: Scrieti o functie care converteste din CSV in JSON si salvati rezultatul in fisierul json_file.
# import json
# import csv
# def convertire_csv_to_json(csv_data,json_file):
#     data=[]
#     with open(csv_data,'r',) as file:
#         csv_reader=csv.DictReader(file)
#         for row in csv_reader:
#             data.append(row)
#     with open(json_file,'w',) as json_file:
#         json.dump(data,json_file,indent=4,)
# convertire_csv_to_json('csv_data.csv', 'json_data.json')

# TODO 1 Scrie un program care creează două thread-uri.
#  Primul thread să afișeze numerele de la 1 la 5, iar al doilea să afișeze literele de la 'a' la 'e'.
#  Fiecare thread va afișa un element și apoi va dormi pentru o secundă.
# import threading
# import time
#
# def numere_1_5():
#     for numar in range(1,6):
#         print(numar)
#         time.sleep(1)
#
# def litere_a_e():
#     for litera in range(ord('a'),ord('f')):
#         print(chr(litera))
#         time.sleep(1)
#
# thread1=threading.Thread(target=numere_1_5)
# thread2=threading.Thread(target=litere_a_e)
# thread1.start()
# thread2.start()
# thread1.join()
# thread2.join()



# TODO 2 Scrie un program care simulează descărcarea a trei fișiere diferite.
#  Fiecare "descărcare" ar trebui să fie executată de un thread separat și să dureze un timp aleatoriu între 1 și 5 secunde.
# import threading
# import time
# import random
#
# def descarcare_fisier(nume_fisier):
#     durata=random.randint(1,5)
#     print(f"Incep descarcarea fisierului {nume_fisier}. Va dura {durata} secunde...")
#     time.sleep(durata)
#     print(f"Descarcarea {nume_fisier} a fost finalizata!")
# fisiere=["fisier1.txt","fisier2.txt","fisier3.txt"]
# threads=[]
# for fisier in fisiere:
#     thread1 = threading.Thread(target=descarcare_fisier, args=(fisier,))
#     threads.append(thread1)
#     thread1.start()
# for th in threads:
#     th.join()
# print("Toate fisierele s-au descarcat.")

# TODO 1 Compararea metodelor de căutare a unui element într-o listă
#
# Instrucțiuni:
#
#   1. Generați o listă de 1000 de numere întregi aleatorii.
#   2. Comparați două metode de căutare a unui element:
#   •  Folosirea operatorului in pentru o listă simplă.
#   •  Transformarea listei într-un set și folosirea operatorului in pentru un set.
#   3. Măsurați timpul necesar pentru a găsi un element într-o listă și într-un set.
# import random
# import timeit
#
# lista=[random.randint(1,1500) for i in range(1000)]
# numar=lista[500]
# def cauta_in_lista(numar,lista):
#     return numar in lista
#
# def cauta_in_set(numar,lista):
#     set_lista=set(lista)
#     return numar in set_lista
#
# timp_lista=timeit.timeit(stmt="cauta_in_lista(numar,lista)",globals=globals(),number=1000)
# timp_set=timeit.timeit(stmt="cauta_in_set(numar,lista)",globals=globals(),number=1000)
# print(f"Timpul pentru cautarea in lista este de {timp_lista}.")
# print(f"Timpul pentru cautarea in set este de {timp_set}.")


# TODO 2 Creează un decorator numit verifica_tipurile care verifică dacă toate argumentele unei funcții sunt de un anumit tip specificat (de exemplu, int).
 #  Dacă vreun argument nu este de tipul așteptat, decoratorul va ridica o excepție TypeError.

# def verifica_tipurile(tip):
#     def decorator(functie):
#         def wrapper(*args, **kwargs):
#             for arg in args:
#                 if not isinstance(arg,tip): #Verifica daca arg este de tipul tip
#                     raise TypeError(f"Argumentul {arg} nu este de tipul {tip.__name__}")
#             for cheie,valoare in kwargs.items():
#                 if not isinstance(valoare,tip):
#                     raise TypeError(f"Argumentul {cheie} cu {valoare} nu este de tipul {tip.__name__}")
#             return functie(*args, **kwargs)
#         return wrapper
#     return decorator
# @verifica_tipurile(str)
# def aduna_numere(a,b,c):
#     return a+b
# try:
#     print(aduna_numere("5",2,6))
# except TypeError as e:
#     print(e)


#  TODO 3 Utilizarea try, except, else, finally
# Cerință:
# Creează o funcție numită citeste_numar care citește un număr de la tastatură.
# Dacă utilizatorul introduce altceva decât un număr, va arunca o excepție ValueError.
# Folosește blocul try-except-else-finally pentru a gestiona intrarea.

# def citeste_numar():
#     try:
#         numar=int(input("Introdu un numar: "))
#     except ValueError:
#         print("Ati introdus o valoare invalida. Trebuie introdusa o valoare de tipul int.")
#     else:
#         print(f"Ati introdus numarul {numar}")
#     finally:
#         print("Incercarea de a citi un numar a luat sfarsit.")
# citeste_numar()

# TODO 4 Utilizarea raise pentru validarea unei parole
# Cerință:
# Creează o funcție numită verifica_parola care primește o parolă ca argument.
# Dacă parola este mai scurtă de 8 caractere, aruncă o excepție ValueError cu mesajul "Parola trebuie să conțină cel puțin 8 caractere!".
# Dacă parola este validă, returnează mesajul "Parola este validă!".

# def verifica_parola(parola):
#     if len(parola)<8:
#         raise ValueError("Parola trebuie să conțină cel puțin 8 caractere!")
#     else:
#         print("Parola este valida!")
#
# verifica_parola("MDSAR")


# TODO 5. Generator pentru generarea multiplilor unui număr
# Cerință:
# Creează un generator numit genereaza_multipli care primește două argumente: un număr și o limită. Generatorul va returna toți multiplii numărului
# dat până la acea limită.

# def genereaza_multipli(numar,limita):
#     for i in range(1,(limita//numar)+1):
#         yield numar*i
#
# for item in genereaza_multipli(3,20):
#     print(item)




# TODO 6. Iterator personalizat pentru parcurgerea inversă a unei liste
# Cerință:
# Creează o clasă ReverseIterator care implementează metodele __iter__ și __next__, astfel încât să parcurgă o listă de la ultimul element la primul.


# class ReverseIterator:
#     def __init__(self,lista):
#         self.lista=lista
#         self.index=len(lista)-1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index<0:
#             raise StopIteration("Ai ajuns la inceputul listei.")
#         element=self.lista[self.index]
#         self.index-=1
#         return element
#
# lista_mea=[1,2,3,4,5]
# iterator=ReverseIterator(lista_mea)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))


# TODO 7.   Filtrarea numerelor divizibile cu 3:
# Creează o listă de numere și aplică o expresie lambda cu filter() pentru a returna doar numerele divizibile cu 3.

# lista=[1,2,3,4,5,6,7,8,9]
# print(list(filter(lambda x: x%3==0,lista)))



# TODO 8. Moștenire simplă (singulară)
# Cerință:
# Creează două clase, Animal și Caine. Clasa Caine va moșteni de la clasa Animal. Clasa Animal va avea o metodă vorbeste(), iar clasa Caine va suprascrie această metodă pentru a afișa sunetul specific unui câine.
#
# Instrucțiuni:
#
#   1. Creează clasa Animal cu metoda vorbeste(), care afișează un mesaj generic.
#   2. Creează clasa Caine care moștenește clasa Animal și suprascrie metoda vorbeste() pentru a afișa "Ham ham!".
#   3. Instanțiază un obiect de tip Caine și apelează metoda vorbeste().
#

# class Animal:
#     def __init__(self,nume):
#         self.nume=nume
#
#     def vorbeste(self):
#         print("Animalul poate vorbi.")
#
# class Caine(Animal):
#     def __init__(self,nume,sunet):
#         super().__init__(nume)
#
#     def vorbeste(self):
#         print("Ham-ham")
#
# caine1=Caine("Rex","latrat")
# caine1.vorbeste()




# TODO 9: Moștenire multiplă (dublă)
#Creează trei clase: Vehicul, Zburator și MasinaZburatoare. Clasa MasinaZburatoare va moșteni atât de la clasa Vehicul, cât și de la clasa Zburator. Fiecare clasă va avea un constructor (__init__()) și atribute proprii. Constructorul clasei MasinaZburatoare trebuie să apeleze constructorii din clasele de bază.

    # 1.   Clasa Vehicul:
    # •    Constructorul va primi un atribut marca care specifică marca vehiculului.
    # •    Va avea o metodă conduc() care afișează mesajul "Conduc vehiculul  pe drum."
    # 2.   Clasa Zburator:
    # •    Constructorul va primi un atribut altitudine_maxima care specifică altitudinea maximă la care poate zbura.
    # •    Va avea o metodă zboara() care afișează mesajul "Zbor la altitudinea maximă de <altitudine_maxima> metri."
    # 3.   Clasa MasinaZburatoare:
    # •    Constructorul va primi atributele marca, altitudine_maxima și viteza care specifică viteza maximă a mașinii zburătoare.
    # •    Va apela constructorii din clasele Vehicul și Zburator.
    # •    Va avea o metodă pornire() care afișează mesajul "Masina zburătoare de marca  a pornit cu viteza maximă de  km/h."
    # 4.   Creează un obiect de tip MasinaZburatoare și apelează metodele conduc(), zboara() și pornire() pentru a verifica funcționalitatea moștenirii și constructorilor.


# class Vehicul:
#     def __init__(self,marca):
#         self.marca=marca
#
#     def conduc(self):
#         print("Conduc vehiculul pe drum.")
#
# class Zburator:
#     def __init__(self,altitudine_maxima):
#         self.altitudine_maxima=altitudine_maxima
#
#     def zboara(self):
#         print(f"Zbor la altitudinea maximă de {self.altitudine_maxima} metri.")
#
# class MasinaZburatoare(Vehicul,Zburator):
#     def __init__(self,marca,altitudine_maxima,viteza):
#         Vehicul.__init__(self,marca)
#         Zburator.__init__(self,altitudine_maxima)
#         self.viteza=viteza
#
#     def pornire(self):
#         print(f"Masina zburătoare de marca {self.marca} a pornit cu viteza maximă de {self.viteza} km/h.")
#
#
# masina_zburatoare=MasinaZburatoare("Pegas",100,250)
# masina_zburatoare.conduc()
# masina_zburatoare.zboara()
# masina_zburatoare.pornire()



#TODO 10 Clase Abstracte și Metode Statice

# Cerințe:
#
#   1. Creează o clasă abstractă numită Vehicul, care să conțină:
#   •  O metodă abstractă pornire() care trebuie implementată de clasele derivate.
#   •  O metodă statică informatii_vehicul() care primește un parametru și afișează detalii despre vehicul.
#   •  O metodă de clasă numită informatii_generale() care returnează un mesaj general despre vehicule.
#   2. Creează două clase derivate: Masina și Bicicleta, care să moștenească clasa Vehicul.
#   •  Fiecare clasă derivată ar trebui să aibă o implementare proprie a metodei pornire().
#   •  În clasa Masina, adaugă o metodă specifică numită alimentare() care primește un parametru și afișează un mesaj că mașina a fost alimentată cu combustibilul specificat.
#   •  În clasa Bicicleta, implementează o metodă specifică numită schimba_viteza() care primește o valoare și afișează un mesaj că bicicleta și-a schimbat viteza.
#   3. Creează instanțe ale claselor Masina și Bicicleta și apelează metodele lor specifice și metoda pornire().
#   4. Apelează metoda statică informatii_vehicul() și metoda de clasă informatii_generale() pentru fiecare clasă derivată.
#
# from abc import ABC, abstractmethod
#
# class Vehicul(ABC):
#     tip_vehicul="vehicul generic"
#     @abstractmethod
#     def pornire(self):
#         pass
#
#     @staticmethod
#     def informatii_vehicul(marca):
#         print(f"Vehiculul este marca {marca}.")
#
#     @classmethod
#     def informatii_generale(cls):
#         print(f"Vehiculul este un mijloc de transport. Tip vehicul: {cls.tip_vehicul} ") #atribut de clasa, nu de instanta
#
# class Masina(Vehicul):
#     tip_vehicul="masina"
#     def pornire(self):
#         print("Masina este pornita")
#
#     def alimentare(self,combustibil):
#         print(f"Masina merge cu {combustibil}")
#
# class Bicicleta(Vehicul):
#     tip_vehicul = "bicicleta"
#     def pornire(self):
#         print("Bicicleta este gata sa fie folosita")
#
#     def schimba_viteza(self,viteza):
#         print(f"Bicicleta schimba viteza in {viteza}. ")
#
# masina_mea=Masina()
# bicicleta_mea=Bicicleta()
# masina_mea.informatii_vehicul("Toyota")
# masina_mea.informatii_generale()
# bicicleta_mea.pornire()
# bicicleta_mea.schimba_viteza(3)
# Bicicleta.informatii_generale()
# """
# from timeit import timeit
# code="""
# from timeit import sleep
# def method():
#     sleep(1)
# method()
# """
# print(timeit(code,number=1))
# """
# param=(i*i for i in range(5))
# print(type(param))
# a=[1,2]
# b=[x**2 for x in a if x<2]
# print(b)
# lst=[1,2,3,4,5]
# def max_lista(lst):
#     current_max=lst[0]
#     for numar in lst:
#         if numar > current_max:
#             current_max=numar
#     return current_max
# print(max_lista(lst))

# 1. Numărătoare inversă
# Scrie o funcție recursivă care afișează numerele de la n până la 1.
# def scrie_numere_n_la_1(n):
#     if n == 1:
#         print(n)
#     else:
#         print(n)
#         n=n-1
#         scrie_numere_n_la_1(n)
#
#
# scrie_numere_n_la_1(10)

# 2.Verificarea unui număr par
# Scrie o funcție recursivă care verifică dacă un număr este par.
# Putem verifica daca un numar este par, daca realizand scaderi repetate ajungem la la valoarea finala de 0
# Daca ajungem la valoarea 1, inseamna ca numarul este impar
# Ex:
# 7 => 7 -2 = 5 ; 5 - 2 = 3; 3 - 2 = 1 => este impar
# 8 => 8 - 2 = 6; 6 - 2 = 4; 4 - 2 = 2; 2 - 2 = 0 => este par
# def verificare_numar_par(n):
#     if n == 0:
#         return True
#     elif n == 1:
#         return False
#     else:
#         n-=2
#         return verificare_numar_par(n)
#
#
# print(verificare_numar_par(9))


# 3. Produsul cifrelor unui numar
# Scrieti o functie recursiva ce calculeaza produsul cifrelor unui numar.

# def produsul_cifrelor_unui_numar(n):
#     if n<10:
#         return n
#     else:
#         return (n%10) * produsul_cifrelor_unui_numar(n//10)
#
# print(produsul_cifrelor_unui_numar(12345))

# 4. Suma elementelor unui sir
#Scrieți o funcție recursivă care să calculeze suma tuturor elementelor unui șir de numere întregi.
# Implementați această funcție folosind recursivitatea.
#ex: Suma elementelor din șirul [1, 2, 3, 4, 5] este: 15
# sir=[1, 2, 3, 4, 5]
# def suma_elemente_sir(sir):
#     if len(sir)==0:
#         return 0
#     else:
#         return sir[0]+suma_elemente_sir(sir[1:])
#
# print(suma_elemente_sir(sir))


# 5. Factorial
# Scrie o functie care să calculeze factorialul unui număr întreg pozitiv folosind recursivitatea.
# Factorialul unui număr n (notat n!) este definit astfel:
# 	•	0! = 1 (factorialul lui 0 este 1)
# 	•	n! = n * (n-1)! pentru n > 0
# Input: n = 5
# 	•	Output: 120 (deoarece 5! = 5 * 4 * 3 * 2 * 1 = 120)

# def numar_factorial(n):
#     if n==0:
#         return 1
#     else:
#         return n * numar_factorial(n-1)
# print(numar_factorial(5))


# # 6. Cerință: Scrieți o funcție recursivă care să calculeze numărul Fibonacci de la un anumit indice n. Secvența Fibonacci începe cu 0 și 1, iar fiecare număr Fibonacci următor este suma celor două numere precedente. Implementați această funcție folosind recursivitatea.
# 	•	 F(0) = 0
# 	•	 F(1) = 1
# 	•	 F(2) = F(1) + F(0) = 1 + 0 = 1
# 	•	 F(3) = F(2) + F(1) = 1 + 1 = 2
# 	•	 F(4) = F(3) + F(2) = 2 + 1 = 3
# 	•	 F(5) = F(4) + F(3) = 3 + 2 = 5

# def fibonacci_recursive(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
# print(fibonacci_recursive(5))

# 7. Descompunerea unui număr în sumă de puteri ale lui 2:
# Scrie o funcție recursivă care să descompună un număr dat în sumă de puteri ale lui 2. In cazul in care numarul nu este o putere
# de a lui 2, se va returna cea mai apropiata putere de numarul respectiv.
# Ex: n = 10 -> se va reuturna 3 deoarece 2 ^ 3 = 8 este cea mai apropiata putere de numarul n
# # Exemplu de utilizare:
# print(decompose_in_powers_of_two(8))  # Output: 3

# 1. **Descompunerea unui număr în sumă de puteri ale lui 2**:
# Scrie o funcție recursivă care să descompună un număr dat în sumă de puteri ale lui 2.


# Caculam puterea lui 8
# 8 = 2 ^ 3 => 3
#
# current_power = 0 cum  2 la puterea current_power este mai mic decat n, incrementam current_power
# 2 ^ 0 = 1

# current_power = 1 cum 2 la puterea current_power este mai mic decat n, incrementam current_power
# 2 ^ 1 = 2

# current_power = 2, cum 2 la puterea current_power este mai mic decat n, incrementam current_power
# 2 ^ 2 = 4

# current_power = 3
# 2 ^ 3 = 8 => cum 2 la puterea current_power(3) este mai mare sau egal decat n, returnam current_power


# def decompose_in_powers_of_two(n, current_power=0):
#     # Verificam daca 2 ** current_power >= n
#     # daca este adevarat, returnam current_power
#     # altfel, apelam functia recursiv cu acelasi n, dar cu curren_power incrementat cu 1
#     if 2**current_power >= n:
#         return current_power
#     else:
#         return decompose_in_powers_of_two(n, current_power + 1)
# print(decompose_in_powers_of_two(12))





# 8. Numărul de aparitii ale unui element într-o listă:
# Scrie o funcție recursivă care să calculeze numărul de apariții ale unui element dat într-o listă dată.
# print(number_of_occurances(3, [1,2,3])) #=> va returna 1
# print(number_of_occurances(4, [1,2,3])) #=> va returna 0
# lista=[1,2,3,4,5,5]
# def numarul_de_aparitii(n,lista):
#     if len(lista)==0:
#         return 0
#     if lista[0] == n:
#         return numarul_de_aparitii(n,lista[1:])+1
#     else:
#         return numarul_de_aparitii(n,lista[1:])
# print(numarul_de_aparitii(5,lista))






# 9. Calculul puterii
# Scrieți o funcție recursivă care să calculeze x ^ n, unde x si n sunt numere întreg.
# 	Pentru a calcula puterea lui x ridicată la n folosind metoda recursivă putem folosi următoarea abordare:
# 	1. Dacă n este 0, rezultatul este întotdeauna 1.
# 	3. În caz contrar, putem folosi metoda de divizare și stăpânire astfel:
# 		- Dacă n este par, putem calcula x la puterea n/2 și apoi putem înmulți rezultatul cu el însuși.
# 		- Dacă n este impar, putem calcula x la puterea (n-1)/2 și apoi putem înmulți rezultatul cu el însuși, și încă o dată cu x pentru a obține rezultatul final.
# # Exemplu de utilizare:
# x = 2
# n = 5
# result = power(x, n)

# def calculare_putere(x,n):
#     if n==0:
#         return 1
#     rezultat=calculare_putere(x,n//2)
#     if n % 2 == 0:
#         return rezultat*rezultat
#     else:
#         return rezultat*rezultat*x
#
# print(calculare_putere(2,5))

# 9. **Numărul de aparitii ale unui element într-o listă**:
# 	Scrie o funcție recursivă care să calculeze numărul de apariții ale unui element dat într-o listă dată.
# # Example usage
# lst = [1, 2, 3, 4, 2, 2, 5]
# element = 2
# print(f"The number of occurrences of {element} in the list is: {count_occurrences(lst, element)}")
#
# def numarul_de_aparitii(n,lista):
#     if len(lista)==0:
#         return 0
#     if lista[0] == n:
#         return numarul_de_aparitii(n,lista[1:])+1
#     else:
#         return numarul_de_aparitii(n,lista[1:])
#
# print(f"The number of occurrences of {5} in the list is: {numarul_de_aparitii(5,[1, 2,5,5,5,5, 3, 4, 2, 2, 5])}")

# 10. **Determinarea celei mai lungi secvențe crescătoare dintr-o listă:**
# 	Scrie o funcție recursivă care să determine lungimea celei mai lungi secvențe crescătoare dintr-o listă dată.
# # Exemplu de utilizare:
# print(longest_increasing_sequence([1, 3, 5, 2, 4, 7, 9]))  # Output: 4 (pentru secvența 1, 3, 5, 7)
#


# 11. **Calcularea Puterii**:
# 	- Cerință: Scrieți o funcție recursivă care să calculeze x ^ n , unde x și n sunt numere întregi, folosind metoda recursivă de divizare și stăpânire. Implementați această funcție folosind recursivitatea.
# 	Pentru a calcula puterea lui x ridicată la n folosind metoda recursivă de divizare și stăpânire în Python, putem folosi următoarea abordare:
# - Dacă n este 0, rezultatul este întotdeauna 1.
# - În caz contrar, putem folosi metoda de divizare și stăpânire astfel:
# 		- Dacă n este par, putem calcula x la puterea n/2 și apoi putem înmulți rezultatul cu el însuși.
# 		- Dacă n este impar, putem calcula x la puterea (n-1)/2 și apoi putem înmulți rezultatul cu el însuși, și încă o dată cu x pentru a obține rezultatul final.
#
# 12. **Paranteze corect asociate**:
# 	- Cerință: Scrieți o funcție care să determine dacă un șir de paranteze este corect asociat sau nu. Un șir de paranteze este considerat corect asociat dacă fiecare paranteză deschisă are o paranteză corespunzătoare închisă și în ordinea corectă. Implementați această funcție folosind recursivitatea.
#
# 	Această funcție `is_valid_parentheses` primește un șir de paranteze și folosește o stivă pentru a verifica corespondența corectă între paranteze. Funcția utilizează o funcție auxiliară `is_matching` pentru a verifica dacă o paranteză deschisă are o paranteză corespunzătoare închisă. Apoi, o funcție recursivă `check_recursively` este utilizată pentru a parcurge recursiv șirul de paranteze. Dacă la final stiva este goală, înseamnă că toate parantezele au fost asociate corect și returnăm `True`, altfel returnăm `False`.
#
# # Exemple de utilizare:
# print(is_valid_parentheses("(){}[]"))  # True
# print(is_valid_parentheses("([{}])"))  # True
# print(is_valid_parentheses("({[}])"))  # False
# print(is_valid_parentheses("(()"))     # False


# Cerință: Scrieți cod pentru a elimina duplicatele dintr - o listă înlănțuită neordonată.
#
# Iată câteva exemple cu input și output:
#
# Exemplu
# 1:
#
# Input: 1 -> 2 -> 3 -> 2 -> 4 -> 1 -> None
# Output: 1 -> 2 -> 3 -> 4 -> None
# Exemplu
# 2:
#
# Input: 3 -> 1 -> 3 -> 5 -> 5 -> 2 -> None
# Output: 3 -> 1 -> 5 -> 2 -> None
# Exemplu
# 3:
#
# Input: 7 -> 7 -> 7 -> 7 -> 7 -> None
# Output: 7 -> None

# class Node:
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def append(self, data):
#         new_node = Node(data)
#         if not self.head:
#             self.head = new_node
#             return
#         last = self.head
#         while last.next:
#             last = last.next
#         last.next = new_node
#
#     def remove_duplicates(self):
#         current = self.head
#         prev = None
#         seen_data = set()
#
#         while current:
#             if current.data in seen_data:
#                 prev.next = current.next
#             else:
#
#                 seen_data.add(current.data)
#                 prev = current
#             current = current.next
#
#     def print_list(self):
#         current = self.head
#         while current:
#             print(current.data, end=" -> ")
#             current = current.next
#         print("None")
#
#
# llist1 = LinkedList()
# for value in [1,2,2,2,3,4,2]:
#     llist1.append(value)
#
# print("Exemplu 1 - Lista inițiala:")
# llist1.print_list()
# llist1.remove_duplicates()
# print("Exemplu 1 - Lista dupa eliminarea duplicatelor:")
# llist1.print_list()
#
# llist2 = LinkedList()
# for value in [3, 1, 3, 5, 5, 2]:
#     llist2.append(value)
#
# print("\nExemplu 2 - Lista initiala:")
# llist2.print_list()
# llist2.remove_duplicates()
# print("Exemplu 2 - Lista după eliminarea duplicatelor:")
# llist2.print_list()
#
# llist3 = LinkedList()
# for value in [7, 7, 7, 7, 7]:
#     llist3.append(value)
#
# print("\nExemplu 3 - Lista initiala:")
# llist3.print_list()
# llist3.remove_duplicates()
# print("Exemplu 3 - Lista după eliminarea duplicatelor:")
# llist3.print_list()


# class Node:
#     def __init__(self, data,next=None):
#         self.data = data
#         self.next = next
#
# node_3=Node(data=3,next=None)
# node_2=Node(data=2,next=node_3)
# node_1=Node(data=1,next=node_2)
#
# def print_list(root_node):
#     current=root_node
#     while current.next:
#         print(current.data,end="->")
#         current=current.next
#         print(current.__dict__)
# print_list(node_1)


# 5. Găsirea elementului de la mijloc într-o listă legată simplă
#
# 	Creează o metodă pentru a găsi elementul de la mijloc într-o listă legată simplă. Dacă lista are un număr par de noduri, returnează al doilea nod din mijloc.

# class Node:
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next
#
# node_3=Node(data=3,next=None)
# node_2=Node(data=2,next=node_3)
# node_1=Node(data=1,next=node_2)
#
# class SingleLinkedList:
#     def __init__(self):
#         self.head=None
#
#     def append(self,data):
#         new_node=Node(data)
#         if not self.head:
#             self.head=new_node
#             return
#         current=self.head
#         while current.next:
#             current=current.next
#         current.next=new_node
#         return
#
#     def reverse(self):
#         prev = None
#         current = self.head
#         while current:
#             next_node = current.next
#             current.next = prev
#             prev = current
#             current = next_node
#         self.head = prev
#
#     def display(self):
#         current=self.head
#         while current:
#             print(current.data,end="->")
#             current=current.next
#         print("None")
#
#     def find_half(self):
#         counter=0
#         current=self.head
#         while current:
#             counter+=1
#             current=current.next
#         middle_node=counter//2
#         counter = 0
#         current = self.head
#         while current:
#             if counter==middle_node:
#                 return current.data
#             counter+=1
#             current=current.next
# list_1 = SingleLinkedList()
# list_1.append(1)
# list_1.append(2)
# list_1.append(3)
# list_1.append(4)
# print("----- Initial list ----")
# list_1.display()
# print(list_1.find_half())


# 6. Îmbinarea a două liste legate sortate într-o singură listă legată sortată
#
#Creează o metodă care îmbină două liste legate sortate într-o singură listă legată sortată. Metoda ar trebui să ia două liste legate ca argumente
# și să returneze capul noii liste îmbinate,păstrând ordinea sortată.

# def combine(list_1,list_2):
#     current_list_1=list_1.head
#     current_list_2=list_2.head
#
#     combined_list= SingleLinkedList()
#     while current_list_1 and current_list_2:
#         if current_list_1.data<current_list_2.data:
#             combined_list.append(current_list_1.data)
#             current_list_1=current_list_1.next
#         elif current_list_1.data>=current_list_2.data:
#             combined_list.append(current_list_2.data)
#             current_list_2=current_list_2.next
#     while current_list_1:
#         combined_list.append(current_list_1.data)
#         current_list_1=current_list_1.next
#     while current_list_2:
#         combined_list.append(current_list_2.data)
#         current_list_2=current_list_2.next
#
#     return combined_list
#
#
# list_1 = SingleLinkedList()
# list_1.append(1)
# list_1.append(3)
# list_1.append(5)
# list_1.append(7)
#
# list_2 = SingleLinkedList()
# list_2.append(2)
# list_2.append(3)
# list_2.append(4)
# list_2.append(6)
# list_2.append(8)
#
# combined_linked_list = combine(list_1, list_2)
# combined_linked_list.display()
#
# combined_linked_list.reverse()
# combined_linked_list.display()
# 7. Reversarea unei liste legate simplu (Singly Linked List)
#
# 	Creează o metodă pentru a inversa o listă legată simplu.
#
#     ```python
#     Ex: 1 -> 2 -> 3 va deveniii 3 -> 2 -> 1
#     ```

# Creează o aplicație care simulează gestionarea unui logger pentru aplicație.
# Aplicația trebuie să aibă un singur logger activ care poate înregistra mesaje de tipul info, warning, error etc.
# Fiecare mesaj trebuie să fie salvat împreună cu un timestamp (data și ora curentă).
# import datetime
#
# def SingletonDecorator(class_to_decorate):
#     __instances={}
#
#     def get_instance(*args, **kwargs):
#         if class_to_decorate in __instances:
#             return __instances[class_to_decorate]
#         else:
#             __instances[class_to_decorate]=class_to_decorate(*args, **kwargs)
#             return __instances[class_to_decorate]
#
#     return get_instance
#
# @SingletonDecorator
# class Logger:
#     def __init__(self):
#         self.log=[]
#
#     def log_info(self, message):
#         timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         self.log.append(f"[INFO] {timestamp} - {message}")
#
#     def log_warning(self, message):
#         timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         self.log.append(f"[WARNING] {timestamp} - {message}")
#
#     def log_error(self, message):
#         timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         self.log.append(f"[ERROR] {timestamp} - {message}")
#
#     def show_logs(self):
#         return "\n".join(self.log)
#
# logger1 = Logger()
# logger1.log_info("Aplicația a început.")
# logger1.log_warning("Aceasta este o avertizare.")
# logger1.log_error("A apărut o eroare!")
#
# # Afisăm mesajele
# print("Mesaje înregistrate:")
# print(logger1.show_logs())
#
# # Creăm o altă instanță și verificăm dacă este aceeași
# logger2 = Logger()
# logger2.log_info("Înregistrăm un alt mesaj.")
#
# # Verificăm dacă logger2 și logger1 sunt aceeași instanță
# print("\nMesaje după instanțierea logger2:")
# print(logger2.show_logs())
#
# print(f"logger1 este același cu logger2? {logger1 is logger2}")



# Construcția unui set de mașini de tipuri diferite (Ex: Mașină electrică, Mașină sport, Mașină de teren).
#
# Descrierea cerinței:
#
# Vrei să creezi un sistem care să construiască diverse tipuri de mașini. Fiecare tip de mașină are caracteristici (de exemplu, tipul motorului, tipul de roți, și culoarea).
# Vrei să folosești un pattern Builder pentru a construi aceste mașini, iar un Director pentru a le construi pas cu pas, astfel încât fiecare mașină să fie construită corespunzător tipului său.
#
# Detalii suplimentare:
# Mașina va avea 3 caracteristici: motor, roți și culoare.
# Fiecare tip de mașină va avea valori implicite pentru aceste caracteristici (ex: Mașina electrică va avea un motor electric și roți pentru drumuri asfaltate).
# Un Director va controla procesul de construire al mașinii, alegând tipul de motor, roți și culoare pentru fiecare tip de mașină.

# from abc import ABC, abstractmethod
#
# class Masina:
#     def __init__(self):
#         self.tipul_motorului=None
#         self.tipul_de_roti=None
#         self.culoare=None
#
#     def __str__(self):
#         return f"tipul motorului: {self.tipul_motorului},tipul de roti {self.tipul_de_roti},culoare: {self.culoare}"
#
# class Masina_builder(ABC):
#     @abstractmethod
#     def set_tipul_motorului(self,tipul_motorului):
#         pass
#     @abstractmethod
#     def set_tipul_de_roti(self,tipul_de_roti):
#         pass
#     @abstractmethod
#     def set_culoare(self,culoare):
#         pass
#     @abstractmethod
#     def get_masina(self):
#         pass
#
# class Masina_electrica(Masina_builder):
#     def __init__(self):
#         self.masina=Masina()
#
#     def set_tipul_motorului(self,tipul_motorului):
#         self.masina.tipul_motorului=tipul_motorului
#
#     def set_tipul_de_roti(self,tipul_de_roti):
#         self.masina.tipul_de_roti=tipul_de_roti
#
#     def set_culoare(self,culoare):
#         self.masina.culoare=culoare
#
#     def get_masina(self):
#         return self.masina
#
# class Masina_sport(Masina_builder):
#     def __init__(self):
#         self.masina=Masina()
#
#     def set_tipul_motorului(self,tipul_motorului):
#         self.masina.tipul_motorului=tipul_motorului
#
#     def set_tipul_de_roti(self, tipul_de_roti):
#         self.masina.tipul_de_roti = tipul_de_roti
#
#     def set_culoare(self, culoare):
#         self.masina.culoare = culoare
#
#     def get_masina(self):
#         return self.masina
#
# class Masina_de_teren(Masina_builder):
#     def __init__(self):
#         self.masina=Masina()
#
#     def set_tipul_motorului(self,tipul_motorului):
#         self.masina.tipul_motorului=tipul_motorului
#
#     def set_tipul_de_roti(self, tipul_de_roti):
#         self.masina.tipul_de_roti = tipul_de_roti
#
#     def set_culoare(self, culoare):
#         self.masina.culoare = culoare
#
#     def get_masina(self):
#         return self.masina
#
# class Masina_director:
#     def __init__(self,builder):
#         self.builder=builder
#
#     def construct_masina(self,motor,culoare):
#         self.builder.set_tipul_motorului(motor)
#         self.builder.set_culoare(culoare)
#
#         if isinstance(self.builder,Masina_electrica):
#             self.builder.set_tipul_de_roti("Michelin")
#
#         if isinstance(self.builder,Masina_sport):
#             self.builder.set_tipul_de_roti("Semi-Slick")
#
#         if isinstance(self.builder,Masina_de_teren):
#             self.builder.set_tipul_de_roti("Off-road Pro-Line")
#         return self.builder.get_masina()
#
# masina_electrica=Masina_electrica()
# masina_sport=Masina_sport()
# masina_de_teren=Masina_de_teren()
#
# masina_electrica_director=Masina_director(masina_electrica)
# masina_sport_director=Masina_director(masina_sport)
# masina_de_teren_director=Masina_director(masina_de_teren)
#
# masina_sport_rosie_6_0_v12=masina_sport_director.construct_masina("6.0 V12","Rosie")
# print(masina_sport_rosie_6_0_v12)
#
# masina_electrica_galbena_electric=masina_electrica_director.construct_masina("1000cp Plaid","Galbena")
# print(masina_electrica_galbena_electric)
#
# masina_offroad_neagra_4_4_v8=masina_de_teren_director.construct_masina("4.4 V8","Neagra")
# print(masina_offroad_neagra_4_4_v8)

#Scrie un program care să primească o listă de numere și să calculeze suma tuturor numerelor impare din acea listă. Exemplu:
# lista = [1,2,3,4,5,6,7,8,9,10,12,432,6,34,634,63,46]
# suma_numere = 0
# for numar in lista:
#     if numar % 2 != 0:
#         suma_numere += numar
#         print(f"Suma numerelor impare din lista noastra este {suma_numere}")

#1. Clasa pentru un Cont Bancar
# Creează o clasă ContBancar care să aibă următoarele caracteristici:
#
# Atribute: numar_cont (string), sold (float).
# Metode:
# depune(suma): adaugă o sumă în cont.
# retrage(suma): retrage o sumă din cont, dar doar dacă există suficient sold.
# afiseaza_sold(): afișează soldul curent.
# transfera(cont_destinatie, suma): transferă o sumă către un alt cont, dar doar dacă există suficient sold.

# class ContBancar:
#     def __init__(self,numar_cont,sold):
#         self.numar_cont=numar_cont
#         self.sold=sold
#
#     def depune(self,suma):
#         self.sold+=suma
#         print(f"Suma de {suma} lei a fost adaugata in cont. Soldul dvs. este de {self.sold}")
#
#     def retrage(self,suma):
#         if suma>self.sold:
#             print("Sold insuficient!")
#         else:
#             self.sold-=suma
#             print(f"Suma de {suma} lei a fost extrasa din cont. Soldul dvs. este de {self.sold}")
#
#     def afiseaza_sold(self):
#         print (f"Soldul curent este de  {self.sold} ron.")
#
#     def transfera(self,cont_destinatie,suma):
#         if suma<=self.sold:
#             self.sold-=suma
#             cont_destinatie.sold +=suma
#             print(f"Transfer de {suma} realizat din contul {self.numar_cont} în contul {cont_destinatie.numar_cont}.")
#         else:
#             print("Fonduri insuficiente pentru transfer!")
#
# cont1=ContBancar(31032005,800000)
# cont2=ContBancar(31063405,50000)
#
# cont1.afiseaza_sold()
# cont1.depune(200000)
# cont1.retrage(1342)
# cont1.transfera(cont2,200000)


#
# Creează o clasă Produs care să reprezinte un produs dintr-un magazin online și o clasă CosDeCumparaturi pentru a gestiona coșul de cumpărături.
#
# Clasa Produs:
# Atribute: denumire (string), pret (float), stoc (int).
# Metode:
# modifica_stoc(cantitate): scade stocul cu o cantitate dată.
# Clasa CosDeCumparaturi:
# Atribute: produse (listă de obiecte Produs), total (float).
# Metode:
# adaugă_produs(prod): adaugă un produs în coș.
# calculează_total(): calculează suma totală a produselor din coș.
# afisează_cos(): afișează produsele și prețurile din coș.
# # finalizează_comanda(): calculează totalul și scade stocul produselor.

# class Produs:
#     def __init__(self,denumire,pret,stoc):
#         self.denumire = denumire
#         self.pret = pret
#         self.stoc = stoc
#
#     def modifica_stoc(self,cantitate):
#         self.stoc -= cantitate
#         return self.stoc
#
# class CosDeCumparaturi:
#     def __init__(self):
#         self.produse = []
#         self.total = 0
#
#     def adauga_produs(self,produs):
#         if produs.stoc>0:
#             self.produse.append(produs)
#             self.total+=produs.pret
#             produs.modifica_stoc(1)
#
#     def calculeaza_total(self):
#         print(f"Totalul cosului este de {self.total}")
#
#     def afiseaza_cos(self):
#         print("Produse în coș:")
#         for prod in self.produse:
#             print(f"{prod.denumire} - {prod.pret} lei")
#
#     def finalizeaza_comanda(self):
#         print(f"Comanda finalizată! Total: {self.total} lei.")
#         for prod in self.produse:
#             print(f"Stoc disponibil pentru {prod.denumire}: {prod.stoc}")
#
# produs1 = Produs("Laptop", 3000, 10)
# produs2 = Produs("Telefon", 1500, 5)
#
# cos = CosDeCumparaturi()
# cos.adauga_produs(produs1)
# cos.adauga_produs(produs2)
#
# cos.calculeaza_total()
# cos.afiseaza_cos()
# cos.finalizeaza_comanda()


# try:
#     numar = int(input("Introduceti un numar: "))
#     patrat_numar=numar**2
# except ValueError:
#     print("Introduceti o valoare de tipul int.")
# else:
#     print(f"Patratul numarului introdus de dvs este {patrat_numar}")

# try:
#     with open('fisier.txt',"r") as file:
#         continut=file.read()
#         print(continut)
# except FileNotFoundError:
#     print("Eroare: Fișierul nu a fost găsit!")
# finally:
#     print("Închidere fișier - chiar dacă a apărut o eroare sau nu.")




#Listă de numere pare
# Scrie o funcție care primește o listă de numere și returnează o nouă listă care conține doar numerele pare.

# def numere_pare(lista):
#     rezultat=[]
#     for numar in lista:
#         if numar%2==0:
#             rezultat.append(numar)
#     return rezultat
# print(numere_pare([1,2,3,4,5,6,7,8,9]))

# Clasa pentru gestionarea angajaților
# Creează o clasă Angajat care are atributele nume, salariu și o metodă afiseaza_detalii() care afișează informațiile despre angajat.

# class Angajat:
#     def __init__(self,nume,salariu):
#         self.nume = nume
#         self.salariu = salariu
#
#     def afiseaza_detalii(self):
#         print(f"Angajatul pe nume {self.nume} are urmatorul salariu: {self.salariu} ron.")
#
# angajat1=Angajat("Maliuca",12500)
# angajat1.afiseaza_detalii()

# Număr prim
# Scrie o funcție care verifică dacă un număr este prim.

# def numar_prim(numar):
#     if numar < 2:
#         return False
#     for i in range(2,int(numar ** 0.5)+1):
#         if numar % i == 0:
#             return False
#     return True
#
# print(numar_prim(5))
# print(numar_prim(7))
# print(numar_prim(9))


# Sortare cu lambda
# Ai o listă de tuple, fiecare conținând numele și vârsta unei persoane. Sortează lista crescător după vârstă folosind lambda și sorted().
#
# persoane = [("Mario",20),("Maria",19),("Catalin",46)]
# persoane_sortate=sorted(persoane,key=lambda x: x[1])
# print(persoane_sortate)

# Fibonacci cu recursivitate
# Scrie o funcție recursivă care returnează al n-lea termen din șirul Fibonacci.
#
# def fibonacci(n):
#     if n==0:
#         return "Numar invalid"
#     elif n==1:
#         return 0
#     elif n==2:
#         return 1
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)
#
# print(fibonacci(8))

# Decorator pentru măsurarea timpului de execuție
# Scrie un decorator care măsoară timpul de execuție al unei funcții.
# import time
# def timp_executie(func):
#     def wrapper(*args,**kwargs):
#         start = time.time()
#         rezultat = func(*args,**kwargs)
#         end = time.time()
#         print(f"Executia a durat {end-start:.5f} secunde")
#         return rezultat
#     return wrapper
# @timp_executie
# def calculeaza():
#     time.sleep(4)
#     print("Calcul efectuat!")
# calculeaza()

# Generator pentru numere pare
# Creează un generator care returnează numerele pare până la un număr dat.

# def generator_pare(numar):
#     for i in range(0,numar+1,2):
#         yield i
#
# for num in generator_pare(10):
#     print(num,end=" ")

# Folosirea map() și filter()
# Dă o listă de numere întregi și folosește map() pentru a le ridica la pătrat și filter() pentru a păstra doar cele mai mari de 50.

# lista= [1,25,53,52,75,423,756]
# patrate=list(map(lambda x:x**2,lista))
# print(patrate)
# pestecincizenci=list(filter(lambda x:x>50,lista))
# print(pestecincizenci)

# Gestionarea erorilor
# Scrie o funcție care primește două numere și returnează rezultatul împărțirii. Tratează eroarea de împărțire la zero cu try-except.

def impartire(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print("a nu poate fi egal cu 0.")
print(impartire(2,0))


# Fișiere - citire și scriere
# Scrie un program care creează un fișier text, scrie câteva linii în el și apoi le citește și le afișează pe ecran.