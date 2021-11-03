import markovify
import sys
import requests
import time

# Discord_Token = 
# ChannelID = 

def main(): 
    with open('corpus.txt', 'r', encoding='iso-8859-1') as f:
        text = f.read()

    # Train model
    text_model = markovify.Text(text)
    text_model = text_model.compile()
   
    #random_sentences to send to people >:)
    
    for x in range(10):        
        sendMessage(Discord_Token, ChannelID, text_model.make_sentence())

def sendMessage(token, channel_id, message):
    url = 'https://discord.com/api/v8/channels/{}/messages'.format(channel_id)
    data = {"content": message}
    header = {"authorization": token}
 
    r = requests.post(url, data=data, headers=header)



if __name__ == "__main__":
    main()
