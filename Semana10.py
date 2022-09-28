import abc

class MediaLoader(abc.ABC):
    """
    Clase abstracta para crear un cargador de archvios de media genericos
    """
    @abc.abstractclassmethod
    def play(self) -> None:
        ...
    @property
    @abc.abstractclassmethod
    def ext(self) -> str:
        ...

class Wav(MediaLoader):
    pass
class Ogg(MediaLoader):
    ext = ".Ogg"
    def play(self,formato):
        #print("Playing ogg")
        return "Playing {}".format(formato)

prueba = Ogg()
print(prueba.play("Ogg"))

#Los parametros del constructor no son atributos de la clase, se vuelven atributos al guardarlo como self.