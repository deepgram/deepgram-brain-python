# https://brain.deepgram.com is now live
During testing/beta we were using https://api.deepgram.com for our rest API. This has now moved to https://brain.deepgram.com. This is the default URL in the python client so if you are using the client for the first time you shouldn't notice a change. For those users that were using the client anc connecting using the url parameter, just remove the url and let the default take over and you should be up and running!

# deepgram-brain-python
Python API wrapper for the Deepgram API. Oh yes, it's cool. You should get it.
Here is a quick usage

# install
From git:

    get clone https://github.com/deepgram/deepgram-brain-python.git
    cd deepgram-brain-python
    python setup install

From pypi

    pip install deepgram-brain

# usage Python 3.X
    from deepgram import Brain

    ...

    # Get your user_id and token from deepgram.com/console/documentation
    brainAPI = Brain(user_id=<user_id>, token=<token>)

    # print asset information on all of your assets
    for asset in brainAPI.assets:
      print(brainAPI.asset(asset['asset_id'])

    #just transcribe something
    print(brainAPI.transcribeFromURL('http://some.server.com/someAudioFile.wav'))

    #upload a new asset from a URL
    result = brainAPI.createAssetFromURL('http://some.server.com/someAudioFile.wav')
    print(brainAPI.asset(result['asset_id'])

    #create it from a local file and give it a filename
    with open(audioFileLocation, mode='rb') as audioFile:
      asset = brainAPI.uploadAsset(audioFile, metadata={'filename': filename})

# usage Python 2.X
We are not planning to support python 2.X so we highly encourage upgrading to 3.X. Having said that, the current version should work with 2.X, however when uploading a file you will need to send it as an array of bytes so the example above should now look like:

    ...
    #create it from a local file and give it a filename
    with open(audioFileLocation, mode='rb') as audioFile:
      asset = brainAPI.uploadAsset(audioFile.read(), metadata={'filename': filename})
    ...


## See the code for more usage and check back often for updates!
