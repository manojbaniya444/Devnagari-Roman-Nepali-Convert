import keras

class Model:
    def __init__(self, model: str):
        self.model = keras.models.load_model(model)
        self.LATENT_DIM = 256

    def encoder(self):
        """Return the encoder model"""
        encoder_inputs = self.model.input[0]  # input_1
        encoder_outputs, state_h_enc, state_c_enc = self.model.layers[2].output  # lstm_1
        encoder_states = [state_h_enc, state_c_enc]
        
        encoder_model = keras.Model(encoder_inputs, encoder_states)
        
        return encoder_model
        
    def decoder(self):
        """Return the decoder model"""
        decoder_inputs = self.model.input[1]
        decoder_state_input_h = keras.Input(shape=(self.LATENT_DIM,), name="decoder_state_1")
        decoder_state_input_c = keras.Input(shape=(self.LATENT_DIM,), name="decoder_state_2")
        
        decoder_states_inputs = [decoder_state_input_h, decoder_state_input_c]
        
        decoder_lstm = self.model.layers[3]
        
        decoder_outputs, state_h_dec, state_c_dec = decoder_lstm(
            decoder_inputs, initial_state=decoder_states_inputs)
        
        decoder_states = [state_h_dec, state_c_dec]
        
        decoder_dense = self.model.layers[4]
        
        decoder_outputs = decoder_dense(decoder_outputs)
        
        decoder_model = keras.Model(
        [decoder_inputs] + decoder_states_inputs, [decoder_outputs] + decoder_states
        )
        
        return decoder_model
    
if __name__ == "__main__":
    model = Model("../model/model_1.keras")
    encoder_model = model.encoder()
    decoder_model = model.decoder()
    decoder_model = None
    print(encoder_model, decoder_model)
    print("Model loaded successfully")