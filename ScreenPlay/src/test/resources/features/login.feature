Feature: login to automation practice page
  As a user
  I need to log in to the automation practice page
  to view my account

  Scenario Outline: Login Succesful
    Given the user is on the automation practices page
    When  he logs in with his "<username>" and "<password>"
    Then  He will be able to view the message Welcome to your account.
    Examples:
      | username                         | password    |
      | automation.practice.dz@gmail.com | AUTOMATION1 |