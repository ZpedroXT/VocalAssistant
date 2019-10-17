# -*-coding:UTF-8 -*
from Model.Command import Command as cmd
# from Controller.DateInformation import DateInformation
import importlib
class CommandSequence:

    def __init__(self, command):
        # self.command = command
        print("initialisation ok")





    def guessRecognition(self,command):
        commandInstance = cmd()
        bestCommand = commandInstance.compareCommands(command)

        takeEveryInformation = commandInstance.getAllInformation(bestCommand)
        return takeEveryInformation


    def executeSequence(self,command):

        maClasse  = command[7].rstrip()
        maMethode = command[4]

        module = importlib.import_module("Controller."+maClasse)
        print(module)
        classLocation = getattr(module, maClasse)

        instance = classLocation()

        return getattr(instance, maMethode)()

        #ici on créera l'execution du code demandé
        return True











