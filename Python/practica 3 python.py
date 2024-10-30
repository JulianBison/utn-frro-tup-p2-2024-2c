class Persona:
    def __init__(self,nombre,edad):
        self.set_nombre(nombre)
        self.set_edad(edad)
    def set_nombre(self,nombre):
        self.nombre = nombre
    def set_edad(self,edad):
        self.edad = edad
    def get_nombre(self):
        return self.nombre
    def get_edad(self):
        return self.edad
    def print_persona(self):
        print(f'La persona se llama {self.nombre} y tiene {self.edad} años')
    def es_mayor_de_edad(self):
        if(self.edad>18):
            return True
        else:
            return False
        
    def es_mayor_que (self,otra_persona):
        if(self.edad>otra_persona.edad):
            return True
        else:
            return False
    @staticmethod
    def get_mayor (persona1,persona2):
        if(persona1.edad>persona2.edad):
            return persona1.edad
        else:
            return persona2.edad
    


# Ejercicio 6: Clase Alumno
class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    
    def imprimir(self):
        print(f"Nombre: {self.nombre}, Nota: {self.nota}")
    
    def resultado(self):
        if self.nota >= 6:
            print(f"El alumno {self.nombre} ha aprobado.")
        else:
            print(f"El alumno {self.nombre} ha suspendido.")

# Ejercicio 7: Clase Triángulo
class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def lado_mayor(self):
        mayor = max(self.lado1, self.lado2, self.lado3)
        print(f"El lado mayor es: {mayor}")
    
    def tipo_triangulo(self):
        if self.lado1 == self.lado2 == self.lado3:
            print("El triángulo es equilátero.")
        elif self.lado1 == self.lado2 or self.lado2 == self.lado3 or self.lado1 == self.lado3:
            print("El triángulo es isósceles.")
        else:
            print("El triángulo es escaleno.")

# Ejercicio 8: Clase Calculadora
class Calculadora:
    def __init__(self, valor1, valor2):
        self.valor1 = valor1
        self.valor2 = valor2
    
    def sumar(self):
        return self.valor1 + self.valor2
    
    def restar(self):
        return self.valor1 - self.valor2
    
    def multiplicar(self):
        return self.valor1 * self.valor2
    
    def dividir(self):
        if self.valor2 != 0:
            return self.valor1 / self.valor2
        else:
            return "No se puede dividir por cero."

# Ejercicio 9: Clase Agenda
class Agenda:
    def __init__(self):
        self.contactos = []
    
    def anadir_contacto(self, nombre, telefono, email):
        self.contactos.append({"nombre": nombre, "telefono": telefono, "email": email})
    
    def listar_contactos(self):
        for contacto in self.contactos:
            print(f"Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}, Email: {contacto['email']}")
    
    def buscar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto['nombre'] == nombre:
                print(f"Encontrado: Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}, Email: {contacto['email']}")
                return
        print("Contacto no encontrado.")
    
    def editar_contacto(self, nombre, telefono=None, email=None):
        for contacto in self.contactos:
            if contacto['nombre'] == nombre:
                if telefono:
                    contacto['telefono'] = telefono
                if email:
                    contacto['email'] = email
                print("Contacto actualizado.")
                return
        print("Contacto no encontrado.")
    
    def cerrar_agenda(self):
        print("Agenda cerrada.")
        self.contactos = []

# Ejercicio 10: Clases Cliente y Banco
class Cliente:
    def __init__(self, nombre, cantidad=0):
        self.nombre = nombre
        self.cantidad = cantidad
    
    def depositar(self, monto):
        self.cantidad += monto
    
    def extraer(self, monto):
        if monto <= self.cantidad:
            self.cantidad -= monto
        else:
            print("Fondos insuficientes.")
    
    def mostrar_total(self):
        print(f"Cliente: {self.nombre}, Total en cuenta: {self.cantidad}")

class Banco:
    def __init__(self, cliente1, cliente2, cliente3):
        self.clientes = [cliente1, cliente2, cliente3]
    
    def operar(self):
        for cliente in self.clientes:
            cliente.mostrar_total()
    
    def deposito_total(self):
        total = sum(cliente.cantidad for cliente in self.clientes)
        print(f"El total depositado en el banco es: {total}")

# Prueba rápida para los ejercicios 6 al 10

# Persona     

persona1= Persona("Juan",30)
persona2= Persona("Ana",25)

persona1.print_persona()
persona2.print_persona()

# Alumno
alumno1 = Alumno("Juan", 7)
alumno1.imprimir()
alumno1.resultado()

# Triángulo
triangulo1 = Triangulo(3, 4, 5)
triangulo1.lado_mayor()
triangulo1.tipo_triangulo()

# Calculadora
calculadora = Calculadora(10, 5)
suma = calculadora.sumar()
resta = calculadora.restar()
multiplicacion = calculadora.multiplicar()
division = calculadora.dividir()
print(f'Su suma es: {suma}, su resta es {resta}, su multiplicacion es {multiplicacion},su division es {division}')
# Agenda
agenda = Agenda()
agenda.anadir_contacto("Maria", "123456789", "maria@gmail.com")
agenda.listar_contactos()
agenda.buscar_contacto("Maria")
agenda.editar_contacto("Maria", telefono="987654321")
agenda.listar_contactos()

# Banco y clientes
cliente1 = Cliente("Carlos", 500)
cliente2 = Cliente("Ana", 800)
cliente3 = Cliente("Luis", 300)
banco = Banco(cliente1, cliente2, cliente3)
banco.operar()
banco.deposito_total()




