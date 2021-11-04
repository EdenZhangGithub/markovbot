import math
import nltk
import os
import sys
import random

# https://web.stanford.edu/~jurafsky/slp3/3.pdf

def main():
    # n amount of n-grams
    n = 3

    corpus = load_data(sys.argv[1], n)
    # print(f"test: {corpus}")

    ngrams = list(nltk.ngrams(corpus, n))

    # print(ngrams)
    model = markovchain(ngrams, n)
    model.update()
    model.generate_text()

    # print(model.ngram_counter)


def load_data(directory, n):
    contents = []
    n = n - 1
    i = 0

    # need to remodel the sentences. e.g. <start> and end with <end>
    for filename in os.listdir(directory):
        with open(os.path.join(directory, filename), 'r', encoding="utf-8") as f:
            text = f.read().split("\n")
            
            for sentence in text:
                sentence = sentence.lower()

                for run in range(n):
                    contents.append("<START>")

                for word in nltk.tokenize.word_tokenize(sentence):
                    if word.islower():
                        contents.append(word)

                for run in range(n): 
                    contents.append("<END>")

    return contents

class markovchain():
    def __init__(self, ngrams, n):
        self.ngrams = ngrams
        self.ngram_frequency = {}
        # test
        # self.ngram_counter = {}
        self.n = n

    # fix to prob density
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



            # print(f"{ngram[:n-1]}", " ", {ngram})
            # state = [ngram[:n-1]]
            # if state not in self.ngram_frequency:


            # if(ngram[:n-1] not in self.ngram_frequency):
            #     self.ngram_frequency[ngram[:n-1]] = state
            # else:
            #     if(ngram[n-1:] not in self.ngram_frequency[ngram[:n-1]]):         
            #         self.ngram_frequency[ngram[:n-1]] = state
            #     else:
            #         self.ngram_frequency[ngram[:n-1]][state] += 1
            
            # print(self.ngram_frequency)
                

            # if ngram not in self.ngram_counter: 
            #     self.ngram_counter[ngram] = 1
            # else:
            #     self.ngram_counter[ngram] += 1 
    
    # start with a random ngram with {<start> smth | <start>} then continue the chain. until it forms with { <end> <end> | smth}
    # then create recursion , for until inf .break when "<end>"
    def generate_text(self):
        start_state = tuple(("<START>") for i in range(self.n-1))
        # print(self.ngram_frequency[start])
        ngram_frequency = self.ngram_frequency
        r = random.choice(list(ngram_frequency[start_state].keys()))

        test = self.next_token(start_state)

    def get_prob(self, state, context):

        context_counter = self.ngram_frequency[state][context]
        sum_token_counter = sum(self.ngram_frequency[state].values())
        
        # print(context)
        return(context_counter / sum_token_counter)

    #if we choose best option over and over again, sentence is repetitve, and sometimes can reach to infinity.
    #therefore, we can choose semirandomly. 
    def next_token(self, state):
        #gives a num from 0 -> 1
        random_probability = random.random()
        
        #given state can calculate a prob
        ngram_prob_density = {}

        #precomute prob
        for context in self.ngram_frequency[state].keys():
            ngram_prob_density[context] = self.get_prob(state, context)
          
        ngram_prob_density = sorted(ngram_prob_density.items(), key=lambda x: x[1], reverse=True)
        sum = 0
        print(ngram_prob_density)

        for context in ngram_prob_density:
            # print(context)
            sum += ngram_prob_density[context]
            print(ngram_prob_density[context])
            # print(sum)
            #sum should add to one. what the fuck?
            

if __name__ == "__main__":
    main()