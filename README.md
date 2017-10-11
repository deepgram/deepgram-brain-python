# PLEASE NOTE, THE DEFAULT API LINK IS NOT CURRENTLY VALID. PLEASE USE https://api.deepgram.com

We are in a push to realign naming as we continally improve Deepgram and the interfaces to it. At the moment our api can be accessed at 'https://api.deepgram.com' but that link will shortly change to 'https://brain.deepgram.com'. In anticipation of this the python client has the default api set to 'https://brain.deepgram.com' which will throw an error if you try to use it. Please connect with the following command:

    from deepgram import Brain

    ...

    # Get your user_id and token from deepgram.com/console/documentation
    brainAPI = Brain(url='https://api.deepgram.com', user_id=<user_id>, token=<token>)

This will work now and when the switch happens just remove the url and the default behavior will point to the correct server.

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

    #upload a new asset from a URL
    result = brainAPI.createAssetFromURL('http://some.server.com/someAudioFile.wav')
    print(brainAPI.asset(result['asset_id'])

    #create it from a local file and give it a filename
    with open(audioFileLocation, mode='rb') as audioFile:
      asset = brainAPI.uploadAsset(audioFile, metadata={'filename': filename})



## See the code for more usage and check back often for updates!
