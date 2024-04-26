# Exceções e Erros em Funções

### Como "testar" erros e tratar exceções:

try:
    o que eu quero tentar fazer
except:
    o que vou fazer caso dê erro


### Como "printar" um erro em uma function

raise Exception('O erro foi esse')

ou então avisando qual o tipo de erro que ele teve

raise TypeError('O erro foi esse')
raise ValueError('O erro foi esse')
raise ZeroDivisionError('O erro foi esse')

### Tratamento Completo:

try:
    tente fazer isso
except ErroEspecífico:
    deu esse erro aqui que era esperado 
else:
    caso não dê o erro esperado, rode isso.
finally:
    independente do que acontecer, faça isso.