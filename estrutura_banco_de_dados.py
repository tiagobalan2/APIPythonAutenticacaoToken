from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# criar uma api flask
app = Flask(__name__)
# criar uma instancia de SQLAlchemy
app.config['SECRET_KEY'] = '123ABC'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres.kygjajmpouvbzrzvfqsq:Tiago11balan@aws-0-us-west-1.pooler.supabase.com:5432/postgres'
db = SQLAlchemy(app)
db:SQLAlchemy
# definir a estrutura da tabela Postagem
class Postagem(db.Model):
    __tablename__ = 'postagem'
    id_postagem = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String)
    id_autor = db.Column(db.Integer, db.ForeignKey('autor'))
# definir a estrutura da tabela Autor
class Autor(db.Model):
    __tablename__ = 'autor'
    id_autor = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String)
    email = db.Column(db.String)
    senha = db.Column(db.String)
    admin = db.Column(db.Boolean)
    postagens = db.relationship('Postagem')

def inicializar_banco():
    with app.app_context():
        #executar o comando para criar o banco de dados
        db.drop_all()
        db.create_all()
        # criar usuarios admins
        autor = Autor(nome='tiago', email='tiago@gmail.com', senha='123', admin=True)
        db.session.add(autor)
        db.session.commit()

if __name__ == '__main__':
    inicializar_banco()



















