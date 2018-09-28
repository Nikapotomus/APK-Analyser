from src.FileHandler import FileHandler
from config.Config import APKAnalyserConfig

class Main:

    FH = FileHandler()
    AAConfig = APKAnalyserConfig()

    def __init__(self):
        print("[-] Setting everything up here etc..")

        self.Setup()

    def Setup(self):
        print("[-] Main class here doing stuff...")
        self.FH.UnzipAPK()

        self.FH.FindFile("test.txt", self.AAConfig.OutputDir)
        self.FH.FindDir("niktest", self.AAConfig.OutputDir)
