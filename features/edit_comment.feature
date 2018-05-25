
  Feature: Edit Comment
    In order to edit or delete a comment of myself
    As a user
    I want to edit or delete the comment I wrote

    Background: There is a registered user
      Given Exists a user "user" with password "password"
      And Exists a comment
          | author  | title   |  text         | commented_meme  |
          | user    | coolbro | haha so funny | Ugandan Knuckles|

      Scenario: Delete a comment
        Given I login as user "user" with password "password"
        When I go to my profile
        And I'm viewing the details page for comments by "user"
          | author  | title   |  text         | commented_meme  |
          | user    | coolbro | haha so funny | Ugandan Knuckles|
        And there are 1 comment
        And I delete the comment
        Then There are 0 comments


    Scenario: Delete a comment from others
       Given I login as user "user" with password "password"
        When I go to my profile
        And I'm viewing the details page for comments by "user"
          | author  | title   |  text         | commented_meme  |
          | user    | coolbro | haha so funny | Ugandan Knuckles|
          | OP      | OPtitle |I'm the OP and I'm OP   | user   |
        And there are 2 comment
        And I delete the comment
          | author  | title   |  text         | commented_meme  |
          | OP      | OPtitle |I'm the OP and I'm OP   | user   |
        Then there are 1 comment