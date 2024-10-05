Feature: Intu Login Feature
    Scenario: Successful intu Login
        Given the user is in the intu login page
        When the user logs int with valid intu credentials
        Then the user should be redirected to the dashboard
