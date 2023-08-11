Feature: Subtrair dois números
  Scenario: Realizar uma subtração simples
    Given eu tenho dois números inteiros: 5 e 7
    When eu subtraio os dois números inteiros
    Then o resultado deve ser -2
