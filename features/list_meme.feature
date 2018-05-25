
  Feature: List Meme
    In order to seek for a specific meme or topic
    As a user
    I want to search for a tag or a title and find the meme

    Background: There are 5 memes registered by same user
      Given Exists a user "user" with password "password"
      And Exists meme registered by "user"
        |name   |date   |
        |first  |2018-01|
        |second |2018-02|
        |third  |2018-03|
        |fourth |2018-04|
        |fifth  |2018-05|

    Scenario: List the last five
      When I list memes
      Then I'm viewing a list containing
        |name     |
        |first    |
        |second   |
        |third    |
        |fourth   |
        |fifth    |
      And the list contains 5 memes

    Scenario: List the last five
      Given Exists a meme registered by "user"
        |name   |date     |
        |sixth  |2018-06  |
      When I list memes
      Then I'm viewing a list containing
        |name     |
        |sixth    |
        |fifth    |
        |fourth   |
        |third    |
        |second   |