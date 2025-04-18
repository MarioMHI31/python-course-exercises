def main():
	fisier = open('../.venv/numerele_mele.txt', "w")
	contor = 0  # Inițializăm un contor
	for numar in range(1, 10):  # Iterăm prin numerele de la 1 la 9
		fisier.write(str(numar * numar ) + "\n")  # Scriem produsul
		contor += 1  # Incrementăm contorul
	fisier.write("Aceasta este tabla inmultirii")  # Scriem un mesaj la final
	fisier.close()  # Închidem fișierul
	print("Tabla inmultirii se realizeaza pana la numarul: ",contor)
main()