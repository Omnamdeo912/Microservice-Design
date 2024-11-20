import os, requests


def login(request):
    auth = request.authorization
    if not auth:
        return None, ("missing credentials", 401)

    basicAuth = (auth.username, auth.password)                #login me to username aur passowrd aayega token to login ke bad wale serbices me dalte hai

    response = requests.post(                                  # Here we are making req to our auth micro service
        f"http://{os.environ.get('AUTH_SVC_ADDRESS')}/login", auth=basicAuth
    )

    if response.status_code == 200:
        return response.text, None
    else:
        return None, (response.text, response.status_code)
