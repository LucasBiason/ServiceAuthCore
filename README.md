# authservice

API for Users and customers control. Can be used to start new projects from zero.
Authentication with JWT at Django Rest Framework

#### JWT Auth

import coreapi, requests

*Auth by login with you dont have token yet*
```python
result = requests.post(
    url='http://127.0.0.1:5009/auth/v1/token/', 
    json={
        "username": "lucas", 
        "password": "python2525"
    }
)
result = result.json()
token = result['token']
print("result > ", result)

```

Auth by token with you have it yet
*Auth by token with you have it yet*
```python
auth = coreapi.auth.TokenAuthentication(
    scheme='JWT',
    token=token
)
client = coreapi.Client(auth=auth)
print("client by token > ", client)
```
