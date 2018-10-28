#!/usr/bin/python3

main_code = ""

def zamek():
    print("Zamek szyfrowy ! \n")
    kod = input("Podaj swoj kod:")
    check = input("Podaj kod jeszcze raz:")

    if (kod == check):
        main_code = kod
        print("Twoj kod zostal zapisany ! \n")
    else:
        print("Podales niepoprawny kod! \n")
        zamek()

    return 0

zamek()