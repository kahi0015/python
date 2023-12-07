import time
import os


def clear():
    os.system('cls' if os.name == 'nt'
              else 'clear')


def draw_square(size):
    clear()
    for _ in range(size):
        print("* " * size)
        time.sleep(0.1)


draw_square(15)