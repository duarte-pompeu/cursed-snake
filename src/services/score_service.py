from repositories.score_repo import ScoreRepository


class ScoreService:
    repo : ScoreRepository
    
    def __init__(self, repo: ScoreRepository = ScoreRepository()):
        self.repo = repo

    def get_highscore(self,) -> int:
        return self.repo.get_score()
    
    def enter_new_score(self, score: int):
        current_score = self.get_highscore()

        if current_score < score:
            self.repo.update_score(current_score)

        

