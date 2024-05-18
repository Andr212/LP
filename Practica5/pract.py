class Fracciones:
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def Suma(self, a, b):
        nume = a.den * b.num + b.den * a.num
        deno = a.den * b.den
        return Fracciones(nume, deno)

    def Resta(self, a, b):
        nume = a.den * b.num - b.den * a.num
        deno = a.den * b.den
        if nume == 0 or deno == 0:
            return Fracciones(0, 0)
        else:
            return Fracciones(nume, deno)

    def Division(self, a, b):
        if b.num == 0:
            return Fracciones(0, 0)
        else:
            nume = a.num * b.den
            deno = a.den * b.num
        if nume == 0 or deno == 0:
            return Fracciones(0, 0)
        else:
            return Fracciones(nume, deno)

    def Multipliacacion(self, a, b):
        nume = a.num * b.num
        deno = a.den * b.den
        return Fracciones(nume, deno)

    def simplificar(self):
        if self.num == 0 or self.den == 0:
            return Fracciones(0, 0)
        else:
            for i in range(2, self.num):
                if self.num % i == 0 and self.den % i == 0:
                    self.num = self.num // i
                    self.den = self.den // i
            if self.num == self.den:
                return Fracciones(1, 1)
            return Fracciones(self.num, self.den)

p = 1
while p > 0 and p < 5:
    print("1. Suma de fracciones")
    print("2. Resta de fracciones")
    print("3. Division de fracciones")
    print("4. Multiplicacion de fracciones")
    print("Presiona cualquier otro numero para salir...")
    p = int(input("Ingrese la operacion que desea realizar: "))
    if p == 1:
        numerador1 = int(input("Ingrese el numerador de la primera fraccion: "))
        denominador1 = int(input("Ingrese el denominador de la primera fraccion: "))
        numerador2 = int(input("Ingrese el numerador de la segunda fraccion: "))
        denominador2 = int(input("Ingrese el denominador de la segunda fraccion: "))
        a = Fracciones(numerador1, denominador1)
        b = Fracciones(numerador2, denominador2)
        result = Fracciones(0, 0)
        print(
            f"La suma  de las fracciones {numerador1}/{denominador1} y {numerador2}/{denominador2} es: "
        )
        print(
            result.Suma(a, b).simplificar().num,
            "/",
            result.Suma(a, b).simplificar().den,
        )
    elif p == 2:
        numerador1 = int(input("Ingrese el numerador de la primera fraccion: "))
        denominador1 = int(input("Ingrese el denominador de la primera fraccion: "))
        numerador2 = int(input("Ingrese el numerador de la segunda fraccion: "))
        denominador2 = int(input("Ingrese el denominador de la segunda fraccion: "))
        a = Fracciones(numerador1, denominador1)
        b = Fracciones(numerador2, denominador2)
        result = Fracciones(0, 0)
        print(
            f"La resta de las fracciones {numerador1}/{denominador1} y {numerador2}/{denominador2} es: "
        )
        print(
            result.Resta(a, b).simplificar().num,
            "/",
            result.Resta(a, b).simplificar().den,
        )
    elif p == 3:
        numerador1 = int(input("Ingrese el numerador de la primera fraccion: "))
        denominador1 = int(input("Ingrese el denominador de la primera fraccion: "))
        numerador2 = int(input("Ingrese el numerador de la segunda fraccion: "))
        denominador2 = int(input("Ingrese el denominador de la segunda fraccion: "))
        a = Fracciones(numerador1, denominador1)
        b = Fracciones(numerador2, denominador2)
        result = Fracciones(0, 0)
        print(
            f"La division de las fracciones {numerador1}/{denominador1} y {numerador2}/{denominador2} es: "
        )
        print(
            result.Division(a, b).simplificar().num,
            "/",
            result.Division(a, b).simplificar().den,
        )
    elif p == 4:
        numerador1 = int(input("Ingrese el numerador de la primera fraccion: "))
        denominador1 = int(input("Ingrese el denominador de la primera fraccion: "))
        numerador2 = int(input("Ingrese el numerador de la segunda fraccion: "))
        denominador2 = int(input("Ingrese el denominador de la segunda fraccion: "))
        print(
            f"La multiplicacion de las fracciones {numerador1}/{denominador1} y {numerador2}/{denominador2} es: "
        )
        a = Fracciones(numerador1, denominador1)
        b = Fracciones(numerador2, denominador2)
        result = Fracciones(0, 0)
        print(
            result.Multipliacacion(a, b).simplificar().num,
            "/",
            result.Multipliacacion(a, b).simplificar().den,
        )
    else:
        print("saliendo...")
