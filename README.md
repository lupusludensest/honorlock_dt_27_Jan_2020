# honorlock_dt_27_Jan_2020
honorlock_dt_27_Jan_2020

Test Case

# Created by rapid at 1/27/2020
Feature: System rejects wrong login and password

  Scenario: User enter wrong login and password and system rejects
    Given Loginpage
    Then Wrong login "WrongPassword1234!@gmail.com"
    Then Wrong password "WrongPassword1234!"
    Then Click on login button
    Then Verify "Invalid username or password" sign is here
	
	Preconditions:
Runnable on: Windows 10
Browser: Chrome
Tools: Java, Selenium Webdriver

Testcase steps:
1.	Go to https://honorlock.instructure.com/login/canvas
2.	Input wrong login "WrongPassword1234!@gmail.com".
3.	Input wrong password "WrongPassword1234!".
4.	Click on login button.
5.	Verify "Invalid username or password" pop-up is here.

Please put your code to GitHub.com and send the project link.

Thank you.

===========================================================================================
If you will install allure(java should be here)-you would be able to see the visual report. 
See steps:
$ pip install allure-behave
$ pip install allure-pytest
$ pip install pytest-allure-adaptor

to launch tests and generate reports folder: 
$ behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/
to extract report into browser: 
$ allure serve test_results/
