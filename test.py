# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 18:24:55 2020

@author: admin
"""
# coding=utf-8
import urllib
import requests
import re

import pandas as pd
import numpy as np
import tushare as ts
from selenium import webdriver
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import json
import time

df = ts.get_k_data("600519",start="2010-01-01")
df.to_csv("600519.csv")

df = pd.read_csv("600519.csv",index_col="date",parse_dates=["date"])[["open","close","high","low"]]
print(df.head())


