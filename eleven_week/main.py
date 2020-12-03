from objetos_midia import Filme, Serie

def main():
    filme1 = Filme("Os caça fantasmas", 2001, 1000.3)
    serie1 = Serie("Supernatural", 2002, 8)
    serie2 = Serie("The walking dead", 2004, 9)
    serie3 = Serie("The Walkin DAD", 2005, 1)
    serie4 = Serie("Breaking Walking BAD", 2007, 3)
    serie2.add_spinoff(serie3)
    serie2.add_spinoff(serie4)
    serie5 = Serie("Programming Education", 2006, 1)

    print(filme1)
    for i in range(1, 6):
        print(eval(f'serie{i}'))
    serie2.has_spinoffs()


if __name__ == '__main__':
    main()