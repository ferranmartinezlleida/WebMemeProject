
  Feature: Delete Meme
    In order to edit something wrong about a meme I posted
    As a user
    I want to delete it

      Background: There are registered users and a meme by one of them
    Given Exists a user "user1" with password "password"
    And Exists a user "user2" with password "password"
    And Exists meme registered by "user1"
      | title             | tag       |
      | Ugandan Knuckles  | deadmeme  |

  Scenario: Delete the meme while logged in
    Given I login as user "user1" with password "password"
    When I delete the meme with name "Ugandan Knuckles"
    Then I'm viewing the details page for restaurant by "user1"
      | name            | city            | country         |
      | The Tavern      | London          | England         |
    And There are 1 restaurants

  Scenario: Try to delete meme but not logged in
    Given I'm not logged in
    When I view the details for meme "Ugandan Knuckles"
    Then There is no "Delete" link available

  Scenario: Try to delete meme but not the owner no delete button
    Given I login as user "user2" with password "password"
    When I view the details for meme "Ugandan Knuckles"
    Then There is no "Delete" link available