# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 11:01:21 2019

@author: U6077221
"""

import re
import regex
email_validator = re.compile('[a-z]+')
print(email_validator.match('schoolofaiBellevue'))
def valid_email(email):
    return bool(re.search("^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email)) 

valid_email('maria@yahoo.com')
