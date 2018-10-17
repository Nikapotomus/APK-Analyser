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
            print ("[+] Application has a libs folder for storing native libraries!")

            # Array for holding full path references for each lib in artefact
            artefactLibs = []

            for lib in os.listdir(libsDir):
                # print("[+] {} :: {}".format(lib, os.path.join(libsDir, lib)))
                artefactLibs.append(os.path.join(libsDir, lib))

            if artefactLibs:
                print("[+] Found {} native libraries, analysing compiler flags..".format(len(artefactLibs)))

                for al in artefactLibs:
                    print("\t[-] {}".format(al))
            else:
                print("[!] No native libraries used by artefact!")
