#This program prints the first 100 natural numbers using for loops

squares = []

def run():
    for i in range(1, 101):
        if i % 3 != 0:
            squares.append(i**2)
    
    print(squares)


if __name__ == '__main__':
    run()