# Created by rapid at 1/29/2020
Feature: System redirects to forget password pop-up

  Scenario: User clicks "Forgot Password" button
    Given Loginpage
    Then Clicks "Forgot Password" button
    Then Verify "Enter your Email and we'll send you a link to change your password." sign is here