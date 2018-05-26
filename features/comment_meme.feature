
  Feature: Comment Meme
    In order to express an opinion through text about a meme
    As a user
    I want to comment a meme


    Background: There is a registered user
      Given Exists a user "user" with password "password"

      Scenario: Comment a meme
        Given I login as user "user" with password "password"
        When I comment meme
          | author  | title   |  text         | commented_meme  |
          | user    | coolbro | haha so funny | Ugandan Knuckles|
        Then I'm viewing the details page for meme by "user"
          | author  | title   |  text         | commented_meme  |
          | user    | coolbro | haha so funny | Ugandan Knuckles|
        And there are 1 comment


     Scenario: Try to comment meme but not logged in
       Given I'm not logged in
       When I comment meme
          | author  | title   |  text         | commented_meme  |
          | user    | coolbro | haha so funny | Ugandan Knuckles|
       Then I'm redirected to the login form
       And There are 0 comments