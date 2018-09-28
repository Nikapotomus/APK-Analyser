from src.FileHandler import FileHandler
from config.Config import APKAnalyserConfig

import os

class Main:

    FH = FileHandler()
    AAConfig = APKAnalyserConfig()

    def __init__(self):
        print("[-] Setting everything up here etc..")

        self.Setup()

    def Setup(self):
        print("[-] Main class here doing stuff...")
        self.FH.UnzipAPK()


        if self.FH.FindFile("test.txt", self.AAConfig.OutputDir):
            print "Found test.txt!"


        libsDir = self.FH.FindDir("libs", self.AAConfig.OutputDir)
        if libsDir:
            print "Found libs directory!"
            for lib in os.listdir(libsDir):
                print lib
