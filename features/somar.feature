Feature: Somar dois números
  Scenario: Realizar uma soma simples 01
    Given eu tenho dois números inteiros: 5 e 7
    When eu somo os dois números inteiros
    Then o resultado deve ser 12
