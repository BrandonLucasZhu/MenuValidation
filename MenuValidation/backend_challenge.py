'''
Created on Dec 30, 2017

@author: Brandon
'''

import os
import sys
import requests







if __name__ == "__main__":

    #Get API endpoint response
    response = requests.get("https://backend-challenge-summer-2018.herokuapp.com/challenges.json?id=1&page=1")

