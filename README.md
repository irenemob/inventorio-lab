# inventorio-lab
## SISTEMA DE INVENTÁRIO DE LABORATÓRIO QUÍMICO ##
# Como funciona ?
> Este projeto é uma solução em python para o processamento dos dados de um laboratório de Engenharia Química. Ele funciona identificando os reagentes disponíveis, ignorando as duplicatas, organiza mostrando-os por lote e grau de pureza e, depois, mostra aqueles que são adequados para experimentos sensíveis, com grau de pureza maior ou igual a 98.0% . 
# Como Executar ?
Para rodar este sistema na sua máquina, basta:

1. Abra o git bash.
2. Clone este repositório executando o comando:
   git clone [LINKDOGITHUB]
3. Entre na pasta do projeto:
   cd inventario-lab
4. Execute o script Python:
    python inventario_lab.py

# Perguntas Teóricas :
1. Seria incorreto pois o dicionário, fundamentalmente, não permite chaves duplicadas. Como o laboratório possui vários lotes de um mesmo reagente, se usássemos o nome como chave, o dicionário guardaria apenas o lote do último reagente lido com esse nome, e apagaria todo o resto, 
2. Antes de usar o list, o zip sozinho apenas gera um objeto iterável na memória. O Python não cruza os dados imediatamente, ele apenas guarda a lógica de pareamento na memória. O list é o comando que obriga o Python a efetivamente executar o que foi processado.
3. O list comprehension agrupa, em uma só linha, a criação da lista, o laço de repetição 'for', o desempacotamento das variáveis e o filtro condicional 'if`. Além de deixar o código mais limpo, ele permite  uma execução mais rápida e necessita de menos poder de processamento. 