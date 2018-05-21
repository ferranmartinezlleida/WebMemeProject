
  Feature: Create Meme
    In order to show the world the best memes
    As a user
    I want to create a meme

    Background: There is a registered user
      Given Exists a user "user" with password "password"

      Scenario: Create a meme
        Given I login as user "user" with password "password"
        When I create meme
          | title             |
          | Ugandan Knuckles  |
        Then I'm viewing the details page for meme by "user"
          | title             |
          | Ugandan Knuckles  |
        And there are 1 memes


     Scenario: Try to register meme but not logged in
       Given I'm not logged in
       When I register restaurant
         | title              |
         | Ugandan Knuckles   |
       Then I'm redirected to the login form
       And There are 0 memes