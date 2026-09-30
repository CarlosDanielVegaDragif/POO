from abc import ABC, abstractmethod
from enum import Enum

class CalidadVideo(Enum):
    HD = 1
    FULL_HD = 2
    ULTRA_HD = 3

class Contenido(ABC):


    def __init__(self, titulo, autor, viz):
        if not isinstance(titulo, str):
            raise TypeError("El título debe ser un texto.")
        if not titulo.strip():
            raise ValueError("El título no puede estar vacío.")

        if not isinstance(autor, str):
            raise TypeError("El autor debe ser un texto.")
        if not autor.strip():
            raise ValueError("El autor no puede estar vacío.")

        if not isinstance(viz, int):
            raise TypeError("Las visualizaciones deben ser un número entero.")
        if viz < 0:
            raise ValueError("Las visualizaciones no pueden ser negativas.")

        self.__titulo = titulo
        self.__autor = autor
        self._viz = viz

    def mostrar_titulo(self):
        return self.__titulo

    def mostrar_autor(self):
        return self.__autor

    def mostrar_visualizaciones(self):
        return self._viz

    @abstractmethod
    def calcular_puntos(self):
        pass

class PublicacionVideo(Contenido):

    def __init__(self, titulo, autor, viz, calidad:CalidadVideo):
        
        super().__init__(titulo, autor, viz)

        if not isinstance(calidad, CalidadVideo):
            raise TypeError("La calidad debe ser un valor del enum CalidadVideo.")
        self.__calidad = calidad

    def mostrar_calidad(self):
        return self.__calidad

    def calcular_puntos(self):
        return self._viz * 5

class PublicacionTexto(Contenido):

    def calcular_puntos(self):
        return self._viz * 2

def mostrar_puntos(publicacion):
    if isinstance(publicacion, PublicacionVideo):
        print(f"Los puntos de la publicacion {publicacion.mostrar_titulo()} en {publicacion.mostrar_calidad()} de {publicacion.mostrar_autor()} con {publicacion.mostrar_visualizaciones()} vistas: {publicacion.calcular_puntos()}")
    else:
        print(f"Los puntos de la publicacion {publicacion.mostrar_titulo()} de {publicacion.mostrar_autor()} con {publicacion.mostrar_visualizaciones()} vistas: {publicacion.calcular_puntos()}")

def test_correcto():
    video_divertido = PublicacionVideo("la caida de edgar", "edgar", 10000, CalidadVideo.FULL_HD)
    texto_cientifico = PublicacionTexto("ADN", "el hermano de edgar", 6500)

    mostrar_puntos(video_divertido)
    mostrar_puntos(texto_cientifico)

def test_errores():
        video_divertido = PublicacionVideo(88823, False, "mil", "HD")
        texto_cientifico = PublicacionTexto("ADN", "el hermano de edgar", 6500)
    
        mostrar_puntos(video_divertido)
        mostrar_puntos(texto_cientifico)

test_correcto()
test_errores()