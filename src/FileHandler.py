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
            print("[+] Found target artefact, unzipping...")
            # print(self.AAConfig.RootDir)
            # print(self.AAConfig.OutputDir)

            zipRef = zipfile.ZipFile(targetAPK, 'r')
            zipRef.extractall(self.AAConfig.OutputDir)
            zipRef.close()

    def FindFile(self, name, path):
        for root, dirs, files in os.walk(path):
            if name in files:
                # print "Found File :: {}".format(os.path.join(root, name))
                return os.path.join(root, name)

    def FindDir(self, name, path):
        for root, dirs, files in os.walk(path):
            if name in dirs:
                # print "Found Directory :: {}".format(os.path.join(root, name))
                return os.path.join(root, name)
