from app import db

class Task(db.Model):
    __tablename__ = 'Task'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(
        db.String(100), nullable=False)
    status = db.Column(db.Integer, nullable=False)

    def __init__(self, name, status):
        self.name = name
        self.status = status

    def find_all():
        tasks = Task.query.all()
        return tasks
    
    def find_one(id):
        task = Task.query.filter_by(id=id).first()
        return task
    
    def create(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()
