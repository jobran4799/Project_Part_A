Todoist Website Test Code Check
Description
This project involves performing functional and non-functional testing on the Todoist website. The tests are conducted to ensure the proper functioning and performance of the website under various conditions. The project also includes running the code in multiple browsers and leveraging Selenium Grid to distribute test execution across different nodes.

Testing
Functional Testing
Functional testing involves verifying that the Todoist website's features and functionalities work as expected. This includes testing tasks such as creating new tasks, editing existing tasks, setting reminders, and managing projects and labels.

Non-Functional Testing
Non-functional testing focuses on aspects like performance, usability, security, and compatibility. Performance testing ensures that the website responds quickly and efficiently under different load conditions. Usability testing assesses the user-friendliness of the interface. Security testing checks for vulnerabilities and ensures data privacy. Compatibility testing ensures that the website works correctly across different browsers and devices.

Multi-Browser Testing
The project involves running the test code in multiple browsers to ensure cross-browser compatibility. This ensures that the Todoist website functions correctly regardless of the browser used by the end user.

Selenium Grid
Selenium Grid is used to distribute test execution across multiple nodes, allowing for parallel execution of tests. This improves efficiency and reduces the overall test execution time

infra/ Folder
This folder contains infrastructure-related code.

api_wrapper: Provides a wrapper for api-related operations.
base_page.py: Implements the base page class for other page objects.
browser_wrapper.py: Provides a wrapper for browser-related operations.
logic/ Folder
This folder contains logic related to different pages of the Todoist website.

login_page.py: Defines the page object for the login page.
main_page.py: Defines the page object for the main page.
project_list_page.py: Defines the page object for the project list page.
tests/ Folder
This folder contains test scripts.

login_page_test.py: Contains tests for the login page.
main_page_test.py: Contains tests for the main page.
project_list_page_test.py: Contains tests for the project list page.
test_runner.py: Executes the tests and reports results.

Other Files
README.md: Contains project documentation and instructions.
