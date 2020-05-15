
#change on lander to other Lander.

import requests
import json
import time
import sys




URL = str(sys.argv[1])

def ApiCheckHealth():
    try:
        res = requests.get(URL)
       # time.sleep(0.5)
        if res.status_code == 200:
            print("API \t" + URL + "\tSTATUS ====>\t"+ str(res.status_code) )
        else:
            print("API \t" + URL + "\tSTATUS ====>\t"+ str(res.status_code))      
            
    except Exception as er:
        print("error",er)


def main():
    ApiCheckHealth()


if __name__ == "__main__":
    main()