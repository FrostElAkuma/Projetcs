from cs50 import get_int


def main():
    pInt = get_posotive_int()
    
    for i in range(pInt):
        print(" " * (pInt - 1 - i), end="")
        print("#" * (i+1), end="")
        print("  ", end="") 
        print("#" * (i+1))


def get_posotive_int():
    while True:
        n = get_int("Height: ")
        if n > 0 and n < 9:
            break
    return n                


main()    