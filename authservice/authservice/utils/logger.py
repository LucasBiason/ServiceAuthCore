import requests
from django.conf import settings


def make_logger(message, id_user=None, kind='INFO', trace=''):
    try: 
        URL = settings.URL_LOGGER_SERVICE
        if not URL:
            raise Exception(" NO URL_LOGGER_SERVICE CONFIG")
        
        PARAMS = { 
            "message": message, 
            "kind": kind, 
            "trace": trace, 
            "id_user": id_user 
        }
        result = requests.put(url=URL, json=PARAMS)
        if not result.status_code == 200:
            raise Exception(str(result.content))
        
    except Exception as e:
        print(" ERROR AT LOGGER SERVICE: {}".format(e))  # TODO: pass to python logging
    
    return None
