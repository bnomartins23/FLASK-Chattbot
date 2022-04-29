from flask import Flask, render_template, request, url_for
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
import time
time.clock = time.time

app = Flask(__name__)

from conversacoes import conversas

bot = ChatBot("ChattBot")
trainer = ListTrainer(bot)
trainer.train(conversas)
print('Bot iniciado !')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/get')
def get_bot_response():
    userText = request.args.get('msg')
    response = str(bot.get_response(userText))
    res = f"<span style='align: left'>BOT: {response}</span>"
    print(res)
    return res

if __name__ == '__main__':
    app.run()