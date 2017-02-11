# -*- coding: utf-8 -*-
"""
Created on Thu Feb 02 23:49:36 2017

@author: DTILAK
"""
from collections import Counter
import re
#   Maximum Likelihood Hypothesis
#
#
#   In this quiz we will find the maximum likelihood word based on the preceding word
#
#   Fill in the NextWordProbability procedure so that it takes in sample text and a word,
#   and returns a dictionary with keys the set of words that come after, whose values are
#   the number of times the key comes after that word.
#   
#   Just use .split() to split the sample_memo text into words separated by spaces.


def NextWordProbability(sampletext,word):
    print ("Provided word is '{}'.".format(word))
    #Split the words in sample text to get individual words
    split_words = sampletext.split()   
    
    #to save location
    word_location = []
    preceding_words = []
    next_words = []

    #check if the given word is in the sample_text
    if (word in sampletext):
    #Run through the list of splits, searching for word and give the count/location of the preciding word
        for i,word_data in enumerate(split_words):
            if word_data == word:
                #word_location = i; #will provide data one below another
                word_location.append(i)  #this will return an array
    else:
        print ("!!!The given word does not exist in the sample text!!!")
        
    #print word_location
    #print range(len(word_location))
    
    
    
    #search the preceding word and save it in n array
    for index in range(len(word_location)):
        preceding_word_data = split_words[word_location[index] - 1]
        preceding_words.append(preceding_word_data)
        index-=1
    
    print ("Preceding words to the given word are: {}".format(preceding_words))
    
    # count the number of time a word has been repeated
    preceding_counts = Counter(preceding_words)
    print "Preceding word {}".format(preceding_counts)
    
    
    
    
    #actual answer returns a dictionary with keys the set of words that come after, whose values are
    #the number of times the key comes after that word.
    for next_index in range(len(word_location)):
        next_word_data = split_words[word_location[next_index] + 1]
        next_words.append(next_word_data)
        next_index-=1
    print ("Next words to the given word are: {}".format(next_words))
    # count the number of time a word has been repeated
    next_counts = Counter(next_words)
    print "Next word {}".format(next_counts)

    
    dictionary = {"Next words":next_words, 
                  "Next word count":next_counts}
    #print dictionary
    return {}





sample_memo = '''
Milt, we're gonna need to go ahead and move you downstairs into storage B. We have some new people coming in, and we need all the space we can get. So if you could just go ahead and pack up your stuff and move it down there, that would be terrific, OK?
Oh, and remember: next Friday... is Hawaiian shirt day. So, you know, if you want to, go ahead and wear a Hawaiian shirt and jeans.
Oh, oh, and I almost forgot. Ahh, I'm also gonna need you to go ahead and come in on Sunday, too...
Hello Peter, whats happening? Ummm, I'm gonna need you to go ahead and come in tomorrow. So if you could be here around 9 that would be great, mmmk... oh oh! and I almost forgot ahh, I'm also gonna need you to go ahead and come in on Sunday too, kay. We ahh lost some people this week and ah, we sorta need to play catch up.
'''
    
NextWordProbability(sample_memo,'ahead')
