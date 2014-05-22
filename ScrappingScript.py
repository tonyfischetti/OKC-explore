#!/usr/bin/env python -tt

import requests 

session = requests.Session()
#session.auth = ('millovely', 'compaq1')



loginInfo={'password':'compaq1','username':'millovely'}
#http://www.okcupid.com/profile/linnea_borealis
session.post('http://www.okcupid.com/login',params=loginInfo)
t = session.get('http://www.okcupid.com/profile/linnea_borealis')

fh=open("okc_output.txt","w")
fh.write(t.text)
#print(r.text)
#('password':rver