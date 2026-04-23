Feature: Login
    Scenario:create a login account
        Given a new user
        When new user provides user name and password and submits
        Then account should be created

    Scenario: when Existing user logs in
        Given an existing user
        When user logs in
        Then user must log in successfully