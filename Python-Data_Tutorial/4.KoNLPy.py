# from konlpy.tag import Kkma
# # from konlpy.tag import Hannanum
# # from konlpy.tag import Twitter    #모듈이 여러개이니 체크 
# Kkma = Kkma()
# print(Kkma.sentences('한국어 분석을 시작합니다 재미있어요~~'))
# print(Kkma.nouns('한국어 분석을 시작합니다 재미있어요~~')) #명사 분석
# print(Kkma.pos('한국어 분석을 시작합니다 재미있어요~~')) #형태소 분석 

#word cloud
# from wordcloud import WordCloud, STOPWORDS
# import matplotlib.pyplot as plt
# import numpy as np
# from PIL import Image

# text=open('./data/09. alice.txt').read()
# alice_mask = np.array(Image.open('./data/09. alice_mask.png'))
# stopwords = set(STOPWORDS)
# stopwords.add("said")   #said는 카운터에서 제거 
# # plt.figure(figsize=(8,8))
# # plt.imshow(alice_mask, cmap=plt.cm.gray, interpolation='bilinear')
# # plt.axis('off')
# wc=WordCloud(background_color='white',max_words=2000, mask=alice_mask,stopwords=stopwords)  #background_color default는 black
# wc=wc.generate(text)
# plt.figure(figsize=(12,12))
# plt.imshow(wc,interpolation='bilinear')
# plt.axis('off')
# plt.show()

#naive bayes classifier
# from nltk import classify
# from nltk.tokenize import word_tokenize
# import nltk
# train=[('i like you', 'pos'),('i hate you', 'neg'),('you like me', 'pos'),('i like her', 'pos')]
# all_words=set(word.lower() for sentence in train for word in word_tokenize(sentence[0]))
# print(all_words)
# t=[({word: (word in word_tokenize(x[0])) for word in all_words} , x[1]) for x in train]
# classfier=nltk.NaiveBayesClassifier.train(t)
# classfier.show_most_informative_features()
# test_sentence='i like Merui'
# test_sentence_features = {word.lower():(word in word_tokenize(test_sentence.lower()))for word in all_words}
# print(classfier.classify(test_sentence_features))

