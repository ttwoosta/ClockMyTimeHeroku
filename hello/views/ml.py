#
# Filename: stock.py
# Project : Clock My Time
#
# Created by Tu Tong on 05/18/20
# Copyright 2020 Tu Tong. All rights reserved.
#

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.middleware import csrf
from django.views.decorators.csrf import ensure_csrf_cookie
from django.conf import settings
from django.contrib.auth.models import User
import numpy as np
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from io import BytesIO

def predict_score(request):
    fig, ax = plt.subplots()  # Create a figure containing a single axes.
    ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the axes.
    
    img = BytesIO()
    fig.savefig(img)
    img.seek(0)

    return HttpResponse(img, content_type='image/png')

def breat_cancer(request):
    return render(request, "sample.html")

def breat_cancer_fig(request):

    # load breast cancer dataset
    ds = datasets.load_breast_cancer()

    # Create features and target arrays
    X = ds.data
    y = ds.target

    # Split into training and test set
    X_train, X_test, y_train, y_test = train_test_split(X, y, 
        test_size=0.2, random_state=42, stratify=y)

    # Setup arrays to store train and test accuracies    
    neighbors = np.array([1, 5, 10, 15])
    train_accuracy = np.empty(len(neighbors))
    test_accuracy = np.empty(len(neighbors))

    for i, k in enumerate(neighbors):
        
        # Create a k-NN classifier with k neighbors
        knn = KNeighborsClassifier(k)

        # Fit the classifier to the training data
        knn.fit(X_train, y_train)

        #Compute accuracy on the training set
        train_accuracy[i] = knn.score(X_train, y_train)

        #Compute accuracy on the testing set
        test_accuracy[i] = knn.score(X_test, y_test)

    # Generate plot
    fig, ax = plt.subplots()

    ax.set_title('k-NN: Varying Number of Neighbors')
    ax.plot(neighbors, test_accuracy, label = 'Testing Accuracy')
    ax.plot(neighbors, train_accuracy, label = 'Training Accuracy')
    ax.legend()
    ax.set_xlabel('Number of Neighbors')
    ax.set_ylabel('Accuracy')

    img = BytesIO()
    fig.savefig(img)
    img.seek(0)

    return HttpResponse(img, content_type='image/png')
