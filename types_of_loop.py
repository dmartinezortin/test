def main():

    # Generació de la seqüència de números, del 0 al 2
    # for i in range(3): print(i)

    # Generació de la llista de numeros, del 0 al 2
    # print([x for x in range(3) if x % 2 == 0])


    # Matriu que es recorrerà per printar els items:

    # classroom = [["Clase ", "Nom ", "Mitjana\n"], ["4t ESO ", "Albert ", "8.7\n"]]

    # [print(y, end="") for x in classroom for y in x]

    # Bucle sobre un diccionari

    # products = {"items": [{"name": "Donettes", "price": 2.5, "stock": 12}, {"name": "Fanta", "price": 1.2, "stock": 22}, {"name": "Galletas maria", "price": 1.5, "stock": 5}]}

    # [print("{}: {}".format(key, value)) for product_list in products["items"] for key, value in product_list.items()]

if __name__ == "__main__":
    main()
