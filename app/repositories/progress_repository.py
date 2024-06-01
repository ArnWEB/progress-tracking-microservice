from app.models.progress import Progress

class ProgressRepository:
    def __init__(self):
        self.progresses = []

    def create(self, progress: Progress):
        self.progresses.append(progress)
        return progress

    def get_by_user_id(self, user_id: int):
        return [progress for progress in self.progresses if progress.user_id == user_id]
