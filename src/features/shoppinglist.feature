@fixture.prepare.environment
Feature: Manage the shopping list

    # User story:Healthcheck
    @Acceptation
    Scenario: The shopping list is alive
        Given a shopping list
        When ask if the shopping list is alive
        Then the shopping list is alive
    # User story: Add items
    @Acceptation
    Scenario: The user can add items to his/her empty shopping List
        Given a shopping list
        When add "Bread" in the shopping list
        Then the shopping list has
            | Item  | Quantity |
            | Bread | 1        |

    # User story: Add items
    @Acceptation
    Scenario: The user can add items to his/her empty shopping List
        Given a shopping list
        When add "Bread" in the shopping list
        And  add "Bread" in the shopping list
        And  add "Milk" in the shopping list
        Then the shopping list has
            | Item  | Quantity |
            | Bread | 2        |
            | Milk  | 1        |
    @Acceptation
    Scenario: The user can add items to his/her filled shopping List
        Given a shopping list with the following items
            | Item  | Quantity |
            | Bread | 2        |
            | Milk  | 1        |
        When add "Bread" in the shopping list
        Then the shopping list has
            | Item  | Quantity |
            | Bread | 3        |
            | Milk  | 1        |
    @Acceptation
    Scenario: The user cannot add items to his/her shopping List if the format is not correct: Emtpy item
        Given a shopping list with the following items
            | Item  | Quantity |
            | Bread | 2        |
            | Milk  | 1        |
        When add " " in the shopping list
        Then the shopping list has
            | Item  | Quantity |
            | Bread | 2        |
            | Milk  | 1        |
        And you cannot add a item with a no correct format
    @Acceptation
    Scenario: The user cannot add items to his/her shopping List if the format is not correct: Emtpy item
        Given a shopping list with the following items
            | Item  | Quantity |
            | Bread | 2        |
            | Milk  | 1        |
        When add "" in the shopping list
        Then the shopping list has
            | Item  | Quantity |
            | Bread | 2        |
            | Milk  | 1        |
        And you cannot add a item with a no correct format
    @Acceptation
    Scenario: The user cannot add items to his/her shopping List if the format is not correct: number without characters
        Given a shopping list with the following items
            | Item  | Quantity |
            | Bread | 2        |
            | Milk  | 1        |
        When add "88" in the shopping list
        Then the shopping list has
            | Item  | Quantity |
            | Bread | 2        |
            | Milk  | 1        |
        And you cannot add a item with a no correct format
    @Acceptation
    Scenario: The user cannot add items to his/her shopping List if the format is not correct: less than 3 chars
        Given a shopping list with the following items
            | Item  | Quantity |
            | Bread | 2        |
            | Milk  | 1        |
        When add "b" in the shopping list
        Then the shopping list has
            | Item  | Quantity |
            | Bread | 2        |
            | Milk  | 1        |
        And you cannot add a item with a no correct format
    @Acceptation
    Scenario: The user cannot add items to his/her shopping List if the format is not correct: less than 3 chars
        Given a shopping list with the following items
            | Item  | Quantity |
            | Bread | 2        |
            | Milk  | 1        |
        When add "br" in the shopping list
        Then the shopping list has
            | Item  | Quantity |
            | Bread | 2        |
            | Milk  | 1        |
        And you cannot add a item with a no correct format

    # User story: Remove items
    @Acceptation
    Scenario: The user can remove items to his/her shopping List
        Given a shopping list with the following items
            | Item  | Quantity |
            | Bread | 2        |
            | Milk  | 1        |
        When remove 1 item of "Milk"
        And remove 1 item of "Bread"
        Then the shopping list has
            | Item  | Quantity |
            | Bread | 1        |
    @Acceptation
    Scenario: The user cannot remove more items from the shopping list than there are in
        Given a shopping list with the following items
            | Item  | Quantity |
            | Bread | 2        |
        When remove 3 item of "Milk"
        Then the shopping list has
            | Item  | Quantity |
            | Bread | 2        |
        And it is impossible to remove this quantity in this items

    @Acceptation
    Scenario: The user can remove all the items
        Given a shopping list with the following items
            | Item  | Quantity |
            | Bread | 2        |
            | Milk  | 1        |
        When remove all items
        Then the shopping list is empty
    @Acceptation
    Scenario: The user can Update the name of an item
        Given a shopping list with the following items
            | Item  | Quantity |
            | Bread | 2        |
            | Milk  | 1        |
        When change the item "Milk" with "Onion"
        Then the shopping list has
            | Item  | Quantity |
            | Bread | 2        |
            | Onion | 1        |
    @Skip
    @Acceptation
    Scenario: The user cannot Update the name of an item if the item doesn't exist
        Given a shopping list with the following items
            | Item  | Quantity |
            | Bread | 2        |
            | Milk  | 1        |
        When change the item "Onion" with "Milk"
        Then the shopping list has
            | Item  | Quantity |
            | Bread | 2        |
            | Milk  | 1        |
        And the name doesn't exist
    @Acceptation
    Scenario: The user can reset the list of items
        Given a shopping list with the following items
            | Item  | Quantity |
            | Bread | 2        |
            | Milk  | 1        |
        When reset the quantity of all items
        Then the shopping list has
            | Item  | Quantity |
            | Bread | 1        |
            | Milk  | 1        |

