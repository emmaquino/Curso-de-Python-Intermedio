#This program prints a list with the multiples of 4, 6 and 9 using list comprenhision.

#Reto
lc = [i for i in range(1, 10000) if i % 36 == 0]
print(lc)