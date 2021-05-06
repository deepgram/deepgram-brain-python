import requests
import io
import base64

"""
Copyright 2017 Deepgram
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
   http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

class Brain:
  def __init__(self, **kwargs):
    """Init and store the user's credentials for future calls. If no credentials are supplied the login function must be called .

    :param url:
    :param signed_username: use the passed apiToken to authenticate
    :param user_id: optional instead of apiToken, must be passed with token
    :param token: optional instead of apiToken, must be passed with user_id
    :param authenticate: only valid with apiToken. Force a call to the server to authenticate the passed credentials.
    """
    self.url = kwargs.get('url', 'https://brain.deepgram.com')
    if any(i in ['user_id', 'token', 'signed_username'] for i in kwargs):
      self.login(**kwargs)

  def _checkReturn(self, response):
    if response.status_code == 200:
      value = response.json()
      return value
    raise Exception('Call failed: {}'.format(response.status_code))

  @property
  def signedUsername(self):
    if self._signedUsername is None:
      raise Exception('Signed username not set. Either set it or login with a user_id/token first')
    return self._signedUsername

  @signedUsername.setter
  def signedUsername(self, signedUsername):
    self._signedUsername = signedUsername

  def login(self, **kwargs):
    """Logs the current user into the server with the passed in credentials. If successful the apiToken will be changed to match the passed in credentials.

    :param apiToken: use the passed apiToken to authenticate
    :param user_id: optional instead of apiToken, must be passed with token
    :param token: optional instead of apiToken, must be passed with user_id
    :param authenticate: only valid with apiToken. Force a call to the server to authenticate the passed credentials.
    :return:
    """
    if 'signed_username' in kwargs:
      apiToken = kwargs['signed_username']
      if kwargs.get('authenticate', False):
        self._checkReturn(requests.get("{}/users?signed_username={}".format(self.url, apiToken)))
      self.signedUsername = apiToken
    else:
      auth = (kwargs['user_id'], kwargs['token'])
      self.signedUsername = self._checkReturn(requests.get("{}/users/login".format(self.url), auth=auth))[
        'signed_username']

  @property
  def user(self):
    return self._checkReturn(requests.get("{}/users?signed_username={}".format(self.url, self.signedUsername)))

  @property
  def assets(self):
    returnValue = requests.get("{}/assets?signed_username={}&done=false".format(self.url, self.signedUsername))
    return self._checkReturn(returnValue)['results']

  def asset(self, assetId, times=False):
    if times == True:
      returnValue = requests.get("{}/assets/{}?times=true&signed_username={}".format(self.url, assetId, self.signedUsername))
      return self._checkReturn(returnValue)
    returnValue = requests.get("{}/assets/{}?signed_username={}".format(self.url, assetId, self.signedUsername))
    return self._checkReturn(returnValue)

  def updateAsset(self, assetId, transcript=None, metadata=None):
    body = {}
    if transcript is not None:
      body['transcript'] = transcript
    if metadata is not None:
      body['metadata'] = metadata
    return self._checkReturn(
      requests.put("{}/assets/{}?signed_username={}".format(self.url, assetId, self.signedUsername), json=body))


  def createAssetFromURL(self, url, isAsync=False, metadata=None, callback=None):
    """Users the passed URL to load data. If isAsync=false a json with the result is returned otherwise a json with an asset_id is returned.

    :param url:
    :param metadata: arbitrary additional description information for the asset
    :param isAsync:
    :param callback: Callback URL
    :return:
    """
    audio = {'uri': url}
    config = {'isAsync': isAsync}
    if callback is not None:
      config['callback'] = callback
    if metadata is not None:
      body = {'audio': audio, 'config': config, 'metadata': metadata}
    else:
      body = {'audio': audio, 'config': config}

    return self._checkReturn(
      requests.post("{}/speech:recognize?signed_username={}".format(self.url, self.signedUsername), json=body))

  def transcribeFromURL(self, url):
    return self.createAssetFromURL(url, isAsync=False)['transcript']

  def uploadAsset(self, data, isAsync=False, metadata=None, callback=None):
    """Takes an array of bytes or a BufferedReader and uploads it. If isAsync=false a json with the result is returned otherwise a json with an asset_id is returned.
    :param data: array of bytes or BufferedReader
    :param metadata: arbitrary additional description information for the asset
    :param isAsync:
    :param callback: Callback URL
    :return:
    """
    #todo: has atter read would be better here
    if isinstance(data, io.BufferedReader):
      data = data.read()
    assert isinstance(data, bytes)
    data = base64.b64encode(data)
    audio = {'content': data.decode("utf-8")}
    config = {'isAsync': isAsync}
    if callback is not None:
      config['callback'] = callback

    if metadata is not None:
      body = {'audio': audio, 'config': config, 'metadata': metadata}
    else:
      body = {'audio': audio, 'config': config}

    return self._checkReturn(
      requests.post("{}/speech:recognize?signed_username={}".format(self.url, self.signedUsername), json=body))

  def transcribe(self, data):
    return self.uploadAsset(data, isAsync=False)['transcript']

  def deleteAsset(self, assetId):
    return self._checkReturn(
      requests.delete("{}/assets/{}?signed_username={}".format(self.url, assetId, self.signedUsername)))

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
      requests.post("{}/assets/search?signed_username={}".format(self.url, self.signedUsername), json=body))
