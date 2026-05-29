@XSP-69 @released4run @daily1
Feature: Login functionality
@XSP-69
Scenario: Valid login
    Given user opens login page
    When user enters valid username and password
    Then user should login successfully

@XSP-80 @released4run @daily1
Feature: Login functionality
@XSP-80
  Scenario: Invalid login
    Given user opens login page
    When user enters invalid username and password
    Then error messag is displaying