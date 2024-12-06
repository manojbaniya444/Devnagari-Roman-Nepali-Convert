## Devnagari Nepali to Roman Nepali Transliteration

This repo contains training code for converting devnagari nepali word to roman nepali word using character level sequence to sequence model.

## Experiment:

Training different model with different architecture, parameters and data.

> Dataset used to train is from HuggingFace and can be found with Roman Nepali Transliteration name.

## Model 0: Simple Encoder Decoder Character Level

Trained on `5 percent` of dataset which is `10k` translation with simple `Encoder Decoder` Architecture and was trained for `100 Epochs` with batch size of `32 batch size`.

**[Model 0 Training Note](./training/02_mini_train.ipynb)**

The model is trained as character level prediction.

![Model 0 Architecture](./images/model_0.png)

#### Model `Training and Validation` `loss and accuracy.`

- The model training well steadily over epoch and is fitting the training data well
- The validation accuracy pleateaus around epoch 30 and after it fluctuates slightly, indicating the model is `overfitting` the training data.
- Here simply I got `overfitting` result but the model is learning properly on the training data.

<div style="display: flex; justify-content: space-around;">
    <img src="./images/model_0_plot0.png" alt="Model 1 Architecture" style="width: 45%;">
    <img src="./images/model_0plot.png" alt="Model 2 Architecture" style="width: 45%;">
</div>
