
Install all requirements by calling `pip install -r requirements.txt`

To install nltk requirements 
```python
import nltk
nltk.download(punkt)
```

Create a new file called secret_settings.py and add usertokens to secret_settings.py to send messages on discord or to scrap data from reddit

```python 
reddit_user_agent = ""
reddit_client_id = ""
reddit_client_secret = ""

discord_token_secret = ''
discord_channel_id
```

To generate the text run `python generator.py n corpus_data`.
The recommended n for ngrams is 2 or 3. 


The text generation has some imperfection as the code is not set to deal with the imperfections of comments from reddit users, therefore users can change the data corpus to something more appropriate  