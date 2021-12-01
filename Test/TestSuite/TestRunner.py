import sys
import os

sys.path.append(sys.path[0] + "/...")
# Uncomment if the above example gives you a relative path error
sys.path.append(os.getcwd())

from unittest import TestLoader, TestSuite, TextTestRunner
from Search.Test.Scripts.test_Home_Page import Google_HomePage
from Search.Test.Scripts.test_Google_Search import Google_Search
from Search.Test.Scripts.test_Change_Cierra import Change_Cierra
from Search.Test.Scripts.test_Submit_Data import Submit_Data

import testtools as testtools

if __name__ == "__main__":
    test_loader = TestLoader()
    # Test Suite is used since there are multiple test cases
    test_suite = TestSuite((
        #test_loader.loadTestsFromTestCase(Google_HomePage),
        #test_loader.loadTestsFromTestCase(Google_Search),
        test_loader.loadTestsFromTestCase(Change_Cierra),
        test_loader.loadTestsFromTestCase(Submit_Data),
    ))

    test_runner = TextTestRunner(verbosity=2)
    test_runner.run(test_suite)

    # Refer https://testtools.readthedocs.io/en/latest/api.html for more information
    parallel_suite = testtools.ConcurrentStreamTestSuite(lambda: ((case, None) for case in test_suite))
    parallel_suite.run(testtools.StreamResult())
        # self.driver.set_page_load_timeout(30)
