Feature: Library
    As a user
    I want to browse the library

Scenario: Registering a new user
    Given I am on the user registration page
    When I enter the required information
    And I submit the registration
    Then I should see that the user has been successfully added
