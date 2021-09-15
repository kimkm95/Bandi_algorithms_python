print("Enter the number of coins you have.")
print("500 won? ",end ='')
Obak = int(input())
print("100 won? ", end = '')
bak = int(input())
print("50 won? ", end = ' ')
oship = int(input())
print("10 won? ", end = ' ')
ship = int(input())

sum = 500 * Obak + 100 * bak + oship * 50 + ship * 10
print(f"You have {sum} won in total.")