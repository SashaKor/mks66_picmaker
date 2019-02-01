# First image assignment
import random

COLS = 500
ROWS = 500
MAX = 255

def headers():
    f = open("img.txt",'a')
    f.write("P3"+"\n")
    # 4 3    3 rows of 4 triplets
    f.write(str(COLS)+" "+ str(ROWS)+"\n")
    f.write(str(MAX)+"\n")
    f.close()


def body():
    f = open("img.txt",'a')
    for r in range(ROWS):
        for c in range(COLS):
            red = r * 255 / COLS
            green = MAX
            blue = c * 255/ ROWS
            f.write(str(red)+" ")
            f.write(str(green)+" ")
            f.write(str(blue)+" \t")
        f.write("\n")
    f.close()




def main():
    headers()
    body()

main()
