from model import Model
import numpy as np

from tokenizer import devnagari_stoi, devnagari_itos, roman_stoi, roman_itos

MODEL_LOCATION = "../model/model_1.keras"
NUM_DECODER_TOKENS = 30
MAX_OUTPUT_SEQUENCE_LENGTH = 100

def decode_sequence(input_seq):
    """Takes the one hoe encoded input sequence and predict the next token and return the decoded roman nepali text after completing all token prediction"""
    model = Model(MODEL_LOCATION)
    encoder_model = model.encoder()
    decoder_model = model.decoder()
    
    # Encode the input as state vectors.
    states_value = encoder_model.predict(input_seq, verbose=0)

    # Generate empty target sequence of length 1.
    target_seq = np.zeros((1, 1, NUM_DECODER_TOKENS))
    # Populate the first character of target sequence with the start character.
    target_seq[0, 0, roman_stoi["<"]] = 1.0

    # Sampling loop for a batch of sequences
    # (to simplify, here we assume a batch of size 1).
    stop_condition = False
    decoded_sentence = ""
    while not stop_condition:
        output_tokens, h, c = decoder_model.predict(
            [target_seq] + states_value, verbose=0
        )

        # Sample a token
        sampled_token_index = np.argmax(output_tokens[0, -1, :])
        sampled_char = roman_itos[sampled_token_index]
        # decoded_sentence += sampled_char

        # Exit condition: either hit max length
        # or find stop character.
        if sampled_char == ">" or len(decoded_sentence) > MAX_OUTPUT_SEQUENCE_LENGTH:
            stop_condition = True
        else:
          decoded_sentence += sampled_char

        # Update the target sequence (of length 1).
        target_seq = np.zeros((1, 1, NUM_DECODER_TOKENS))
        target_seq[0, 0, sampled_token_index] = 1.0

        # Update states
        states_value = [h, c]
    return decoded_sentence