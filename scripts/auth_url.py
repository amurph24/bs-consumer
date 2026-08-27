import bsapi
from bsapi import oauth
from dotenv import load_dotenv

import requests
from os import environ

def main():

    # Step 0: Load env vars
    load_dotenv()
    client_id = environ["CLIENT_ID"]
    redirect_uri = environ["REDIRECT_URI"]
    client_secret = environ["CLIENT_SECRET"]

    # Step 1: Create authorization URL
    scope = "dropbox:folders:read,write enrollment:orgunit:read enrollment:own_enrollment:read grades:gradeobjects:read grades:gradevalues:write"
    auth_url = oauth.create_auth_url(client_id, redirect_uri, scope)
    print(f'Visit: {auth_url}')

    authorization_code = input("Enter the authorization code after visiting the above link: ")

    # Step 2: After user authorizes, extract code from callback URL
    # callback_url = '<URL user was redirected to>'
    # authorization_code = oauth.parse_callback_url(callback_url)

    # Step 3: Exchange code for access token
    token_response = oauth.exchange_code_for_token(
        client_id, client_secret, redirect_uri, authorization_code
    )
    access_token = token_response['access_token']

    # Step 4: Use access token with API
    lms_url = "https://ubc.brightspace.com"
    api = bsapi.BSAPI(access_token, lms_url)


if __name__ == "__main__":
    main()
