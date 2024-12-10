from preprocess import clean_and_map_nepali_text, one_hot_encode_tokens
from tokenizer import Tokenizer
from predict import decode_sequence

def transliterate(text: str) -> str:
    tokenizer = Tokenizer()
    
    # clean the text
    cleaned_text = clean_and_map_nepali_text(text)
    # make a list of text
    tokenized_text = cleaned_text.split(" ")
    # tokenization
    tokenized_devnagari = tokenizer.tokenize_devnagari(tokenized_text)
    # convert in number
    ohe_token = one_hot_encode_tokens(tokenized_devnagari[0])
    # translation
    decoded_sentence = decode_sequence(ohe_token)
    return decoded_sentence
    
if __name__ == "__main__":
    devnagari_text = "यो एउटा उदाहरण वाक्य हो। यसमा १२३४ नम्बर र केही चिन्हहरू छन्।"
    roman_text = []
    for text in devnagari_text.split():
        if any(char.isdigit() for char in text):
            # some refactor need
            roman_text.append(clean_and_map_nepali_text(text))
            continue
        t = transliterate(text)
        roman_text.append(t)
        print(t)
    print(" ".join(roman_text))
        