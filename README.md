# Text_Generation_RNN
A simple LSTM based Recurrent Neural Network(RNN) to generate text. The RNN was built using Keras library in Python. Pickle and numpy libraries were also used. 

Harry Potter and the Philosopher's Stone written by J. K. Rowling is used as input to the network. 
> https://github.com/formcept/whiteboard/tree/master/nbviewer/notebooks/data/harrypotter

The article on which the code is based on : 
> https://machinelearningmastery.com/text-generation-lstm-recurrent-neural-networks-python-keras/. 
                              
A brief description of each file:

1. harry #1.txt : the input can be copy pasted here. In this case, the entire contents of harry potter book 1 are present here. 
2. harry2.txt : output after running remove_page.py
3. char_sequences.txt : output after running text_preprocessing.py
4. remove_page.py : used for file preprocessing 
5. text_preprocessing.py : text prepocessing and formatting inputs to the network
6. rnn_model_creation.py : creating and training the model
7. rnn_testing : used for testing the model
8. model.h5 : the model file
9. mapping.pkl : pickle file used to save the mapping

> NOTE : This model took 6-7 hrs for 100 epochs on a i3 4th gen @ 1.70 Ghz processor,8gb ram machine. Please use kaggle/ Google colab for faster training.

Approximate accuracy of 62% was obtained.
