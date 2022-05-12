from sqlalchemy import ForeignKey
from app import db


class Task(db.Model):
    task_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    completed_at = db.Column(db.DateTime)
    goal_id = db.Column(db.Integer, db.ForeignKey('goal.goal_id'), nullable=True)
    goal = db.relationship("Goal", backref="tasks")

    def return_task_dict(self):
        if self.completed_at:
            status = True
        else:
            status = False
        return {
            "id": self.task_id,
            "title": self.title,
            "description": self.description,
            "is_complete": status
        }