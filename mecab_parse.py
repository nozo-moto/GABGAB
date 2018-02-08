class MecabParser():
    def __init__(self):
        import MeCab
        self.mecab = MeCab.Tagger(
            "-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd"
        )
        self.mecab_parse_word = MeCab.Tagger(
            "-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd -Owakati"
        )
    
    def remove_trash(self, text: str) -> str:
        import re
        text = re.sub(r"(https?|ftp)(:\/\/[-_\.!~*\'()a-zA-Z0-9;\/?:\@&=\+\$,%#]+)", "" ,text)
        text = re.sub(r"(@?|ftp)([-_\.!~*\'()a-zA-Z0-9;\/?:\@&=\+\$,%#]+)", "" ,text)
        return text


    def parse_text(self, text:str) -> str:
        result = self.mecab.parse(text)
        return result
    
    def extract_parsedtext_NVA(self, parsed_text: str) -> list:
        parsed_text = parsed_text.replace("\t", ",")
        data = parsed_text.split("\n")
        extracted_list = [d.split(",") for d in data]
        result_list =  [
            el[0]
            for el in extracted_list
            if len(el) > 3
            if el[1] in "名詞" or el[1] in "形容詞" or el[1] in "動詞"
        ]
        return result_list
    
    def parse_word_to_space(self, text: str) -> str:
        result = self.mecab_parse_word.parse(text)
        return result

if __name__ == '__main__':
    m = MecabParser()
    parsed_text = m.parse_text(TEXT)
    result = m.extract_parsedtext_NVA(parsed_text)
    print(result)
