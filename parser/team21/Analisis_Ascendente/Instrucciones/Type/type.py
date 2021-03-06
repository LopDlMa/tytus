from tytus.parser.team21.Analisis_Ascendente.Instrucciones.Expresiones.Expresion import Expresion
from tytus.parser.team21.Analisis_Ascendente.Instrucciones.expresion import Primitivo
from tytus.parser.team21.Analisis_Ascendente.Instrucciones.instruccion import Instruccion
from tytus.parser.team21.Analisis_Ascendente.storageManager.jsonMode import *
import tytus.parser.team21.Analisis_Ascendente.Tabla_simbolos.TablaSimbolos as TS
#TYPE
class CreateType(Instruccion):
    def __init__(self, id, lista,fila,columna):
        self.id = id
        self.lista = lista
        self.fila = fila
        self.columna = columna

    def ejecutar(createType,ts,consola,exceptions):


        if ts.validar_sim(createType.id) == -1:

            datavalidada = []

            for data in createType.lista:
                resultado = Expresion.Resolver(data,ts,consola,exceptions)
                datavalidada.append(resultado)

            nuevo_tipo = TS.Simbolo(TS.TIPO_DATO.CLASEENUMERADA,createType.id,"Enum",datavalidada,None)
            ts.agregar_sim(nuevo_tipo)
            consola.append(f"Se añadio una clase enum llamada  {createType.id}")

        else:

            consola.append(f"Ya existe esta clase enumerada")