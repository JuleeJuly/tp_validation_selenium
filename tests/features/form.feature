Feature: Filling out a form  
    As a user  
    I want to be able to complete a form  

    Scenario: Entering data into the form  
        Given I am on the form page
        When I enter data into the required fields
        Then I should be able to submit the form