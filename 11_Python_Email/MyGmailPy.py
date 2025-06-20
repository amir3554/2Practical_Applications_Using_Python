import ezgmail
import os
from pathlib import Path


os.chdir(Path.home() / Path("Desktop", "Python_2024_2025", "2Practical_Applications_Using_Python", "11_Python_Email"))
ezgmail.init(credentialsFile='credentials.json')
