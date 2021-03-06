from flask import Flask, render_template, redirect, jsonify
from tree import Tree

app = Flask(__name__)

trees = [
    Tree(0, "Salmoragem", "No mundo atual, o acompanhamento das preferências de consumo nos obriga à análise dos relacionamentos verticais entre as hierarquias. Por outro lado, a valorização de fatores subjetivos é uma das consequências do fluxo de informações. A prática cotidiana prova que a revolução dos costumes pode nos levar a considerar a reestruturação do sistema de participação geral."),
    Tree(1, "PodCast Klabin", "Percebemos, cada vez mais, que a consulta aos diversos militantes estende o alcance e a importância das diversas correntes de pensamento. Por outro lado, o desafiador cenário globalizado acarreta um processo de reformulação e modernização das novas proposições. A prática cotidiana prova que a revolução dos costumes faz parte de um processo de gerenciamento dos níveis de motivação departamental."),
    Tree(2, "Alerta de Risco", "O cuidado em identificar pontos críticos na constante divulgação das informações desafia a capacidade de equalização dos relacionamentos verticais entre as hierarquias. Assim mesmo, o desafiador cenário globalizado pode nos levar a considerar a reestruturação do retorno esperado a longo prazo. No mundo atual, a complexidade dos estudos efetuados cumpre um papel essencial na formulação do orçamento setorial. Caros amigos, o acompanhamento das preferências de consumo representa uma abertura para a melhoria do investimento em reciclagem técnica."),
    Tree(3, "Redução de Reduído", "No mundo atual, o acompanhamento das preferências de consumo nos obriga à análise dos relacionamentos verticais entre as hierarquias. Por outro lado, a valorização de fatores subjetivos é uma das consequências do fluxo de informações. A prática cotidiana prova que a revolução dos costumes pode nos levar a considerar a reestruturação do sistema de participação geral."),
    Tree(4, "Cresça sua Ideia",
         "Percebemos, cada vez mais, que a consulta aos diversos militantes estende o alcance e a importância das diversas correntes de pensamento. Por outro lado, o desafiador cenário globalizado acarreta um processo de reformulação e modernização das novas proposições. A prática cotidiana prova que a revolução dos costumes faz parte de um processo de gerenciamento dos níveis de motivação departamental."),
    Tree(5, "Chatbot Luna",
         "O cuidado em identificar pontos críticos na constante divulgação das informações desafia a capacidade de equalização dos relacionamentos verticais entre as hierarquias. Assim mesmo, o desafiador cenário globalizado pode nos levar a considerar a reestruturação do retorno esperado a longo prazo. No mundo atual, a complexidade dos estudos efetuados cumpre um papel essencial na formulação do orçamento setorial. Caros amigos, o acompanhamento das preferências de consumo representa uma abertura para a melhoria do investimento em reciclagem técnica.")

]

@app.route('/arvores')
def page_arvores():
    return render_template('arvores.html', trees=sorted(trees, key=lambda x: x.votes, reverse=True))

@app.route('/votar/<tree_id>', methods=["GET"])
def vote_on_tree(tree_id=None):
    tree = next(filter(lambda x: x.tree_id == int(tree_id), trees))
    tree.vote()
    return jsonify(votes=tree.votes, stage=tree.stage)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/mapa')
def mapa():
    return render_template('mapa.html')

@app.route('/nlp')
def nlp():
    return render_template('NLP.html')

@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response