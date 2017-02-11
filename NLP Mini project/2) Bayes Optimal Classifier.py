# -*- coding: utf-8 -*-
"""
Created on Fri Feb 03 13:44:10 2017

@author: DTILAK
"""

#------------------------------------------------------------------

#
#   Bayes Optimal Classifier
#
#   In this quiz we will compute the optimal label for a second missing word in a row
#   based on the possible words that could be in the first blank
#
#   Finish the procedurce, LaterWords(), below
#
#   You may want to import your code from the previous programming exercise!
#
from __future__ import division #used to calculate probability division, without this division relults in 0

sample_memo = '''
Milt, we're gonna need to go ahead and move you downstairs into storage B. We have some new people coming in, and we need all the space we can get. So if you could just go ahead and pack up your stuff and move it down there, that would be terrific, OK?
Oh, and remember: next Friday... is Hawaiian shirt day. So, you know, if you want to, go ahead and wear a Hawaiian shirt and jeans.
Oh, oh, and I almost forgot. Ahh, I'm also gonna need you to go ahead and come in on Sunday, too...
Hello Peter, whats happening? Ummm, I'm gonna need you to go ahead and come in tomorrow. So if you could be here around 9 that would be great, mmmk... oh oh! and I almost forgot ahh, I'm also gonna need you to go ahead and come in on Sunday too, kay. We ahh lost some people this week and ah, we sorta need to play catch up.
'''

corrupted_memo = '''
Yeah, I'm gonna --- you to go ahead --- --- complain about this. Oh, and if you could --- --- and sit at the kids' table, that'd be --- 
'''

data_list = sample_memo.strip().split() #strip removes all whitespace at the start and end, including spaces, tabs, newlines and carriage returns.

words_to_guess = ["ahead","could"]

def LaterWords(sample,word,distance):
    '''@param sample: a sample of text to draw from
    @param word: a word occuring before a corrupted sequence
    @param distance: how many words later to estimate (i.e. 1 for the next word, 2 for the word after that)
    @returns: a single word which is the most likely possibility
    '''
    
    # TODO: Given a word, collect the relative probabilities of possible following words
    # from @sample. You may want to import your code from the maximum likelihood exercise.
    print ("Provided word is '{}' with distance of '{}'.".format(word,distance))
    
    word_location = []
    #check if the given word is in the sample_text
    if (word in sample):
    #Run through the list of splits, searching for word and give the count/location of the preceding word
        for i,word_data in enumerate(data_list):
            if word_data == word:
                #word_location = i; #will provide data one below another
                word_location.append(i)  #this will return an array
        #####print ("The given word exists in the sample text, lets proceed!!!")
    else:
        print ("The given word does not exist in the sample text!!!")
        
    #print word_location
    
    from collections import Counter
    next_words = []
    for next_index in range(len(word_location)):
        next_word_data = data_list[word_location[next_index] + distance]
        next_words.append(next_word_data)
        next_index-=1
    # count the number of time a word has been repeated
    next_counts = Counter(next_words)
    #####print "Next word {}".format(next_counts)
    
    #conver into dataframe simply for easy access
    import pandas as pd 
    import numpy as np
    my_dic = pd.DataFrame(next_counts, index=[0]).T
    print my_dic
    
    #print my_dic[column_number][row_number] -> 0 and 0 pprovides 1st element
    #print my_dic[0][0]

    #probability of each word calculation, prob = number of times of that word/total    
    #for next_index in range(len(word_location)):
    #prob = (my_dic[0][0])/total_number_of_words  #single column, so 0
    #print "Repetation count is {}".format(my_dic[0][0])
    #print "Total number of words is {}".format(total_number_of_words)
    #print "Probability is {}".format(prob)
    
    total = my_dic.sum(axis=0)
    sum_column = total[0]
    #####print "sum is {}".format(sum_column)
    
    total_number_of_words = len(my_dic)   
    total_prob = 0
    Probability_of_each_word = []    
    for prob_next_index in range(total_number_of_words):
        prob = (my_dic[0][prob_next_index])/sum_column
        Probability_of_each_word.append(prob)    
        total_prob = total_prob + prob
        prob_next_index-=1  
    #####print "Probability of each word is {}" .format(Probability_of_each_word)
    #####print "Total probability should be 1.0 and it is {}".format(total_prob)
    
    
    # TODO: Repeat the above process--for each distance beyond 1, evaluate the words that
    # might come after each word, and combine them weighting by relative probability
    # into an estimate of what might appear next.
    
    best_prob = max(Probability_of_each_word)
    best_prob_location = Probability_of_each_word.index(best_prob)
    best_probable_word = (my_dic.index[best_prob_location])
    #type(best_probable_word)
    print "'{}' has best probability of {}".format(best_probable_word,best_prob)
    best_probable_word = str(best_probable_word)
    return (best_probable_word)
    
#print LaterWords(sample_memo,"gonna",1)
#print LaterWords(sample_memo,"ahead",1)
#print LaterWords(sample_memo,"ahead",2)
#print LaterWords(sample_memo,"could",1)
#print LaterWords(sample_memo,"could",2)
#print LaterWords(sample_memo,"be",1)

print LaterWords(sample_memo,"and",1)

#Yeah, I'm gonna need you to go ahead and come complain about this. 
#Oh, and if you could be/just go and sit at the kids' table, that'd be great 
