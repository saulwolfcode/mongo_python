# -*- coding: utf-8 -*-
__author__ = 'saul alejos garay'

"""
class Futbolista:

    def __init__(self, nombre, apellidos, edad, demarcacion, internacional):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.demarcacion = demarcacion
        self.internacional = internacional

    def toDBCollection (self):
        return {
            "nombre":self.nombre,
            "apellidos":self.apellidos,
            "edad": self.edad,
            "demarcacion":self.demarcacion,
            "internacional":self.internacional
        }

    def __str__(self):
        return "Nombre: %s - Apellidos: %s - Edad: %i - Demarcaciรณn: %s - Internacional: %r" \
               %(self.nombre, self.apellidos, self.edad, self.demarcacion, self.internacional)
"""

class Equipo:
    def __init__(self,nombre,apellido,edad,experiencia,internacional):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        self.experiencia=experiencia
        self.internacional=internacional
def MongoCollection(self):
    return {
        "nombre":self.nombre,
        "apellido": self.apellido,
        "edad": self.edad,
        "experiencia": self.experiencia,
        "internacional": self.internacional
    }
def __str__(self):
    return "Nombre: %s - Apellido: %s - Edad: %i - Experiencia: %s - Internacional: %r"\
            %(self.nombre, self.apellido, self.edad, self.experiencia, self.internacional)