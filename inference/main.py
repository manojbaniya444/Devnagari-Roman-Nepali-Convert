from preprocess import clean_and_map_nepali_text, one_hot_encode_tokens
from tokenizer import Tokenizer
from predict import decode_sequence

def transliterate(text: str) -> str:
    tokenizer = Tokenizer()
    
    cleaned_text = clean_and_map_nepali_text(text)
    print(cleaned_text)
    tokenized_text = cleaned_text.split(" ")
    print(tokenized_text)
    tokenized_devnagari = tokenizer.tokenize_devnagari(tokenized_text)
    print(tokenized_devnagari)
    ohe_token = one_hot_encode_tokens(tokenized_devnagari[0])
    print(ohe_token)
    decoded_sentence = decode_sequence(ohe_token)
    return decoded_sentence
    

if __name__ == "__main__":
    devnagari_text = "कार्यालयमा"
    roman_text = transliterate(devnagari_text)
    print(roman_text)