import random

from repositories.score_repo import ScoreRepository

n = random.randint(0, 100)

repo = ScoreRepository("test.db")
# repo.update_score(0)
score = repo.get_score()
print(score)
