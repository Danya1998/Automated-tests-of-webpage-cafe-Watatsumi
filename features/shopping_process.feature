Feature: Check the ability of buying some food for register user on website Watatsumi

  Scenario: User authorization on website
    Given website "https://watatsumi.com.ua/"
    Then I go to user authorization page
    And Login with username "test10@gmail.com" and password "daniel1988170"
    And Verify that I registered on website with username "test10"

  Scenario: Login on website and add pizza to cart
    Given website "https://watatsumi.com.ua/"
    Then I go to user authorization page
    And Login with username "test10@gmail.com" and password "daniel1988170"
    And Verify that I registered on website with username "test10"
    And Go to pizza page, add "Пицца Украинская" to shopping cart and check successful message

  Scenario: Check that roll is added to shopping cart
    Given website "https://watatsumi.com.ua/"
    Then I go to user authorization page
    And Login with username "test10@gmail.com" and password "daniel1988170"
    And Verify that I registered on website with username "test10"
    And Go to pizza page, add "Пицца Украинская" to shopping cart and check successful message
    And Go to rolls page, add "Эверест" to shopping cart and check successful message

  Scenario: Check that pizza is in shopping cart
    Given website "https://watatsumi.com.ua/"
    Then I go to user authorization page
    And Login with username "test10@gmail.com" and password "daniel1988170"
    And Verify that I registered on website with username "test10"
    And Go to pizza page, add "Пицца Украинская" to shopping cart and check successful message
    And Go to rolls page, add "Эверест" to shopping cart and check successful message
    And Go to checkout page and check that first product "Украинская - 30 см " is added to order

  Scenario: Check that sushi is in shopping cart
    Given website "https://watatsumi.com.ua/"
    Then I go to user authorization page
    And Login with username "test10@gmail.com" and password "daniel1988170"
    And Verify that I registered on website with username "test10"
    And Go to pizza page, add "Пицца Украинская" to shopping cart and check successful message
    And Go to rolls page, add "Эверест" to shopping cart and check successful message
    And Go to checkout page and check that first product "Украинская - 30 см " is added to order
    And Go to checkout page and check that second product "Эверест " is added to order

  Scenario: Log out from account
    Given website "https://watatsumi.com.ua/"
    Then I go to user authorization page
    And Login with username "test10@gmail.com" and password "daniel1988170"
    And Verify that I registered on website with username "test10"
    And Go to pizza page, add "Пицца Украинская" to shopping cart and check successful message
    And Go to rolls page, add "Эверест" to shopping cart and check successful message
    And Go to checkout page and check that first product "Украинская - 30 см " is added to order
    And Go to checkout page and check that second product "Эверест " is added to order
    And Log out from account


