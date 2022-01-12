
Install all requirements by calling `pip install -r requirements.txt`

To install nltk requirements 
```python
import nltk
nltk.download(punkt)
```

Create a new file called secret_settings.py and add usertokens to secret_settings.py to send messages on discord or to scrap data from reddit
To only send messages on discord do not need first 3 secret tokens as used for reddit.

```python 
# string
reddit_user_agent = ""
reddit_client_id = ""
reddit_client_secret = ""

# string
discord_token_secret = ''
# integar 
discord_channel_id = 
```

discord token secret is found through:
```inspect element -> application -> local storage -> token```

discord channel id can be found through:
```inspect element -> network -> messages -> channelid```


To generate the text run `python generator.py n corpus_data`.
The recommended n for ngrams is 2 or 3. 


The text generation has some imperfection as the code is not set to deal with the imperfections of comments from reddit users, therefore users can change the data corpus to something more appropriate  
