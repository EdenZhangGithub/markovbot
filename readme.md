
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
```

To generate the text run `python generator.py corpus_data`
