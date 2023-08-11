from behave import given, when, then

@given('eu tenho dois números inteiros: {num1:d} e {num2:d}')
def step_impl(context, num1, num2):
    context.num1 = num1
    context.num2 = num2

@when('eu somo os dois números inteiros')
def step_impl(context):
    context.resultado = context.num1 + context.num2

@then('o resultado deve ser {resultado:d}')
def step_impl(context, resultado):
    assert context.resultado == resultado, f"Resultado incorreto. Esperado: {resultado}. Obtido: {context.resultado}"

@given('eu tenho dois números inteiros: {num1:d} e {num2:d}')
def step_impl(context, num1, num2):
    context.num1 = num1
    context.num2 = num2

@when('eu subtraio os dois números inteiros')
def step_impl(context):
    context.resultado = context.num1 - context.num2

@then('o resultado deve ser {resultado:d}')
def step_impl(context, resultado):
    assert context.resultado == resultado, f"Resultado incorreto. Esperado: {resultado}. Obtido: {context.resultado}"