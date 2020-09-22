class Tree:
    def __init__(self, tree_id, title, message):
        self.tree_id = tree_id
        self.title = title
        self.message = message
        self.votes = 0

    def vote(self):
        self.votes += 1