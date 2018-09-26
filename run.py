import os.path

from src.Main import Main
from config.Config import APKAnalyserConfig

AAConfig = APKAnalyserConfig
print AAConfig.banner

AAConfig.RootDir = os.path.dirname(os.path.abspath(__file__))
AAConfig.OutputDir = os.path.join(AAConfig.RootDir, 'output')

Main = Main()
