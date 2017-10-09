# deepgram-brain-python
Python API wrapper for the Deepgram API. Oh yes, it's cool. You should get it.
Better description to follow but here is a quick usage

# install
From git:

    get clone https://github.com/deepgram/deepgram-brain-python.git
    cd deepgram-brain-python
    python setup install

From pypi

    pip install deepgram-brain

# usage
    from deepgram import Brain

    ...

    # Get your user_id and token from deepgram.com/console/documentation
    brainAPI = Brain(user_id=<user_id>, token=<token>)

    # print asset information on all of your assets
    for asset in brainAPI.assets:
      print(brainAPI.asset(asset['asset_id'])

    #just transcribe something
    print(brainAPI.transcribeFromURL('http://some.server.com/someAudioFile.wav'))

    #upload a new asset
    result = brainAPI.createAssetFromURL('http://some.server.com/someAudioFile.wav')
    print(brainAPI.asset(result['asset_id'])



## See the code for more usage and check back often for updates!
