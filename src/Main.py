from src.FileHandler import FileHandler

class Main:

    FH = FileHandler()

    def __init__(self):
        print("[-] Setting everything up here etc..")



        self.Setup()

    def Setup(self):
        print("[-] Main class here doing stuff...")
        self.FH.Description()
