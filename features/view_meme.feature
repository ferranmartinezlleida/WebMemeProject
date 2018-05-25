
  Feature: View Meme
    In order to read comments and vote a meme
    As a user
    I want to view the meme details including comments tags and rating

    Background: There is one meme with 2 comments and another without
      Given Exists a user "user1" with password "password"
      And Exists a user "user2" with password "password"
      And Exists meme registered by "user1"
          | title             | tag       |
          | Ugandan Knuckles  | deadmeme  |
          | Cat Meme          | cutememe  |
      And Exists comment at meme "Ugandan Knuckles" by "user1"
          | title | text                    |
          | OP    | I'm the OP and I'm OP   |
      And Exists comment at meme "Cat Meme" by "user2"
          | title        | text             |
          | Love Cats    | Kawaii Desune :3 |
      And Exists vot at meme "Ugandan Knuckles" by "user1"
          | value | author  | voted meme      |
          | 1     | user1   | Ugandan Knuckles|
      And Exists vot at meme "Ugandan Knuckles" by "user2"
          | value | author  | voted meme      |
          | 1     | user2   | Ugandan Knuckles|

    Scenario: View details for meme with two vots and a comment
      Given I login as user "user1" with password "password"
      When I view the details for meme "Ungandan Knuckles"
      Then I'm viewing meme details including
          | title             | tag       |
          | Ugandan Knuckles  | deadmeme  |
      And I'm viewing a meme vot list containing
          | value           | author        | voted meme                |
          | 1               | user1         | Ugandan Knuckles          |
          | 1               | user2         | Ugandan Knuckles          |
      And The list contains 2 reviews
      And I'm viewing a meme comments list containing
          | title | text                    | author|
          | OP    | I'm the OP and I'm OP   | user1 |
      And The list contains 1 comments

    Scenario: View details for not owned meme with 1 comment but no vots
      Given I login as user "user2" with password "password"
      When I view the details for meme "Cat Meme"
      Then I'm viewing meme details including
          | title             | tag       |
          | Cat Meme          | cutememe  |
      And There is no "edit" link available
      And I'm viewing a meme vots list containing
          | value           | author        | voted meme                |
      And The list contains 0 vots
      And I'm viewing a meme comments list containing
          | title        | text             |
          | Love Cats    | Kawaii Desune :3 |
      And The list contains 1 comments

    Scenario: View details for restaurant with 1 comment but no vots when not logged in
      Given I'm not logged in
      When I view the details for restaurant "Ugandan Knuckles"
      Then I'm viewing meme details including
          | title             | tag       |
          | Ugandan Knuckles  | deadmeme  |
      And There is no "edit" link available
      And I'm viewing a restaurant vots list containing
          | value           | author        | voted meme                |
      And The list contains 0 vots
      And I'm viewing a meme commments list containing
          | title | text                    | author|
          | OP    | I'm the OP and I'm OP   | user1 |
      And The list contains 1 comments