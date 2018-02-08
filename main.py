import settings
import twitter
import mecab_parse

def init():
    global TW_CLIENT_KEY, TW_CLIENT_KEY_SECRET, TW_ACCSESS_TOKEN, TW_ACCSESS_TOKEN_SECRET
    TW_CLIENT_KEY = settings.TW_CLIENT_KEY
    TW_CLIENT_KEY_SECRET = settings.TW_CLIENT_KEY_SECRET
    TW_ACCSESS_TOKEN = settings.TW_ACCSESS_TOKEN
    TW_ACCSESS_TOKEN_SECRET = settings.TW_ACCSESS_TOKEN_SECRET

def main():
    tw = twitter.Twitter(
        TW_CK=TW_CLIENT_KEY,
        TW_CK_SE=TW_CLIENT_KEY_SECRET,
        TW_AT=TW_ACCSESS_TOKEN,
        TW_AT_SE=TW_ACCSESS_TOKEN_SECRET
    )
    mp = mecab_parse.MecabParser()

    search_tweet =  tw.search_tweet(
        search_word="漫画",
        result_type="popular",
        count=100
    )
    data = [
        st['text'].replace("\n", "")
        for st in search_tweet["statuses"]
    ]
    data = mp.remove_trash(" ".join(data))
    parsed_text = mp.parse_text(
        data
    )
    data_for_word2vec = mp.parse_word_to_space(
        data
    )
    with open("test.txt", "w+") as f:
        f.write(data_for_word2vec)
    
    print(mp.extract_parsedtext_NVA(
        parsed_text
    ))

if __name__ == '__main__':
    init()
    main()