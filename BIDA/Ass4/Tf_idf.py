# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 20:54:40 2020

@author: humne
"""

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
documentA="HI, MY NAME IS HARSHAL AND I STUDY IN VIIT"
documentB="I AM DIGVIJAY PAWAR AND I AM PURSUIG MY COMPUTER ENGINEERING FROM VIIT"
vectorize= TfidfVectorizer()
respose= vectorize.fit_transform([documentA, documentB])
print(respose)



