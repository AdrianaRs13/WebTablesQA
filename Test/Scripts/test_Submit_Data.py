import sys
import time

sys.path.append(sys.path[0] + "/...")
# import os
# Uncomment if the above example gives you a relative path error
# sys.path.append(os.getcwd())

import unittest
from time import sleep
from Search.Src.TestBase.WebDriverSetup import WebDriverSetup
from Search.Src.PageObject.Pages.WebTablesPage import WebTablesPage
from Search.Src.Utils.Utils import Utils
from Search.Src.PageObject.Locators import *

class Submit_Data(WebDriverSetup):
