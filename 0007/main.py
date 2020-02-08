import berserk
from .game import Game

with open('./lichessAccessToken.token') as f:
    token = f.read()
session = berserk.TokenSession(token)
client = berserk.Client(session)

for event in client.bots.stream_incoming_events():
    if event['type'] == 'challenge':
        client.bots.accept_challenge(event['challenge']['id'])
    elif event['type'] == 'gameStart':
        game_id = event['game']['id']
        game = Game(client, game_id)
        game.start()
    else:
        print(event)
