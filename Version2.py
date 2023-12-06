import random


def print_array(arr):
    for row in arr:
        row_string = ''.join(" ." if cell == 0 else " *" for cell in row)
        print(row_string)


def tab(x):
    for i in range(x):
        print(' ', end='')


def print_array(arr):
    for row in arr:
        print(row)


def find_nearest_row_with_one(array, target_row):
    distance = 1
    while True:
        if target_row + distance < len(array) and 1 in array[target_row + distance]:
            return target_row + distance
        distance += 1

tab(25)
print("BLACKBOX")
tab(20)
print("CREATIVE COMPUTING")
tab(18)
print("MORRISTOWN, NEW JERSEY")
print("\n\n\n")


def FNR():
    return int(8 * random.random()) + 1


def play_black_box():
    N = int(input("NO. OF ATOMS: "))
    B = [[0] * 8 for _ in range(8)]

    for i in range(1, N + 1):
        x, y = FNR(), FNR()
        while B[x - 1][y - 1] != 0:
            x, y = FNR(), FNR()
        B[x - 1][y - 1] = 1
    print_array(B)
    S = 0
    C = 0
    while True:
        R = int(input("RAY_row: ")) - 1

        if R < 0:
            print("NOW TELL ME, WHERE DO YOU THINK THE ATOMS ARE?")
            print("(IN ROW,COLUMN FORMAT PLEASE.)")
            for q in range(1, N + 1):
                try:
                    print(f"ATOM # {q} ", end="")
                    i, j = map(int, input().split())
                    if B[i - 1][j - 1] != 1:
                        S = S + 5
                    else:
                        B[i - 1][j - 1] = 2
                        C = C + 1
                except(ValueError, IndexError):
                    print("Enter mistake, try again")

            print("\n", end="")
            for row in B:
                row_string = ''.join(" ." if cell == 0 else " *" for cell in row)
                print(row_string)
            print(" YOU GUESSED", C, "OUT OF ", N, "ATOMS CORRECTLY!!")
            print(" YOUR SCORE FOR THIS ROUND WAS ", S, " POINTS.")
            a = input("CARE TO TRY AGAIN (Y/N)? ")
            if a == "Y":
                play_black_box()
            elif a == "N":
                break

        else:
            R1 = int(input("RAY_col: ")) - 1
            try:
                if B[R][R1] == 1:
                    print("absorbed")
                    S = S + 1
                if 1 in B[R] and B[R][R1] != 1:
                    print("reflected")
                    S = S + 1
                elif 1 not in B[R] and B[R][R1] != 1:
                    nearest_row = find_nearest_row_with_one(B, R)
                    print(f"To: {nearest_row + 1}")
                    S = S + 2
            except (ValueError, IndexError):
                print("Enter mistake, try again")


play_black_box()
