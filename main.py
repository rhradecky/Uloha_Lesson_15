#Používateľ zadá hodnoty do zoznamu. Potom začnú dve vlákna. Prvé vlákno nájde najväčšiu hodnotu v zozname.
#Druhé vlákno nájde najmenšiu hodnotu v zozname. Výsledky sa zobrazia na obrazovke.

import threading
def najst_max_cislo(lst):
    max_cislo = max(lst)
    print("Najvacsia hodnota:", max_cislo)

def najst_min_cislo(lst):
    min_cislo = min(lst)
    print("Najmensia hodnota:",min_cislo)


zoznam =[5,8,666,5,3,200,9,8]

thread_max = threading.Thread(target=najst_max_cislo, args=(zoznam,))
thread_min = threading.Thread(target=najst_min_cislo, args=(zoznam,))

thread_max.start()
thread_min.start()

thread_max.join()
thread_min.join()
