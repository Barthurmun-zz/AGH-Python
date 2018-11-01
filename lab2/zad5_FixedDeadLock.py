#!/usr/bin/python3

import threading
import time
import random

class Filozof(threading.Thread):

    def __init__(self,imie,p_widelec,l_widelec):
        threading.Thread.__init__(self)
        self.imie = imie
        self.p_widelec = p_widelec
        self.l_widelec = l_widelec

    def run(self):

        widelec1 , widelec2 = self.l_widelec, self.p_widelec

        while True:
            self.thinking()

            while True:
                print(f"{self.imie} probuje posiasc 1 widelec \n")
                widelec1.acquire()
                print(f"{self.imie} probuje posiasc 2 widelec \n")
                locked = widelec2.acquire(False)

                if locked == True:
                    break
                widelec1.release()

            self.eating()

            widelec2.release()
            print(f"{self.imie} zwalnia 2 widelec \n")

            widelec1.release()
            print(f"{self.imie} zwalnia 1 widelec \n")


    def thinking(self):
        print(f"{self.imie} rozmysla nad sensem zycia \n")
        time.sleep(random.random()*0.1)
        print(f"{self.imie} skonczyl rozmyslac nad sensem zycia \n")

    def eating(self):
        print(f"{self.imie} zaczal jesc \n")
        time.sleep(random.random()*0.1)
        print(f"{self.imie} skonczyl jesc \n")


if __name__ == '__main__':

    widelce = [threading.Lock() for i in range(5)]
    imiona = ["Janek", "Zygus", "Kubus", "Kicius", "Stasiu"]

    filozofowie = [Filozof(imiona[i], widelce[i%5], widelce[(i+1)%5]) for i in range(5)]

    for f in filozofowie:
        f.start()

    for f in filozofowie:
        f.join()

    print ('done')