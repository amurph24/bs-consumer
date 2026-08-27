from dataclasses import dataclass
import os

@dataclass(frozen=True)
class Settings:
    """Server settings read from env vars on import."""

    client_id: str = os.environ["CLIENT_ID"]
    client_secret: str = os.environ["CLIENT_SECRET"]
    redirect_uri: str = os.environ["REDIRECT_URI"]
