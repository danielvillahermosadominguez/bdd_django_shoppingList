@fixture.prepare.application_layer
Feature: Manage shopping List - app layer

@Application
Scenario Outline: add items
        Given a shopping list application
        When add "<Items>" in the shopping list application
        Then the scenario is <Result>

Examples:   Adding items
            |        Items        |       Result            |
            | Bread               |  Bread:1                |
            | Bread,Bread,Bread   |  Bread:3                |
            | Bread, Milk, Bread  |  Bread:2,Milk:1         |
            | Bread, Milk, Milk   |  Bread:1,Milk:2         |
            | Bread, Milk, Onion  |  Bread:1,Milk:1,Onion:1 |

@Application
Scenario Outline: delete items
        Given a shopping list application with <Items>
        When remove "<Input>" in the shopping list application
        Then the scenario is <Result>

Examples:   items to delete
            |        Items        | Input          |      Result            |
            | Bread               |  Bread         |                        |
            | Bread,Bread,Bread   |  Bread,Bread   |        Bread:1         |
            | Bread, Milk, Bread  |  Bread         | Bread:1,Milk:1         |
            | Bread, Milk, Milk   |  Bread         |         Milk:2         |

@Application
Scenario Outline: change items
        Given a shopping list application with <Items>
        When change "<Input>" in the shopping list application
        Then the scenario is <Result>

Examples:   items to delete
            |        Items        | Input          |      Result            |
            | Bread               |  Bread:Milk    |        Milk:1          |
            | Bread,Bread,Bread   |  Bread:Onion   |        Onion:3         |
            | Bread, Milk, Bread  |  Bread:Milk    |         Milk:3         |
            | Bread, Milk, Milk   |  Bread:Onion   |  Onion:1,Milk:2        |