Feature: Check signIn Functionality for the new User
  Scenario: User enters valid credentials
    Given After creating account
    And Clicking on Signin
    When User enters valid email
    And User enters valid password
    Then User lands on Products page

    Scenario Outline:
      Given After creating account
      And Clicking on Signin
      When User enters valid "<email>"
      And User enters valid "<password>"
      Then User lands on Products page
      Examples:
      | email | password |
      | summ@gmail.com | abcd@123  |





