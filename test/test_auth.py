import coreapi, requests

if __name__ == '__main__':
    
    ## Auth by login with you dont have token yet
    result = requests.post(
        url='http://127.0.0.1:5009/auth/v1/token/', 
        json={
            "username": "lucas", 
            "password": "python2525"
        }
    )
    result = result.json()
    print("result > ", result)

    auth = coreapi.auth.TokenAuthentication(
        scheme='JWT',
        token=result['token']
    )
    client = coreapi.Client(auth=auth)
    print("client by login > ", client)
    
    ## Auth by token with you have it yet
    token = result['token']
    auth = coreapi.auth.TokenAuthentication(
        scheme='JWT',
        token=token
    )
    client = coreapi.Client(auth=auth)
    print("client by token > ", client)