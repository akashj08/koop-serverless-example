
#change on lander to other Lander.

import requests
import json
import time




URL = "https://hdhdpxipga.execute-api.us-east-1.amazonaws.com/dev/my-provider/{host}/FeatureServer/0"
success_list = []
failure_list = []


def ApiCheckHealth():
    try:
        res = requests.get(URL)
            time.sleep(0.5)
            if res.status_code == 200:
                print("Api is up now")
            else:
                print("Api is not Up")      
            
    except Exception as er:
        print("error",er)


def main():
    ApiCheckHealth()


if __name__ == "__main__":
    main()