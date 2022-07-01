def divisor(num):
    divisor = [i for i in range(1, num + 1) if num%i == 0]
    return divisor

def run():
    num = input("Ingrese un numero: ")
    assert num.isnumeric() , "Debes de ingresar un número positivo"
    print(divisor(int(num)))

if __name__ == "__main__":
    run()