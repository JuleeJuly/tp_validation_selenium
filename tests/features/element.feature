Feature: Testing different elements  
    As a user  
    I want to be able to interact with various elements  

    Scenario: Following links sends an API call
        Given I am on the Links Page
        When I try the different links
        Then the API returns the corresponding status code

    Scenario: Interacting with radio buttons  
        Given I am on the radio buttons page  
        When I select different options  
        Then the No radio button should be disabled

    Scenario: Testing dynamic properties
        Given I am on the dynamic properties page
        When the 5-second timer expires
        Then the button s color changes