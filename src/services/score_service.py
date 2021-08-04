from loguru import logger

from repositories.score_repo import ScoreRepository


class ScoreService:
    repo: ScoreRepository

    def __init__(self, repo: ScoreRepository = ScoreRepository()):
        self.repo = repo

    def get_highscore(
        self,
    ) -> int:
        return self.repo.get_score()

    def enter_new_score(self, score: int):
        logger.info(f"Entered a new score: {score}")

        high_score = self.get_highscore()
        logger.info(f"Current high score is {high_score}")

        new_high_score = score > high_score
        if new_high_score:
            logger.info(f"High score was beaten, will update it. Congratz!")
            self.repo.update_score(score)
        else:
            logger.info("High score remains unbeaten, will not update it.")
