# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 04:27:40 2018

@author: Tadele Y
"""

'''import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pylab as pl
from matplotlib import cm
from sklearn.metrics import classification_report
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
types = pd.read_table('types.txt')
types.head()
print(types.shape)
print(types['category'].unique())
print(types.groupby('category').size())
sns.countplot(types['category'], label= "count")
plt.show()
types.drop('category_label', axis=1).plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False, figsize=(9,9), 
                                        title='Box Plot for each input variable')
plt.savefig('category_box')
plt.show()
types.drop('category' ,axis=1).hist(bins=30, figsize=(9,9))
pl.suptitle("Histogram for each numeric input variable")
#plt.savefig('catagory hist')
plt.show()

category_names = ['poltics','sport','accident']
x = types[category_names]
y = types['category_label']
cmap = cm.get_cmap('gnuplot')
scatter = pd.scatter_matrix(x, c = y , marker= '0' , s= 40, hist_kwds = {'bins':15}, figsize=(9,9), cmap = cmap)
plt.suptitle('Scatter-matrix for each input variable')
#plt.savefig('category_scatter_matrix')
X_train, X_test, y_train, y_test = train_test_split(x, y, random_state=0)
scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
knn = KNeighborsClassifier()
knn.fit(X_train, y_train)
print('Accuracy of K-NN classifier on training set: {:.2f}'
     .format(knn.score(X_train, y_train)))
print('Accuracy of K-NN classifier on test set: {:.2f}'
     .format(knn.score(X_test, y_test)))
from sklearn.metrics import confusion_matrix
pred = knn.predict(X_test)
print(confusion_matrix(y_test, pred))
print(classification_report(y_test, pred))
import matplotlib.cm as cm
from matplotlib.colors import ListedColormap, BoundaryNorm
import matplotlib.patches as mpatches
import numpy as np

X = types[['poltics', 'sport', 'accident']]
y = types['category_label']
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

def plot_fruit_knn(X, y, n_neighbors, weights):
    X_mat = X[['height', 'width']].as_matrix()
    y_mat = y.as_matrix()

    # Create color maps
    cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF','#AFAFAF'])
    cmap_bold  = ListedColormap(['#FF0000', '#00FF00', '#0000FF','#AFAFAF'])
                                
    clf = KNeighborsClassifier(n_neighbors, weights=weights)
    clf.fit(X_mat, y_mat)

    # Plot the decision boundary by assigning a color in the color map
    # to each mesh point.
    
    mesh_step_size = .01  # step size in the mesh
    plot_symbol_size = 50
    
    x_min, x_max = X_mat[:, 0].min() - 1, X_mat[:, 0].max() + 1
    y_min, y_max = X_mat[:, 1].min() - 1, X_mat[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, mesh_step_size),
                         np.arange(y_min, y_max, mesh_step_size))
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    plt.figure()
    plt.pcolormesh(xx, yy, Z, cmap=cmap_light)

    # Plot training points
    plt.scatter(X_mat[:, 0], X_mat[:, 1], s=plot_symbol_size, c=y, cmap=cmap_bold, edgecolor = 'black')
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())

    patch0 = mpatches.Patch(color='#FF0000', label='poltics')
    patch1 = mpatches.Patch(color='#00FF00', label='sport')
    patch2 = mpatches.Patch(color='#0000FF', label='accident')
    #patch3 = mpatches.Patch(color='#AFAFAF', label='others')
    plt.legend(handles=[patch0, patch1, patch2, patch3])

        
    plt.xlabel('height (cm)')
    plt.ylabel('width (cm)')
    plt.title("4-Class classification (k = %i, weights = '%s')"
              % (n_neighbors, weights))
    
    plt.show()
k_range = range(1, 100)
scores = []

for k in k_range :
    knn = KNeighborsClassifier(n_neighbors = k)
    knn.fit(X_train, y_train)
    scores.append(knn.score(X_test, y_test))
plt.figure()
plt.xlabel('k')
plt.ylabel('accuracy')
plt.scatter(k_range, scores)
plot_fruit_knn(X_train, y_train, 5, 'uniform')
'''

# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 23:32:22 2019

@author: Tadele Y
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score

documents = ["Prime minister dr. abiy have fun",
             "ronaldo score a goal last match.",
             "Ethiopian airline crush yesterday",
             "Ethiopia is under very intense poltical crisis",
             "poltics went off in ethiopia",
             "madrid win the last match",
             "some citizens left the country because of the crisis in the poltics.",
             "five people died because of the car accident."]

vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(documents)

true_k = 3
model = KMeans(n_clusters=true_k, init='k-means++', max_iter=100, n_init=1)
model.fit(X)


order_centroids = model.cluster_centers_.argsort()[:, ::-1]
terms = vectorizer.get_feature_names()
'''for i in range(true_k):
    print("Cluster %d:" % i),
    for ind in order_centroids[i, :5]:
        print(' %s' % terms[ind]),
    print
'''


Y = vectorizer.transform(["air line crush"])
prediction = model.predict(Y)

prediction = int(prediction)

def type_of_interset():
    
    if prediction == 0:
        return 'poltics'
    elif prediction == 1:
        return 'sport'
    elif prediction == 2:
        return 'other'
    

