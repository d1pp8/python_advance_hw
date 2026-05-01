from app.extension import db

class Question(db.Model):
    __tablename__ = 'questions'

    id =  db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)

    responses = db.relationship('Response', backref='question', lazy=True)
    category = db.relationship('Category', backref='questions')


    def __repr__(self):
        return f'Question: {self.text}'


class Statistic(db.Model):
    __tablename__ = 'statistic'

    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'), primary_key=True)
    agree_count = db.Column(db.Integer, nullable=False, default=0)
    disagree_count = db.Column(db.Integer, nullable=False, default=0)

    question = db.relationship('Question', backref = db.backref('statistic', uselist=False))

    def __repr__(self):
        return f"<Statistic for Question {self.question_id}: {self.agree_count} agree, {self.disagree_count} disagree>"