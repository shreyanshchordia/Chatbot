# Chatbot

The following repository demonstrates building a chatting bot using Tensorflow Framework.   
This project uses the ChatterbotEnglish Dataset, from Kaggle and tunes an Encoder Decoder Model on the entire Dataset.

## Bits and Bytes of the Repository
1. From the `\Data` you can download Raw Data to start off from the beggining, you can download Structured Data to save time, or you can even Download Completely pre-processed Model Feedable Pre-Processed Data.

2. `\DataPrepUtils` folder has a set of functions that have been used for structuring the Data. Can be used for multi purposes on editing.

3. `\LoadAndRun` folder contains PY files, that load the trained models and then can reply to the user on the console in real time. After downloading the the folder files, all you need to do is to execute `run.py` if you have tensorflow pre installed in your python environment.

4. `DataPreparation.ipynb` notebook demonstrates, how to structure data for ChatterbotEnglish Dataset.

5. `EncoderDecoderModel.ipynb` notebook demonstrates:   

    a. Processing data for making it feedable in a Sequence Model.
    
    b. Training a Multi Layer Bi Directional Encoder Decoder Model.
    
    c. Using trained Encoder Model and Decoder Model to predict replies in real time.
    

6. `TextDataAugmentation.py` is a PY file, that can be used for Data Augmentation for a Text Dataset.

7. `Vocabulary.py` has the Vocabulary Class that is used for adding words to vocabulary, trimming the vocabulary size, generating Vocabulary Mapping Dictionaries and for converting sentences to number sequences.

## Bi-LSTM Encoder Decoder Model 

### Training :-

<img align='center' src='https://github.com/shreyanshchordia/Chatbot/blob/master/img/Model.jpg?raw=true'></img>


### Encoder Model :-

<p align = "center">
<img src='https://github.com/shreyanshchordia/Chatbot/blob/master/img/Encoder.jpg?raw=true'></img></p>

### Decoder Model :-

<p align = 'center'>
<img src='https://github.com/shreyanshchordia/Chatbot/blob/master/img/Decoder.jpg?raw=true'></img></p>

### Inference (Deployable Model) :-

<p align = 'center'>
<img src='https://github.com/shreyanshchordia/Chatbot/blob/master/img/Inference.jpg?raw=true'></img></p>
