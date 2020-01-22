#S.I.E.R.R.A Trading
#Built By Stephen Flynn

#DO NOT PUT API KEY IN HERE FOR STUPID SECURITY REASONS - Steve
class AlpacaPaperSocket(REST):
    def __init__(self):
        super().__init__(
            key_id='YOUR_KEY_HERE',
            secret_key='YOUR_SECRET_KEY_HERE',
            base_url='https://paper-api.alpaca.markets'
        )
