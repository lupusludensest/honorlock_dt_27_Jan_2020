# Created by rapid at 1/29/2020
Feature: System redirects to forget password pop-up

  Scenario: User clicks "Forgot Password" button
    Given Loginpage
    Then Clicks "Forgot Password" button
    Then Verify "Enter your Email and we'll send you a link to change your password." sign is here
    Then Input email "RestoreAccess@gmail.com" for restoring access
    Then Click on Request Password button
    Then Verify "Password confirmation sent to RestoreAccess@gmail.com. Make sure you check your spam box." sign is here