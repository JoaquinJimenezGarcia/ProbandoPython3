from module_tests.calculator import Calculator

class Main():
    flag = 1

    numero1 = int(input("Primer número: "))
    numero2 = int(input("Segundo número: "))

    calculator = Calculator(numero1, numero2)

    while flag != 0:
        print("Nº1 = " + str(numero1))
        print("Nº2 = " + str(numero2))
        print("############################")
        print("##   PYTHON  CALCULATOR   ##")
        print("############################")
        print("## Cambiar número 1       ##")
        print("## Cambiar número 2       ##")
        print("############################")
        print("## Sumar = 3              ##")
        print("## Restar = 4             ##")
        print("############################")
        print("## Parar = 0              ##")
        print("############################")

        flag = int(input("Seleccione la opcion: "))

        print("TOTAL:")

        if flag == 1:
            numero1 = int(input("Primer número: "))
            calculator.set_numero1(numero1)
        elif flag == 2:
            numero2 = int(input("Segundo número: "))
            calculator.set_numero2(numero2)
        elif flag == 3:
            print(calculator.add())
        elif flag == 4:
            print(calculator.minus())