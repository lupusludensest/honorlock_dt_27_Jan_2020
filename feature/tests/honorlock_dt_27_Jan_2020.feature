# Created by rapid at 1/27/2020
Feature: User enter wrong login and password and system rejects

  Scenario: User enter wrong login and password and system rejects
    Given Loginpage
    Then Wrong login "WrongPassword1234!@gmail.com"
    Then Wrong password "WrongPassword1234!"
    Then Click on login button
    Then Verify "Invalid username or password" sign is here
