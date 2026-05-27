Feature: Login Feature

@XSP-69 @released4run @daily1
Scenario: XSP-69 Valid login test
  Given user is on login page
  When user enters valid username and password
  Then user should see dashboard