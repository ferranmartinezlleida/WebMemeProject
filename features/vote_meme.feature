
  Feature: Vote Meme
    In order to express my opinion about a meme
    As a user
    I want to vote it and see the current score of it


    Background: There is a registered user and restaurant
      Given Exists a user "user" with password "password"
      And Exists meme created "by "user"
          | title             | tag       |
          | Ugandan Knuckles  | deadmeme  |

    Scenario: Register vot
      Given I login as user "user" with password "password"
      When I register a vot at meme "Ugandan Knuckles"
          | value | author  | voted meme      |
          | 1     | user    | Ugandan Knuckles|
      Then I'm viewing the details page for meme by "user"
        | name            |
        | The Tavern      |
      And I'm viewing a meme vots list containing
        | rating          | comment       | user          |
        | 4               | Quite good    | user          |
      And The list contains 1 vot
      And There are 1 vot

    Scenario: Try to register vot but not logged in
      Given I'm not logged in
      When I register a vot at meme "Ugandan Knuckles"
          | value | author  | voted meme      |
          | 1     | user    | Ugandan Knuckles|
      Then I'm redirected to the login form
      And There are 0 vots