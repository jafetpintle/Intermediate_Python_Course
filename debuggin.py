def divisor(num):
    try:
        if num < 0:
            raise ValueError("Solo se pueden ingresar números positivos")
        divisor = [i for i in range(1, num + 1) if num%i == 0]
        return divisor
    except ValueError as ve:
        print(ve)
        return[]

def run():
    try:
        print(divisor(int(input("Ingrese numero: "))))
    except ValueError:
        print("Error: debes de ingresar un número")

if __name__ == "__main__":
    run()