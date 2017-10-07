import requests
import io
import base64
#license goes here <----

class BrainAPI:
  def __init__(self, **kwargs):
    """Init and store the user's credentials for future calls. If no credentials are supplied the login function must be called .

    :param apiURL:
    :param apiToken: use the passed apiToken to authenticate
    :param username: optional instead of apiToken, must be passed with password
    :param password: optional instead of apiToken, must be passed with username
    :param authenticate: only valid with apiToken. Force a call to the server to authenticate the passed credentials.
    """
    self.apiURL = kwargs.get('apiURL', 'https://api.deepgram.com')
    if any(i in ['username', 'password', 'apiToken'] for i in kwargs):
      self.login(**kwargs)

  def _checkReturn(self, response):
    if response.status_code == 200:
      value = response.json()
      return value
    raise Exception('Call failed: {}'.format(response.status_code))

  @property
  def apiToken(self):
    if self._apiToken is None:
      raise Exception('API Token not set. Either set it or login with a username/password first')
    return self._apiToken

  @apiToken.setter
  def apiToken(self, apiToken):
    self._apiToken = apiToken

  def login(self, **kwargs):
    """Logs the current user into the server with the passed in credentials. If successful the apiToken will be changed to match the passed in credentials.

    :param apiToken: use the passed apiToken to authenticate
    :param username: optional instead of apiToken, must be passed with password
    :param password: optional instead of apiToken, must be passed with username
    :param authenticate: only valid with apiToken. Force a call to the server to authenticate the passed credentials.
    :return:
    """
    if 'apiToken' in kwargs:
      apiToken = kwargs['apiToken']
      if kwargs.get('authenticate', False):
        self._checkReturn(requests.get("{}/users?signed_username={}".format(self.apiURL, apiToken)))
      self.apiToken = apiToken
    else:
      auth = (kwargs['username'], kwargs['password'])
      self.apiToken = self._checkReturn(requests.get("{}/users/login".format(self.apiURL), auth=auth))[
        'signed_username']

  @property
  def user(self):
    return self._checkReturn(requests.get("{}/users?signed_username={}".format(self.apiURL, self.apiToken)))

  @property
  def assets(self):
    returnValue = requests.get("{}/assets?signed_username={}&done=false".format(self.apiURL, self.apiToken))
    return self._checkReturn(returnValue)['results']

  def asset(self, assetId, times=False):
    if times == True:
      returnValue = requests.get("{}/assets/{}?times=true&signed_username={}".format(self.apiURL, assetId, self.apiToken))
      return self._checkReturn(returnValue)
    returnValue = requests.get("{}/assets/{}?signed_username={}".format(self.apiURL, assetId, self.apiToken))
    return self._checkReturn(returnValue)

  def updateAsset(self, assetId, transcript=None, metadata=None):
    body = {}
    if transcript is not None:
      body['transcript'] = transcript
    if metadata is not None:
      body['metadata'] = metadata
    return self._checkReturn(
      requests.put("{}/assets/{}?signed_username={}".format(self.apiURL, assetId, self.apiToken), json=body))


  def createAssetFromURL(self, url, async=True, metadata=None):
    """Users the passed URL to load data. If async=false a json with the result is returned otherwise a json with an asset_id is returned.

    :param url:
    :param metadata: arbitrary additional description information for the asset
    :param async:
    :return:
    """
    audio = {'uri': url}
    config = {'async': async}
    if metadata is not None:
      body = {'audio': audio, 'config': config, 'metadata': metadata}
    else:
      body = {'audio': audio, 'config': config}

    return self._checkReturn(
      requests.post("{}/speech:recognize?signed_username={}".format(self.apiURL, self.apiToken), json=body))

  def uploadAsset(self, data, async=True, metadata=None):
    """Takes an array of bytes or a BufferedReader and uploads it. If async=false a json with the result is returned otherwise a json with an asset_id is returned.
    :param data: array of bytes or BufferedReader
    :param metadata: arbitrary additional description information for the asset
    :param async:
    :return:
    """
    #todo: has atter read would be better here
    if isinstance(data, io.BufferedReader):
      data = data.read()
    assert isinstance(data, bytes)
    data = base64.b64encode(data)
    audio = {'content': data.decode("utf-8")}
    config = {'async': async}

    if metadata is not None:
      body = {'audio': audio, 'config': config, 'metadata': metadata}
    else:
      body = {'audio': audio, 'config': config}

    return self._checkReturn(
      requests.post("{}/speech:recognize?signed_username={}".format(self.apiURL, self.apiToken), json=body))

  def deleteAsset(self, assetId):
    return self._checkReturn(
      requests.delete("{}/assets/{}?signed_username={}".format(self.apiURL, assetId, self.apiToken)))

  def searchAssets(self, query, assetIds, npp=None, page=None, limit=None):
    """

    :param query:
    :param assetIds: list of asset Ids
    :param npp: number per page or None (default) for all results
    :param page: page number to start results from or None (default) for 0
    :param limit: max results or None (default) for no limit
    :return:
    """
    body = {"query":query, 'asset_ids':assetIds}
    if npp is not None:
      body['npp'] = npp
    if page is not None:
      body['p'] = page
    if limit is not None:
      body['limit'] = limit
    return self._checkReturn(
      requests.post("{}/assets/search?signed_username={}".format(self.apiURL, self.apiToken), json=body))