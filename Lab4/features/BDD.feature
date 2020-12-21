Feature: Test Bridge

  Scenario: Using 1st API
    Given 1st year student using API 1
    When we try to get marks of student
    Then we will get their marks in range 5...20

  Scenario: Using 2nd API
    Given 1st year student using API 2
    When we try to get marks of student
    Then we will get their marks in range 0...5