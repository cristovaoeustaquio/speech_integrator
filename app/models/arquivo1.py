from app import db

class ClasseModelo1(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)

    def __repr__(self):
        return f'ClasseModelo1(id={self.id}, nome={self.nome}, email={self.email})'
