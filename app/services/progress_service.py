from app.models.progress import Progress
from app.repositories.progress_repository import ProgressRepository
from datetime import date

class ProgressService:
    def __init__(self):
        self.progress_repo = ProgressRepository()

    def create_progress(self, progress_data):
        progress = Progress(
            id=len(self.progress_repo.progresses) + 1,
            user_id=progress_data.user_id,
            activity=progress_data.activity,
            duration=progress_data.duration,
            distance=progress_data.distance,
            intensity=progress_data.intensity,
            calories_burned=progress_data.calories_burned,
            date=progress_data.date,
        )
        return self.progress_repo.create(progress)

    def get_user_progress(self, user_id: int):
        return self.progress_repo.get_by_user_id(user_id)
