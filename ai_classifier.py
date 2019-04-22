# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 23:32:22 2019

@author: Tadele Y
"""
import math
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score
import hackathon

documents = ["Ethiopia is under danger",
             "Merley has the best squooshy kitten belly.",
             "Google Translate app is incredible.",
             "If you open 100 tab in google you get a smiley face.",
             "Best cat photo I've ever taken.",
             "Climbing ninja cat.",
             "Impressed with google map feedback.",
             "Key promoter extension for Google Chrome."
		"Ethiopia is under danger",
             "Merley has the best squooshy kitten belly.",
             "Google Translate app is incredible.",
             "If you open 100 tab in google you get a smiley face.",
             "Best cat photo I've ever taken.",
             "Climbing ninja cat.",
             "Impressed with google map feedback.",
             "Key promoter extension for Google Chrome.""Ethiopia is under danger",
             "Merley has the best squooshy kitten belly.",
             "Google Translate app is incredible.",
             "If you open 100 tab in google you get a smiley face.",
             "Best cat photo I've ever taken.",
             "Climbing ninja cat.",
             "Impressed with google map feedback.",
             "Key promoter extension for Google Chrome.""Ethiopia is under danger",
             "Merley has the best squooshy kitten belly.",
             "Google Translate app is incredible.",
             "If you open 100 tab in google you get a smiley face.",
             "Best cat photo I've ever taken.",
             "Climbing ninja cat.",
             "Impressed with google map feedback.",
             "Key promoter extension for Google Chrome."]

vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(documents)

true_k = 2
model = KMeans(n_clusters=true_k, init='k-means++', max_iter=100, n_init=1)
model.fit(X)

print("Top terms per cluster:")
order_centroids = model.cluster_centers_.argsort()[:, ::-1]
terms = vectorizer.get_feature_names()
for i in range(true_k):
    
    for ind in order_centroids[i, :10]:
        print(' %s' % terms[ind]),
   
value = hackathon.global_return()
Y = vectorizer.transform([str(value)])
prediction = model.predict(Y)

prediction = int(prediction)
def sigmoid(number)-> float:
    number = prediction 
    return 1/(1+math.exp(-number))

value = sigmoid(prediction)
def percentage():
    ans = value * 100
    return ans
    
def real_guesser():
    ans = percentage()
    ans = round(ans, 2)
    return ans

def fake_guesser():
    real = real_guesser()
    ans = 100 -real
    return ans
