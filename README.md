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
    import brain

    ...

    # in the future the api URL will be 'brain.deepgram.com' but for the beta it is brain2
    brainAPI = brain.BrainAPI(apiURL="brain2.deepgram.com",
                            username=<username>,
                            password=<password>)

    # print asset information on all of your assets
    for asset in brainAPI.assets:
      print(brainAPI.asset(asset['asset_id'])

    #upload a new asset
    result = brainAPI.createAssetFromURL('http://some.server.com/someAudioFile.wav', async=False)
    print(brainAPI.asset(result['asset_id'])


## See the code for more usage and check back often for updates!
