def divisors(num):
    try:
        if num < 0:
            raise ValueError("Solo se aceptan números positivos")
        divisors = []
        for i in range(1, num + 1):
            if num % i == 0:
                divisors.append(i)
        return divisors
    except ValueError as ve:
        print(ve)
        return "Code error 1"


def run():
    try:
        num = int(input('Ingresa un número: '))
        print(divisors(num))
        print("Terminó mi programa")
    except:
        print("Debes ingresar un número")

if __name__ == "__main__":
    run()