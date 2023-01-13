# pyPPL 📦📦
Czech PPL (Professional Parcel Logistic) API wrapper written in Python. Helps you to communicate with PPL myAPI without worring about constructing your own SOAP headers, bodies or even fetching access tokens. All (hopefully) done for you in the background.

# Install it from PyPI
```bash
pip install pyPPL
```

## Usage

1. Create a `.env` file in the root of your project and fill it with your credentials. You can find an example below.
### `.env` example
```raw
REST_API_URL=https://api.dhl.com/ecs/ppl/myapi2/ # keep this one
REST_OAUTH2_TOKEN_URL=https://api.dhl.com/ecs/ppl/myapi2/login/getAccessToken # keep this one
REST_GRANT_TYPE=client_credentials
REST_CLIENT_ID=12345 # <-- change this one
REST_CLIENT_SECRET=your_secret # <-- change this one
SOAP_CUST_ID=12345 # <-- change this one
SOAP_PASSWORD=your_password # <-- change this one
SOAP_USERNAME=your_username # <-- change this one
SOAP_ACTION_URL=http://myapi.ppl.cz/v1/IMyApi2/ # keep this one
SOAP_API_URL=https://myapi.ppl.cz/MyApi.svc # keep this one
```

### Example
```python
from pyPPL import SOAPConnector
# TODO
```


## Development
If you're keen on contributing to this project, you can do so by forking this repository and creating a pull request. Please make sure to follow the [PEP8](https://www.python.org/dev/peps/pep-0008/) style guide.