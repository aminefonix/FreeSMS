#!/usr/bin/python3
import base64
import time
import os
import sys
try:
    import requests
    
except ImportError:
    print("Error to import 'requests' Library\ntodo : python3 -m pip install requests")
    exit()

banner ="""
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
PPPPPPPPPPPPPPPPP                                                d::::::d                       DDDDDDDDDDDDD                         
P::::::::::::::::P                                               d::::::d                       D::::::::::::DDD                      
P::::::PPPPPP:::::P                                              d::::::d                       D:::::::::::::::DD                    
PP:::::P     P:::::P                                             d:::::d                        DDD:::::DDDDD:::::D                   
  P::::P     P:::::Paaaaaaaaaaaaa  nnnn  nnnnnnnn        ddddddddd:::::d   aaaaaaaaaaaaa          D:::::D    D:::::D zzzzzzzzzzzzzzzzz
  P::::P     P:::::Pa::::::::::::a n:::nn::::::::nn    dd::::::::::::::d   a::::::::::::a         D:::::D     D:::::Dz:::::::::::::::z
  P::::PPPPPP:::::P aaaaaaaaa:::::an::::::::::::::nn  d::::::::::::::::d   aaaaaaaaa:::::a        D:::::D     D:::::Dz::::::::::::::z 
  P:::::::::::::PP           a::::ann:::::::::::::::nd:::::::ddddd:::::d            a::::a        D:::::D     D:::::Dzzzzzzzz::::::z  
  P::::PPPPPPPPP      aaaaaaa:::::a  n:::::nnnn:::::nd::::::d    d:::::d     aaaaaaa:::::a        D:::::D     D:::::D      z::::::z   
  P::::P            aa::::::::::::a  n::::n    n::::nd:::::d     d:::::d   aa::::::::::::a        D:::::D     D:::::D     z::::::z    
  P::::P           a::::aaaa::::::a  n::::n    n::::nd:::::d     d:::::d  a::::aaaa::::::a        D:::::D     D:::::D    z::::::z     
  P::::P          a::::a    a:::::a  n::::n    n::::nd:::::d     d:::::d a::::a    a:::::a        D:::::D    D:::::D    z::::::z      
PP::::::PP        a::::a    a:::::a  n::::n    n::::nd::::::ddddd::::::dda::::a    a:::::a      DDD:::::DDDDD:::::D    z::::::zzzzzzzz
P::::::::P        a:::::aaaa::::::a  n::::n    n::::n d:::::::::::::::::da:::::aaaa::::::a      D:::::::::::::::DD    z::::::::::::::z
P::::::::P         a::::::::::aa:::a n::::n    n::::n  d:::::::::ddd::::d a::::::::::aa:::a     D::::::::::::DDD     z:::::::::::::::z
PPPPPPPPPP          aaaaaaaaaa  aaaa nnnnnn    nnnnnn   ddddddddd   ddddd  aaaaaaaaaa  aaaa     DDDDDDDDDDDDD        zzzzzzzzzzzzzzzzz
     Telegram>  https://t.me/Pandadz    +213558036534"             
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
  
    """
os.system('clear') 
print(banner)

p = input("Enter a phone number : > ")
m = input("Enter the text message : > ")
resp = requests.post('https://textbelt.com/text', {
        'phone': (p),
        'message': (m), 
        'key': 'textbelt',      
})

try:
    int(p) 
    print("\n\t\t[ + ] plase wait ..... ")
    time.sleep( 5 )
    print(resp.json())
    

except:
    print("\n\t[!] Error sending the message")
    print("\t[!] Please enter the number  \n ")
