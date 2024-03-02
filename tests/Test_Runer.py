# test_runner.py
import json
import unittest
from concurrent.futures import ThreadPoolExecutor
from infra.Brawser_Wrapper import BrowserWrapper
from tests.Log_In_Page_Test import Login_page_test
from tests.Main_Page_Test import Main_page_test
from tests.Projects_List_Page_Test import Project_List_Page_Test

try:
    with open('../Config_Manegre/config.json') as f:
        data = json.load(f)
except FileNotFoundError:
    print("Error: 'config.json' file not found. Make sure the file exists in the correct location.")
    raise  # Raise the error to halt execution if the file is essential for the script to run

list_test_cases_runer = [Login_page_test, Project_List_Page_Test, Main_page_test]
def test_brawser_runer(browser):
    for test_cases in list_test_cases_runer:
        test_cases.browser = browser
        test_suite = unittest.TestLoader().loadTestsFromTestCase(test_cases)
        print(test_suite, browser)
        unittest.TextTestRunner().run(test_suite)


if __name__ == "__main__":
    browser_wrapper = BrowserWrapper()
    parallel = data["parallel"]
    serial = data["serial"]
    get_browser = data["browser"]
    browsers = data["browser_types"]
    if parallel:
        with ThreadPoolExecutor(max_workers=len(browsers)) as executor:
            executor.map(test_brawser_runer, browsers)
    elif serial:
        for browser in browsers:
            test_brawser_runer(browser)
    else:
        test_brawser_runer(get_browser)
