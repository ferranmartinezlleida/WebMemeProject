
  Feature: Comment Comment
    In order to express my opinion to another comment of a meme
    As a user
    I want to reply that comment with a comment of my own

    Background: There is a registered user
      Given Exists a user "user" with password "password"
      And Exists a user "user2" with password "password"

      Scenario: Comment a comment
        Given I login as user "user" with password "password"
        When I'm viewing the details page for meme
          | title             | tag       |
          | Ugandan Knuckles  | deadmeme  |
        And I comment the comment
          | title | text                    | author|
          | OP    | I'm the OP and I'm OP   | user2 |
        Then I'm viewing the details page for meme
          | author  | title   |  text         | commented_meme  |
          | user    | coolbro | haha so funny | Ugandan Knuckles|
          | OP      | OPtitle |I'm the OP and I'm OP   | user2  |

        And there are 2 comments


     Scenario: Try to comment a comment but not logged in
       Given I'm not logged in
       When I'm viewing the details page for meme
          | title             | tag       |
          | Ugandan Knuckles  | deadmeme  |
       And I comment a comment
          | author  | title   |  text         | commented_meme  |
          | user    | coolbro | haha so funny | Ugandan Knuckles|
       Then I'm redirected to the login form
       And There are 1 comments