class Persona ():
    # contructor de Persona
    def __init__ (self, nom , ed ):
        self.nombre = nom
        self.edad = ed
    
    def saludarPersonas(self):
        return "Hola! "+ self.nombre + ' ' + str(self.edad)


# crear un objeto    
n = input("ingrese el nombre  : ")
per1 = Persona(n, 45)
per2 = Persona('Alexandra', 25)

print(per1.nombre)
print(per2.nombre)
print(per2.saludarPersonas())