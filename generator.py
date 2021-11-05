import sys
import requests
import time
import nltk

from markovchain import Markovchain, load_data
from secret_settings import * 

Discord_Token = discord_token_secret
# ChannelID = 

def main(): 

    # n amount of n-grams
    n = 3
    corpus = load_data(sys.argv[1], n)

    ngrams = list(nltk.ngrams(corpus, n))

    model = Markovchain(ngrams, n)
    model.update()
    sentence = model.generate_text()
    print(sentence)

    # uncomment this message to send messages to your friends on discord
    # sendMessage(Discord_Token, ChannelID, sentence)

def sendMessage(token, channel_id, message):
    url = 'https://discord.com/api/v8/channels/{}/messages'.format(channel_id)
    data = {"content": message}
    header = {"authorization": token}
 
    r = requests.post(url, data=data, headers=header)



if __name__ == "__main__":
    main()
