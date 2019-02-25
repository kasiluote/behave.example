Feature: Step Setup Table

   Scenario: Setup Table
     Given a set of specific users
        | name      | department  |
        | Barry     | Beer Cans   |
        | Pudey     | Silly Walks |
        | Two-Lumps | Silly Walks |

    When we count the number of people in each department
    Then we will find 2 people in "Silly Walks"
     But we will find 1 person in "Beer Cans"