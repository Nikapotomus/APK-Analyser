import os
import zipfile

from config.Config import APKAnalyserConfig

class FileHandler:
    AAConfig = APKAnalyserConfig

    def __init__(self):
        pass

    def UnzipAPK(self):

        targetAPK = "/home/nikola/Documents/python_projects/APK-Analyser/nik.zip"
        if os.path.isfile(targetAPK):
            print("FOUND THE FILE!!")

            print(self.AAConfig.RootDir)
            print(self.AAConfig.OutputDir)

            zipRef = zipfile.ZipFile(targetAPK, 'r')
            zipRef.extractall(self.AAConfig.OutputDir)
            zipRef.close()
