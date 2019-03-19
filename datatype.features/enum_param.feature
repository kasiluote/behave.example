Feature: User-Defined Enum Type (Name-to-Value Mapping)

Scenario Outline:
    When Romeo asks Julia: "<Question>"
    Then the answer is "<Answer>"

    Examples: Tests
       | Question          | Answer  |
       | Do you love me?   | yes     |
       | Do you hate me?   | no      |
       | Do you kiss me?   | jubilee |
 
