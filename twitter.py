from requests_oauthlib import OAuth1Session
import json

class Twitter:
    def __init__(self, TW_CK: str, TW_CK_SE: str, TW_AT: str, TW_AT_SE: str):
        self.session = OAuth1Session(
            TW_CK, TW_CK_SE, TW_AT, TW_AT_SE
        )
    
    def search_tweet(self, search_word="", result_type="", count=15) -> dict:
        url = "https://api.twitter.com/1.1/search/tweets.json"
        params = {
            "q" : search_word.encode("utf-8"),
            "result_type": result_type,
            "counte": count
        }
        req = self.session.get(
            url,
            params=params
        )
        timeline = json.loads(req.text)
        return timeline


if __name__ == '__main__':
    import main
    main.init()
    tw = Twitter(
        TW_CK=main.TW_CLIENT_KEY,
        TW_CK_SE=main.TW_CLIENT_KEY_SECRET,
        TW_AT=main.TW_ACCSESS_TOKEN,
        TW_AT_SE=main.TW_ACCSESS_TOKEN_SECRET
    )
    search_tweet =  tw.search_tweet(
        search_word="漫画",
        result_type="popular",
        count=100
    )
    data = [
        st['text'].replace("\n", "")
        for st in search_tweet["statuses"]
    ]
    print(data)