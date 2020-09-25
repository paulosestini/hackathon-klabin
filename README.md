# Cresça sua Ideia
![Cresça sua Ideia](https://i.ibb.co/4PLHzVP/cresca-ideia.png)

## O que é?
A **Cresça sua Ideia** é uma plataforma criada para o hackathon da Klabin/Empathy, cuja proposta era colaborar com melhorias para o robô **Luna**, uma coruja interativa por meio da qual os funcionários da empresa podem enviar ideias e sugestões para a Klabin.

## Floresta de ideias
A Plataforma visa aumentar a interatividade dos funcionários com as ideias geradas por estes. Cada funcionário pode plantar uma ideia, em formato de árvore, e outros funcionários podem regar esta ideia, para que ela floresça.

![Ideias crescendo](https://i.ibb.co/mbJBS9w/ideia-arvore.png)

## Mapa de ideias
O mapa de ideias é um mapa interativo que permite visualizar de onde as ideias estão vindo, nele é possível visualizar as unidades da Klabin e a quantidade de ideias vindas de cada uma.

![Mapa de ideias](https://i.ibb.co/KwMfF63/Screenshot-from-2020-09-25-09-54-14.png)

## NLP e Word Cloud
Quando se trata de ideias e textos, é interessante utilizar *Processamento de Linguagem Natural(NLP)* para analisar o conteúdo das mensagens. A plataforma utiliza a ideia de *Word Cloud*, uma técnica de exploração visual de dados em NLP, que consiste em criar uma nuvem de palavras para visualizar quais mais aparecem nas mensagens, assim, palavras que são usadas com frequência aparecem maiores e com maior destaque.

Há também como personalizar a Word Cloud, e para dar uma melhor caracterização, foi utilizado um formato de coruja em um galho para construir a nuvem, fazendo referência à Luna.

![Word Cloud](https://i.ibb.co/nQcjgsm/Screenshot-from-2020-09-25-10-05-08.png)


# Tecnologias utilizadas
O site foi construído utilizando a linguagem Python, em conjunto com a biblioteca Flask. Para a criação do mapa e da word cloud, foram utilizadas outras bibliotecas.
Principais bibliotecas utilizadas:
* Flask - Framework
* Plotly - Criação do Mapa
* WordCloud - Criação da Word Cloud

Algumas bibliotecas auxiliares utilizadas:
* Matplotlib
* Numpy
* Pandas

## Como executar o site
Com a biblioteca Flask instalada, abra o terminal e rode os seguintes comandos:

No Linux:
```
export FLASK_APP=app.py
flask run
```

No Windows (com terminal padrão):
```
C:\path\to\app>set FLASK_APP=app.py
flask run
```

No Windows (com PowerShell):
```
PS C:\path\to\app> $env:FLASK_APP = "app.py"
flask run
```

## Créditos
Imagem utilizada de máscara para a word cloud: https://www.clipart.email/download/2433738.html

Floresta de fundo do site: https://www.vecteezy.com/vector-art/181748-abstract-forest-landscape




