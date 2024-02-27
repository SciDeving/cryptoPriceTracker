from os import environ

import requests
from requests.sessions import Session

session: Session = requests.session()
session.headers["X-CMC_PRO_API_KEY"] = environ["CMC_API_KEY"]
