# -*- coding: utf-8 -*-
"""Wahyu Inggil Pratama

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/gist/inggil16/b0f792500f1b610b2bde5a106e7a9e31/welcome-to-colaboratory.ipynb
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import matplotlib.pyplot as plt
#data kapasitas mobil 
capacity = np.array([3,3,4,4,4,4,4,6,6,6])
#data harga mobil (dalam juta rupiah)
car_price = np.array([200,215,250,260,275,280,350,360,375])
# %matplotlib inline
plt.scatter(capacity, car_price)