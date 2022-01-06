منبع:https://towardsdatascience.com/spam-classifier-in-python-from-scratch-27a98ddd8e73
```
import pandas as pd
import numpy as np



train_spam = [line.strip() for line in open('/content/spam.txt')]
train_ham = ['سلام چطوری','بیا پایین', 'رسیدم']
test_emails = {'spam':[line.strip() for line in open('/content/sms_data.txt', encoding='utf-16')], 'ham':[line.strip() for line in open('/content/sms_data.txt', encoding='utf-16')]}
vocab_words_spam = []

for sentence in train_spam:
    sentence_as_list = sentence.split()
    for word in sentence_as_list:
        vocab_words_spam.append(word)     
        
print(vocab_words_spam)

vocab_unique_words_spam = list(dict.fromkeys(vocab_words_spam))
print(vocab_unique_words_spam)

ict_spamicity = {}
for w in vocab_unique_words_spam:
    emails_with_w = 0     # counter
    for sentence in train_spam:
        if w in sentence:
            emails_with_w+=1
            
    print(f"Number of spam emails with the word {w}: {emails_with_w}")
    total_spam = len(train_spam)
    spamicity = (emails_with_w+1)/(total_spam+2)
    print(f"Spamicity of the word '{w}': {spamicity} \n")
    dict_spamicity[w.lower()] = spamicity

vocab_words_ham = []

for sentence in train_ham:
    sentence_as_list = sentence.split()
    for word in sentence_as_list:
        vocab_words_ham.append(word)
        
vocab_unique_words_ham = list(dict.fromkeys(vocab_words_ham))
print(vocab_unique_words_ham)

dict_hamicity = {}
for w in vocab_unique_words_ham:
    emails_with_w = 0     # counter
    for sentence in train_ham:
        if w in sentence:
            print(w+":", sentence)
            emails_with_w+=1
            
    print(f"Number of ham emails with the word '{w}': {emails_with_w}")
    total_ham = len(train_ham)
    Hamicity = (emails_with_w+1)/(total_ham+2)       # Smoothing applied
    print(f"Hamicity of the word '{w}': {Hamicity} ")
    dict_hamicity[w.lower()] = Hamicity
                                         # Use built-in lower() to keep all words lower case - useful later when 
                                         # comparing spamicity vs hamicity of a single word - e.g. 'Your' and
                                         # 'your' will be treated as 2 different words if not normalized to lower   
                                         
prob_spam = len(train_spam) / (len(train_spam)+(len(train_ham)))
print(prob_spam)             

prob_ham = len(train_ham) / (len(train_spam)+(len(train_ham)))
print(prob_ham)                         

tests = []
for i in test_emails['spam']:
    tests.append(i)
    
for i in test_emails['ham']:
    tests.append(i)
    
print(tests)    
# split emails into distinct words
distinct_words_as_sentences_test = []
for sentence in tests:
    sentence_as_list = sentence.split()
    senten = []
    for word in sentence_as_list:
        senten.append(word)
    distinct_words_as_sentences_test.append(senten)
        
print(distinct_words_as_sentences_test)   

reduced_sentences_spam_test = []
for sentence in test_spam_tokenized:
    words_ = []
    for word in sentence:
        if word in vocab_unique_words_spam:
            print(f"'{word}', ok")
            words_.append(word)
        elif word in vocab_unique_words_ham:
            print(f"'{word}', ok")
            words_.append(word)
        else:
            print(f"'{word}', word not present in labelled spam training data")
    reduced_sentences_spam_test.append(words_)
print(reduced_sentences_spam_test)   

reduced_sentences_ham_test = []                   # repeat for ham words
for sentence in test_ham_tokenized:
    words_ = []
    for word in sentence:
        if word in vocab_unique_words_ham:
            print(f"'{word}', ok")
            words_.append(word)
        elif word in vocab_unique_words_spam:
            print(f"'{word}', ok")
            words_.append(word)
        else:
            print(f"'{word}', word not present in labelled ham training data")
    reduced_sentences_ham_test.append(words_)
print(reduced_sentences_ham_test)             

test_spam_stemmed = []
non_key = ['سلام',  'من', 'برای','تو']       # non-key words, gathered from spam,ham and test sentences
for email in reduced_sentences_spam_test:
    email_stemmed=[]
    for word in email:
        if word in non_key:
            print('remove')
        else:
            email_stemmed.append(word)
    test_spam_stemmed.append(email_stemmed)
            
test_ham_stemmed = []
non_key = ['سلام',  'من', 'برای','تو'] 
for email in reduced_sentences_ham_test:
    email_stemmed=[]
    for word in email:
        if word in non_key:
            print('remove')
        else:
            email_stemmed.append(word)
    test_ham_stemmed.append(email_stemmed)
            
print(test_ham_stemmed)

def mult(list_) :        # function to multiply all word probs together 
    total_prob = 1
    for i in list_: 
         total_prob = total_prob * i  
    return total_prob

def Bayes(email):
    probs = []
    for word in email:
        Pr_S = prob_spam
        print('prob of spam in general ',Pr_S)
        try:
            pr_WS = dict_spamicity[word]
            print(f'prob "{word}"  is a spam word : {pr_WS}')
        except KeyError:
            pr_WS = 1/(total_spam+2)  # Apply smoothing for word not seen in spam training data, but seen in ham training 
            print(f"prob '{word}' is a spam word: {pr_WS}")
            
        Pr_H = prob_ham
        print('prob of ham in general ', Pr_H)
        try:
            pr_WH = dict_hamicity[word]
            print(f'prob "{word}" is a ham word: ',pr_WH)
        except KeyError:
            pr_WH = (1/(total_ham+2))  # Apply smoothing for word not seen in ham training data, but seen in spam training
            print(f"WH for {word} is {pr_WH}")
            print(f"prob '{word}' is a ham word: {pr_WH}")
        
        prob_word_is_spam_BAYES = (pr_WS*Pr_S)/((pr_WS*Pr_S)+(pr_WH*Pr_H))
        print('')
        print(f"Using Bayes, prob the the word '{word}' is spam: {prob_word_is_spam_BAYES}")
        print('###########################')
        probs.append(prob_word_is_spam_BAYES)
    print(f"All word probabilities for this sentence: {probs}")
    final_classification = mult(probs)
    if final_classification >= 0.5:
        print(f'sms is SPAM: with spammy confidence of {final_classification*100}%')
    else:
        print(f'sms is HAM: with spammy confidence of {final_classification*100}%')
    return final_classification
for sms in test_spam_stemmed:
    print('')
    print(f"           Testing stemmed SPAM email {email} :")
    print('                 Test word by word: ')
    all_word_probs = Bayes(email)
    print(all_word_probs)   
```
![spam](https://user-images.githubusercontent.com/94211519/148329458-1369c694-ab07-47a7-88a8-71faf769a646.PNG)
