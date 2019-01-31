# First image assignment


global COLS= 500
global ROWS= 500
global MAX= 255

def headers():
    f = open("img.txt",'a')
    f.write("P3")
    # 4 3    3 rows of 4 triplets
    f.write(str(COLS)+" "+str(ROWS))
    f.write(str(MAX))
    f.close()


def generate():
    f = open("img.txt",'a')
    for i in range(ROWS):
        for 



def main():
    headers()
    generate()
