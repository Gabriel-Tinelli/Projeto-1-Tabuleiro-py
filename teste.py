from models.games import Games
from app.app import app


if __name__ == '__main__':
    with app.app_context():

        teste = Games.query.get_or_404(1)
        print(teste.name)