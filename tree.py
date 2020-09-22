class Tree:
    
    stages = {'seed' : 0, 'sapling' : 5, 'tree': 10}

    def __init__(self, tree_id, title, message):
        self.tree_id = tree_id
        self.title = title
        self.message = message
        self.votes = 0

        self.stage = 'seed'
        self.scaling = 1

    def vote(self):
        self.votes += 1
        self.update_stage()

    def update_stage(self):
        max_value = Tree.stages[self.stage]
        next_stage = self.stage
        for stage, stage_value in Tree.stages.items():
            if stage_value > max_value and stage_value <= self.votes:
                next_stage = stage
        self.stage = next_stage
        