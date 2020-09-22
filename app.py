from flask import Flask, render_template, redirect
from tree import Tree

app = Flask(__name__)

trees = [
    Tree(0, "Uniformes novos", "Os uniformes em nossa unidade estão antigos, seria muito legal uma nova coleção"),
    Tree(1, "Melhores fones anti-ruído", "Há muito ruído na fábrica, seria legal termos fones de melhor qualidade!")
] 

@app.route('/arvores')
def page_arvores():
    return render_template('arvores.html', trees=sorted(trees, key=lambda x: x.votes, reverse=True))

@app.route('/votar/<tree_id>', methods=["POST"])
def vote_on_tree(tree_id=None):
    next(filter(lambda x: x.tree_id == int(tree_id), trees)).vote()
    return redirect('/arvores')

