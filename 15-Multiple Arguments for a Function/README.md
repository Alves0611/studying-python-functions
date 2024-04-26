# Quantidade Indefinidas de Argumentos

### Utilidade:

Quando você quer permitir uma quantidade indefinida de argumentos, usa o * para isso.

### Estrutura:

*args para positional arguments -> argumentos vêm em formato de tupla

def minha_funcao(*args):
    ...


**kwargs para keyword arguments -> argumentos vêm em formato de dicionário

def minha_funcao(**kwargs):
    ...