## 1. Function para Análise de Indicadores

A maioria das empresas tem suas próprias regras para cálculos de indicadores.

- Algumas empresas definem que um cliente é considerado um cliente inadimplente quando ele está devendo acima de X reais e por mais de X dias.
- Algumas empresas definem que um vendedor bateu a meta quando ele vendeu acima de X reais (outras ainda analisam não só as vendas desse vendedor, mas também da loja ou da unidade de negócios que ele faz parte, ou ainda uma avaliação qualitativa)
- Algumas empresas definem que um produto está em "falta" no estoque quando ele está abaixo de um nível mínimo quando um cliente insere um novo pedido daquele produto
- E assim vai para dezenas de indicadores.

O ponto importante é, cada empresa tem alguma adaptação do cálculo de indicadores. E normalmente se formos analisar esses indicadores é interessante ter funções que façam todo o trabalho de análise deles. Por isso, vamos construir 2 exemplos aqui:


### Item 1: Crie uma função que calcula o percentual de Stockout de uma empresa

- O % de stockout é dado por (Vendas Perdidas por Estoque) / (Vendas Concluídas + Vendas Perdidas por Estoque) -> essas vendas são dadas em valor total (dinheiro) e não em quantidade de vendas
- Seu programa recebe um dicionário com todas as vendas da empresa, o status dela (se foi Concluída ou Cancelada) e, caso tenha sido Cancelada, o motivo de Cancelamento. O formato é o seguinte:

vendas = {
    'VE0001': (15000, 'Concluído', ''),
    'VE0002': (13300, 'Cancelado', 'Cancelado pelo Cliente'),
    'VE0003': (12000, 'Concluído', ''),
    ...
}

- Para reforçar: As vendas Canceladas por qualquer outro motivo que não seja a Falta de Estoque não devem ser consideradas para a conta do Stockout.

### Item 2: Crie uma função para descobrir os clientes inadimplentes de uma empresa

- O objetivo é identificar quem são os clientes inadimplentes e enviar essa lista de clientes para o setor de cobrança poder fazer a cobrança dos clientes.
- Sua função deve então receber uma lista de clientes, analisar quais clientes estão inadimplentes, e retornar uma lista com os clientes inadimplentes (apenas o CPF deles já é suficiente)
- A inadimplência nessa empresa é calculada da seguinte forma:
    1. Se o cliente tiver devendo mais de 1.000 reais por mais de 20 dias, ele é considerado inadimplente.
    2. Isso significa que caso ou cliente esteja devendo 2.000 reais a 10 dias, ele não é inadimplente, pois não se passaram 20 dias ainda. Da mesma forma, se ele estiver devendo 500 reais por 40 dias, ele também não é inadimplente, dado que ele deve menos de 1.000 reais.
    3. As informações vêm no formato (cpf, valor_devido, qtde de dias)