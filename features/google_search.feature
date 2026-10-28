Feature: Google Search Functionality

  Scenario: Searching for Python Behave on Google
    Given I open the Google homepage
    When I search for "Python Behave Selenium"
    Then I should see search results related to "Python Behave"