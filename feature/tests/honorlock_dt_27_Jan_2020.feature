# Created by rapid at 1/27/2020
Feature: User logins

  Scenario: User enter wrong login and password, system rejects
    Given I am on loginpage
    Then Input wrong email "WrongPassword1234!@gmail.com" into login
    Then Input wrong password "WrongPassword1234!"
    Then Click on login button
    Then Verify "Invalid username or password" sign is here
