import threading
# variable global x
x = 0
def incremento():
    global x
    x += 1
def TareaThread():
    for _ in range(100000):
        incremento()
def TareaPrin():
    global x
    x = 0
    # creando hilos
    t1 = threading.Thread(target=TareaThread)
    t2 = threading.Thread(target=TareaThread)
    # inicio de los hilos
    t1.start()
    t2.start()
    # uniendo hilos
    t1.join()
    t2.join()
if __name__ == "__main__":
    for i in range(10):
        TareaPrin()
        print("Iteraccion {0}: x = {1}".format(i, x))