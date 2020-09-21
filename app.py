from flask import Flask, render_template, redirect
app = Flask(__name__)

class Tree:
    def __init__(self, tree_id, title, message):
        self.tree_id = tree_id
        self.title = title
        self.message = message
        self.votes = 0

    def vote(self):
        self.votes += 1
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

