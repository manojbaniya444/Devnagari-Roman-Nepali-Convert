from vocab import devnagari_stoi, roman_itos, devnagari_itos, roman_stoi, special_tokens

class Tokenizer:
    def __init__(self):
        self.pad_token = roman_stoi[special_tokens[1]]
        self.start_token = roman_stoi[special_tokens[2]]
        self.end_token = roman_stoi[special_tokens[3]]
        self.unk_token = roman_stoi[special_tokens[0]]
        
    def tokenize_devnagari(self, text: list[str]):
        """tokenize the devnagari text into token
        
        args:
            text: str: The list of devnagari text to be tokenized
            
        returns:
            list: The list of tokens
        """
        tokens = []
        for word in text:
            token = []
            for character in word:
                try:
                    token.append(devnagari_stoi[character])
                except KeyError:
                    token.append(self.unk_token)
            tokens.append(token)
        return tokens
    
    def detokenize_devnagari(self, tokens: list[list[int]]):
        """detokenize the roman tokens into text
        
        args:
            tokens: list: The list of tokens to be detokenized
            
        returns:
            str: The detokenized list of text
        """
        texts = []
        for token in tokens:
            text = "".join([devnagari_itos[character] for character in token])
            texts.append(text)
        return texts
    
    def tokenize_roman(self, text: list[str]):
        """tokenize the roman text into token
        
        args:
            text: str: The roman text to be tokenized
            
        returns:
            list: The list of tokens
        """
        tokens = []
        for word in text:
            token = []
            for character in word:
                try:
                    token.append(roman_stoi[character])
                except KeyError:
                    token.append(self.unk_token)
            tokens.append(token)
        return tokens
    
    def detokenize_roman(self, tokens: list[list[int]]):
        """detokenize the roman tokens into text
        
        args:
            tokens: list: The list of tokens to be detokenized
            
        returns:
            str: The detokenized list of text
        """
        texts = []
        for tkn in tokens:
            text = "".join([roman_itos[token] for token in tkn])
            texts.append(text)
        return texts
    
if __name__ == '__main__':
    tokenizer = Tokenizer()
    print("_____ORIGINAL_____")
    text = "सहकारी hello र pसम्पत033 k3j43"
    print(f"Text: {text}\n")
    
    devnagari_tokens = tokenizer.tokenize_devnagari(text.split())
    devnagari_text = tokenizer.detokenize_devnagari(devnagari_tokens)
    print("_____DEVANAGARI_TOKENS_____")
    print(f"{devnagari_tokens}\n")
    
    roman_tokens = tokenizer.tokenize_roman(text.split())
    roman_text = tokenizer.detokenize_roman(roman_tokens)
    print("_____ROMAN_TOKENS_____")
    print(roman_tokens)
    
    unk_ = tokenizer.detokenize_devnagari(devnagari_tokens)
    print("\n_____DETOKENIZED_DEVANAGARI_TOKENS_____")
    print(f"{unk_}")
    
    unk_ = tokenizer.detokenize_roman(roman_tokens)
    print("_____DETOKENIZED_ROMAN_TOKENS_____")
    print(f"\n{unk_}")