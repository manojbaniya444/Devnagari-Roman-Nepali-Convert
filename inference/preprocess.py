import re
import numpy as np
from vocab import pad_token, roman_stoi, devnagari_stoi, devnagari_itos

nepali_to_english_numbers = {
    "०": "0",
    "१": "1",
    "२": "2",
    "३": "3",
    "४": "4",
    "५": "5",
    "६": "6",
    "७": "7",
    "८": "8",
    "९": "9",
    "।": "."
}

def clean_and_map_nepali_text(text):
    """clean the devnagari text
    Args:
        text (str): Input Nepali text.

    Returns:
        str: Cleaned and processed text.
    """
    # Define the characters to remove (punctuation and special symbols)
    pattern = r"[,!?\"'।।‘’“”():;—-]"
    
    # Remove punctuation
    cleaned_text = re.sub(pattern, "", text)

    # Replace Nepali numbers with English numbers
    for nep_num, eng_num in nepali_to_english_numbers.items():
        cleaned_text = cleaned_text.replace(nep_num, eng_num)
        
    return cleaned_text
    
def one_hot_encode_tokens(tokens: list):
    """One hot encode the token list"""
    MAX_ENCODER_SEQUENCE_LENGTH = 65
    MAX_ENCODER_TOKENS = 19
    ohe = np.zeros((MAX_ENCODER_TOKENS, MAX_ENCODER_SEQUENCE_LENGTH))
    print(ohe.shape)
    for t, tkn in enumerate(tokens):
        ohe[t, tkn] = 1.0
    # for other just encode the position of the pad token
    ohe[t+1:, devnagari_stoi[pad_token]] = 1.0
    ohe = ohe.reshape(1, ohe.shape[0], ohe.shape[1])
    return ohe
    
if __name__ == '__main__':
    # Example usage
       # Example usage
    nepali_text = "०७८ साउन १९ मा एकैदिन चार करोड ९१ लाख ९४ हजार रुपैयाँ सारिएको प्रतिवेदनमा उल्लेख छ । गोर्खा मिडियाका उपाध्यक्ष छविलाल जोशीको घरबाट बरामद भएको हार्ड डिस्कमा सानो पाइला सहकारीबाट पनि रकम सिधै गोर्खा मिडियामा सारिएको फेला परेको हो । प्रहरीका अनुसार सानो पाइला सहकारीका अध्यक्ष अनन्तबाबु राई, सचिव देवेन्द्रबाबु राई, कोषाध्यक्ष कुमार रम्तेल, प्रबन्धक असरफ अली सिद्धिकी, संरक्षक गीतेन्द्रबाबु (जीबी) राईलगायत ११ जना हालसम्म फरार छन् । सहकारीकी पूर्वउपाध्यक्ष नेहा पौडेल गत साउन २१ मा जिल्ला अदालत पर्साबाट न्यायीक परीक्षण हुँदा ठहरेबमोजिम हुने गरी हाललाई एक करोड १० लाख धरौटीमा रिहा भइन् । यसैगरी सहकारीका कर्मचारी राधेचन्द्र यादव पनि ३५ लाख रुपैयाँ धरौटीमा रिहा भएका छन् ।"
    cleaned_text = clean_and_map_nepali_text(nepali_text)
    
    # print(cleaned_text)
    tokens = [0,2]
    ohe = one_hot_encode_tokens(tokens)
    print(ohe)