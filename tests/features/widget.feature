Feature: Verify widgets
    As a user
    I want to use the different widgets on the site

    Scenario: Displaying a tooltip
        Given I am on the tooltip page  
        When I hover my mouse over an element
        Then a message appears indicating that my mouse is over the element

    Scenario: Selecting options
        Given I am on the select page
        When I select options from the different dropdowns
        Then the options should be selected