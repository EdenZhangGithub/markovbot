import math
import nltk
import os
import sys
import random

# https://web.stanford.edu/~jurafsky/slp3/3.pdf


def load_data(directory, n):
    contents = []
    n = n - 1

    for filename in os.listdir(directory):
        with open(os.path.join(directory, filename), 'r', encoding="utf-8") as f:
            text = nltk.tokenize.sent_tokenize(f.read())
            
            for sentence in text:
                for subsentence in sentence.split('\n'):

                    subsentence = subsentence.lower()

                    for run in range(n):
                        contents.append("<START>")

                    for word in nltk.tokenize.word_tokenize(subsentence):
                        if word.islower():
                            contents.append(word)

                    for run in range(n): 
                        contents.append("<END>")


    return contents

class Markovchain():
    def __init__(self, ngrams, n):
        self.ngrams = ngrams
        self.ngram_frequency = {}
        self.n = n

    def update(self):  
        # initlize dict of dict.  
        set_ngrams = set(self.ngrams)
        for ngram in set_ngrams:
            state = tuple(x for x in ngram[:self.n-1])
            self.ngram_frequency[state] = {}

        for ngram in self.ngrams: 
            state = tuple(x for x in ngram[:self.n-1])
            next = ngram[self.n-1:]
            
            if next not in self.ngram_frequency[state]:
                self.ngram_frequency[state][next] = 1
            else:
                self.ngram_frequency[state][next] += 1
    
    # start with a random ngram with {<start> smth | <start>} then continue the chain. until it forms with { <end> <end> | smth}
    # then create recursion , for until inf .break when "<end>"
    def generate_text(self):
        prev_state = tuple(("<START>") for i in range(self.n))

        ngram_frequency = self.ngram_frequency
        
        out_string = ""

       
        while(1):
            next_state = prev_state[1:]

            next_token = self.next_token(next_state)
            
            next_state = next_state + next_token

            if(next_token == ("<END>", )):
                return out_string   

            out_string = out_string + ''.join(next_token) + " "

            prev_state = next_state


        

    def get_prob(self, state, context):

        context_counter = self.ngram_frequency[state][context]
        sum_token_counter = sum(self.ngram_frequency[state].values())
            
        return(context_counter / sum_token_counter)


    """
    if we choose best option over and over again, sentence is repetitve, 
    and sometimes can reach to infinity. therefore, we can choose semirandomly. 
    """
    def next_token(self, state):
     
        #given state can calculate a prob
        ngram_prob_density = {}

        #precomute prob
        for context in self.ngram_frequency[state].keys():
            ngram_prob_density[context] = self.get_prob(state, context)
          
        ngram_prob_density = dict(sorted(ngram_prob_density.items(), key=lambda x: x[1], reverse=True))
        sum = 0

        random_probability = random.random()

        for context in ngram_prob_density:
            sum += ngram_prob_density[context]
            if(sum > random_probability):
                return context
