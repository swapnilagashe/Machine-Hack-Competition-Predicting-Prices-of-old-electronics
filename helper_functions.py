#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 16:11:09 2020

@author: swapnillagashe
"""

import re
import numpy as np
import pandas as pd
import spacy
from spacy.lang.en import English
nlp=English()

all_stopwords = nlp.Defaults.stop_words


def join_feature (list1, list2, list3):
    final_list= []
    if list1 == [] and list2 == []:
        final_list = list3
    elif list1 ==[] and list2 != []:
        final_list =list2
    elif list1 ==[] and list2 == [] and list3 == []:
        final_list = []
    else :
        final_list = list1
    try:
        return final_list[0]
    except:
        return 'None'


def find_substring (text, substring_list):
    text=text.lower()
    found=[]
    for item in substring_list:
        if (' ' + item + ' ') in (' ' + text + ' '):
            found.append(item)
    return found

def remove_stopwords(text):
    text=text.strip()
    doc= nlp(text)
    toks = [tok.text for tok in doc]
    text = ' '.join([word for word in toks if not word in all_stopwords])
    return text

def extract_nums(text, base_num):
    temp = re.findall(r'\d+', text) 
    res = list(map(int, temp)) 
    l= [num for num in res if num > base_num]
    return l

def replace_string(text, str_org, str_replaced):
    
    text=text.replace(str_org, str_replaced)
    text= text.strip()
    return(text)
    
def remove_numbers(text):
    result = ''.join([i for i in text if not i.isdigit()])
    return result
    
def extract_namex(text):
    text= text.lower()
    doc=nlp(text)
    names=[]
    for tok in doc:
        if tok.text.startswith('name'):
            names.append(tok.text)
    return names

def brand_name(code):
    brand='Unknown'
    if code == 0:
        brand='honor'
    elif code == 1:
        brand = 'iphone'
    elif code == 2 :
        brand = 'lenovo'
    elif code == 3:
        brand = 'lg'
    else:
        brand = 'unknown'
    return brand
        


def replace_from_dict(text):
    garbage_to_values= {'name0':'iphone','name271':'lenovo', 'name233':'honor', 10100000 : 'iphone', 'name414':'xs', 'name229':'max'}
    for key in garbage_to_values:
        str1= str(key)
        str2 = str(garbage_to_values[key])
        final_text = replace_string(text, str1, str2)
        text=final_text
    
    return text

def replace_phone_with_brand_name(text,brand_name):
    final_text = replace_string(text, 'phone', brand_name)
    final_text= replace_string(final_text, 'iiphone', 'iphone')
    return final_text


# function to replace the garbage string(namex type) with the brand name
def replace_first_word(text, brand_name):
    text=text.strip()
    doc=nlp(text)
    final_text=text
    first_word = doc[0].text
    if first_word.startswith('name'):
        final_text=replace_string(text, first_word, brand_name)
    return final_text


#def age(text1, text2):
#    keywords = ['old', 'new', 'very new', 'brand new', 'used']
#    all_text= text1 + ' ' + text2
#    age_of_phone = []
#    doc= nlp(all_text)
#    l= [tok.text for tok in doc]
#    try: 
#        for word in keywords:
#            if word in l:
#                index= l.index(word)
#                if index > 1 and index < len(l)-1 :
#                    previous_two_words = l[index-2]+' ' + l[index-1]
#                    age_ = previous_two_words + ' ' + word
#                    age_of_phone.append(age_)
#                
#                elif index ==1 and index < len(l)-1:
#                    age_ = ' '.join(l[0:2]) 
#                    age_of_phone.append(age_)
#                
#    
#        return ' '. join(age_of_phone)
#    except:
#        return 'unknown'
    
def age (text1, text2 ):
    age_dict = {'new': 'new', 'good' : 'new', 'sealed' : 'new', 'excellent': 'new', 'working' : 'old', 'old': 'old', 'age': 'old', 'decent': 'new', ' brand new ': 'new', 'unopened': 'new', 'un opened': 'new', 'latest':'new', 'months':'old', 'unboxed':'new', 'not opened':'new','month':'old','seal': 'new', 'pack': 'new', 'packed': 'new', '1month':'new', '2month': 'new','3months':'new','3month':'new', '4month': 'old','4months':'old', '5month':'old', '5months': 'old','6months':'old','6month':'old', '7month': 'old','7months':'old','8month': 'old','8months':'old', '9month':'old', '9months': 'old','10months':'old','10month':'old', '11month': 'old','11months':'old' ,'12month': 'old','12months':'old' , 'mint':'new', 'untuch':'new', 'untouch': 'new', 'awesome':'new', 'usable':'old', 'used':'old', 'sealpack':'new', 'flawless':'new', 'scratchless':'new'}
    all_text= text1 + ' ' + text2
    all_text_list= all_text.split()
    ages =[]
    for key in age_dict:
        if key in all_text_list:
            ages.append(age_dict[key])
    if ages == []:
        ages.append('unknown')
        
    final_age= max(set(ages), key=ages.count)
    return final_age
    
            
def remove_keywords(text, list_of_words):
    return ' '.join([word for word in text.split() if not word in list_of_words])

def keep_first_n_words(text, n):
    toks= text.split()
    final_text = ' '.join(toks[0:n]) 
    return final_text


def join_model_and_modelx(text1, text2):
    final_text= text1
    if text1 == 'None':
        final_text = text2
    return final_text

#there are many rows where text is like 6gb32gbram, data is lost here if we don't extract it properly
def ram_memory_nums(text):
    new_numbers=re.findall(r'\d+', text)
    final_text = ' '. join(new_numbers)
    return final_text

    
    
    