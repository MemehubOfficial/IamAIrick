# Look Morty! I tuned myself in an AI, Morty. Morty Look, I am AI Rick!!

The purpose of this program is the progressive building of a machine learning algo to make predictions for the steem blockchain with regards to abuse and botnets.

### Installing

Clone this repo. CD into directory.

`pip install r requirements.txt`

To set up the config.py file, here is exactly what to put in the file:

```
default_stmacct = 'your_steem_account_username'
default_passphrase = 'your_beempy_wallet_passphrase'

steemsql_uid = 'your_steemql_userid'
steemsql_pwd = 'your_steemsql_password'

meme_tags = ['memes', 'meme', 'memestagram', 'memeday', 'memechallenge']

#set test = False for mainnet
test = True

#manually set array of cleaner names
cleaners = ['steemflagrewards', 'cheetah', 'steemcleaners', 'mack-bot', 'mack-botjs', 'spaminator']
```

## Deployment

run `AIrick.py` in CLI

## Versioning

This first version downvotes and comments on active bidboted meme posts with pending payout greater than $10.

## Authors

* **Jeremy Meek** - *Initial work* - [MemehubOfficial](https://github.com/MemehubOfficial)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Steemian @arcange - *steemSQL*
* Steemian @themarkymark - *blacklist api*
* SteemFlagRewards @anthonyadavisii - *Pulling ideas from his source code*