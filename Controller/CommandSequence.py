# -*-coding:UTF-8 -*

from Model.Command import Command as cmd
class CommandSequence:

    def __init__(self, command):
        self.command = command

        self.guessRecognition()



    def guessRecognition(self):
        commandInstance = cmd()
        bestCommand = commandInstance.compareCommands(self.command)
        print(bestCommand)
        takeEveryInformation = commandInstance.getAllInformation(bestCommand)
        self.executeSequence(takeEveryInformation)


    def executeSequence(self,command):

        #ici on créera l'execution du code demandé
        return 0











