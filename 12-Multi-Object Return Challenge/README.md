### Aplicação

- Data Science e Inteligência Artificial usa MUITO isso.

    1. Quando criamos um modelo de previsão, precisamos treinar esse modelo e testar para ver se ele sendo um bom modelo ou não.
    2. Temos então que pegar os nossos dados e dividir em 2 pedaços, uma lista de treino e uma lista de teste.
    3. Vamos então pensar no exemplo de um modelo que tenta identificar qual o valor justo de um imóvel de acordo com o tamanho do imóvel. Temos então 2 listas:
        - Lista 1: Preços Reais dos Imóveis
        - Lista 2: Tamanho do imóvel.
    4. Vamos criar então uma função que recebe 2 listas como entrada e que divide cada uma dessas listas em 2, um pedaço de treino e um pedaço de teste. O percentual que a lista vai ser dividida é definida por um fator (que também vai ser um parâmetro da função)