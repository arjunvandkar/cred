from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service

@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        serv_obj = Service("C:\chromedriver_win32 (2)\chromedriver")
        driver = webdriver.Chrome(service=serv_obj)
        print("Launching the chrome browser ")
    elif browser=='edge':
        serv_obj = Service("C:\Drivers\edge\msedgedriver.exe")
        driver = webdriver.Edge(service=serv_obj)
        print("Launching the edge browser ")
    return driver


def pytest_addoption(parser):  # This will get the value from cli books
    parser.addoption("--browser", action="store", default="chrome", help="Type in browser name e.g. chrome OR edge")

@pytest.fixture()
def browser(request):   #This will return the browser value to setup method
    return request.config.getoption("--browser")
# it is a hook for Ading Enviroments info to HTML Reports
@pytest.fixture()
def browser(request):   #This will return the browser value to setup method
    return request.config.getoption("--browser")
# it is a hook for Ading Enviroments info to HTML Reports
def pytest_configure(config):
    config._metadata['Project Name ']= 'nop commerce'
    config._metadata['Module Name '] = 'Customers'
    config._metadata['Automation Test Engineer '] = 'Arjun'

#It is hook for delete/modify enviroments info to HTML reports
'''@pytest.mark.optinalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("JAVA_HOME", None)'''
#Added a yield statement in the setup fixture to ensure that the browser is closed after the test has completed.
#Added an action and default argument to the pytest_addoption function to set a default browser value if none is provided.
#Added a help argument to the pytest_addoption function to provide a usage message for the --browser option.

# to run test case parallely
#pytest -v -s -n=2 testCases/test_login.py --browser edge
#########################################################

#what is the hooks in pytest html reports

'''In Pytest, hooks are functions that can be used to extend or modify the behavior of the testing framework. The pytest-html plugin provides several hooks that can be used to customize the HTML report generation process. Here are some examples:

pytest_html_report_title(report) - This hook can be used to customize the title of the HTML report. The report argument contains information about the test session.

pytest_html_results_table_header(cells) - This hook can be used to customize the header row of the results table in the HTML report. The cells argument is a list of cell objects that represent the table cells.

pytest_html_results_table_row(report, cells) - This hook can be used to customize each row of the results table in the HTML report. The report argument contains information about the test item, and the cells argument is a list of cell objects that represent the table cells.

pytest_html_report_each(report) - This hook can be used to customize each individual test report in the HTML report. The report argument contains information about the test item.

Using these hooks, you can customize the HTML report to include additional information, modify the styling of the report, or add custom content. You can find more information about the available hooks and how to use them in the pytest-html plugin documentation.'''