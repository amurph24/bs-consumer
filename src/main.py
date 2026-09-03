from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from config import Settings
from local_bs_api import exchange_code_for_token, create_auth_url

app = FastAPI()


@app.get("/access/")
async def authcode_to_accesstoken(code: str | None = None) -> dict[str, str]:
    """Accept an authorization code and return an access token."""
    data = {}

    token_response = exchange_code_for_token(
        Settings.client_id,
        Settings.client_secret,
        Settings.redirect_uri,
        code,
    )
    access_token = token_response['access_token']

    if access_token:
        data.update({"access_token": access_token})
    return data

@app.get("/generate_authurl/")
async def redirect_authurl():
    """Redirect users to authenticate and authorise the access."""
    # hardcoded
    scope = "dropbox:folders:read,write enrollment:orgunit:read enrollment:own_enrollment:read grades:gradeobjects:read grades:gradevalues:write"
    auth_url = create_auth_url(
        Settings.client_id,
        Settings.redirect_uri,
        scope,
    )
    return RedirectResponse(url=auth_url)


@app.get("/health/live/")
async def health_check() -> dict[str, str]:
    """Quick confirmation that the server is alive."""
    return {"status": "ok"}
