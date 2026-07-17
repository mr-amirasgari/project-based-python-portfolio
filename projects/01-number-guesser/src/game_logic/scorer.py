class Score:
    def __init__(self, initial_score=100, penalty=10):
        self.initial_score = initial_score
        self.penalty = penalty
        self.current_score = initial_score

    def decrease(self):
        self.current_score -= self.penalty
        self.current_score = max(self.current_score, 0)

    def reset(self):
        self.current_score = self.initial_score

    def get_score(self):
        return self.current_score