import os
from time import sleep

def padre():

    try:
        cantidad = int(input("¿Cuántos procesos quieres?: "))

        for i in range(cantidad):

            newpid = os.fork()

            if newpid == 0:
                hijo()

    except:
        print("Ha ocurrido un error, inténtelo más tarde")

def hijo():

    print(">><< Nuevo hijo creado con pid %d" % os.getpid())
    sleep(5)

    print(">><< Hijo con pid %d finalizado" % os.getpid())
    os._exit(0)

if __name__ == "__main__":
    padre()