from src.calculator import Calculator


class Test_Calculator:

    # TODOS OS TESTES DEPENDEM DA MÉTRICA QUE VOCÊ UTILIZARÁ NO SEU PROJETO

    def test_add(self):
        result = Calculator.add(2, 3)
        assert result == 5
    
    def test_add2(self):
        result = Calculator.add(2, -3)
        assert result == -1

    def test_subtracao(self):
        result = Calculator.subtracao(2, -3)
        assert result == 5

    def test_multiplicacao(self):
        result = Calculator.multi(2, 3)
        assert result == 6

    def test_divisao(self):
        result = Calculator.divisao(9, 3)
        assert result == 3
    
     # E SE FOR DIVISÃO POR ZERO?????????
    def test_divisao_por_zero(self):
        result = Calculator.divisao(9, 0)
        assert result == 0