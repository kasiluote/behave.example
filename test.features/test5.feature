Feature: Step Data

  Scenario: Some scenario
    Given a sample text loaded into the forbulator:
    """
    Lorem ipsum dolor sit amet, consectetur xxxx
    """

    When we activate the forbulator
    Then we will find it similar to English
