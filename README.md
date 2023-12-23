# Sentiment Analysis & Text Generation

![Alt Text](https://github.com/faizan1234567/sentiment_analysis_and_text_generation/blob/main/images/text_gen.gif)

Animation by ```[3]```

Sentiment analysis on ```Sarcasm dataset``` and text generation on William Shakespere sonnets have been implemened in this repo.
Sentiment analysis is the process of analyzing digital text to determine if the emotional tone of the message is positive, negative, or neutral, however, in our case we are dealing with sarcastic and non sarcastic headlines from the news articles. Today, companies have large volumes of text data like emails, customer support chat transcripts, social media comments, and reviews. Sentiment analysis tools can scan this text to automatically determine the author’s attitude towards a topic. Companies use the insights from sentiment analysis to improve customer service and increase brand reputation. ```[1]```

Text generation is a process where an AI system produces written content, imitating human language patterns and styles. The process involves generating coherent and meaningful text that resembles natural human communication. Text generation has gained significant importance in various fields, including natural language processing, content creation, customer service, and coding assistance. ```[2]```, in this project, I am using ```LSTM``` based model to generate text based on William Shakespere's sonnet dataset.

```
sentiment_analysis_and_text_generation 
├── __init__.py  
├── data
│   └── Sonnet.txt  
├── images 
│   └── ...
├── README.md  
├── requirements.txt  
├── sentiment_analysis
│   └── sentiment_analysis.ipynb 
├── text_generation
│   └── text_generation.ipynb
└── weights
    ├── meta.tsv  
    └── vecs.tsv
```

Overall structure of the repository. 

## Sentiment Analysis
The section involves downloading the Sarcasm dataset from the internet, preporcesing, training, inferencing:
### preprocessing
1. Lower casing
2. Removing HTML tags and URLs from the text
3. Stop words removal
4. Lemmization
5. Dataset split
6. Tokenization
7. Sequence Padding

After preprocessing we have set some hyperparameters for training and test, those parameters will influcnece the performance metrics.

<table>
  <tr>
  <th></th>
  <th>General</th>
  <th>Model</th>
  </tr>
  <tr>
  <td>

  </td>
  <td>

| ```Hyperparameters ```        | ```value```  |    
| ----------------------        | -------- |
| Vocabulary size               | 5000     |
| embedding dimension           | 100      |
| maximum sequence length       | 200      |
| truncation type               | post     |
| padding type                  | post     |
| out of vocab token            | oov      |
| Training set size             | 80%      |

              
  </td>
  <td>
    
| ```Hyperparameters ``` | ```value```          |    
| ---------------------- | -----------------    |
| activation             | relu                 |
| learning rate          | adaptive             |
| maximum epochs         | 30                   |
| loss                   | binary cross entropy |
| optimizer              | Adam                 |
| metric                 | Accuracy             |
| Dropout                |   0.3                |
              
   </td>
  </tr>
  <tr>
</table>



![alt text](https://github.com/faizan1234567/sentiment_analysis_and_text_generation/blob/main/images/model_pic_task3.PNG)

Fig 1: LSTM based model for sentiment analysis

## Installation

```bash
 git clone https://github.com/faizan1234567/sentiment_analysis_and_text_generation
 cd sentiment_analysis_and_text_generation
```
Create and activate Anaconda Environment
```bash
conda create -n nlp python=3.9.0
conda activate nlp
```
Now install all the required dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```
Installation done !

## Text Generation
In the text generation step the william shakespere sonnet dataset has been used. 
The following steps covered.
1. Dataset loading
2. Lowercasing
3. Inspecting dataset 
4. Tokenization
5. Padding to have uniform length sequences

![alt text](https://github.com/faizan1234567/sentiment_analysis_and_text_generation/blob/main/images/poemcloud.png)

Following the preprocessing, the model is define and trained with the following hypermeters:

<table>
  <tr>
  <th></th>
  <th>General</th>
  <th>Model</th>
  </tr>
  <tr>
  <td>

  </td>
  <td>

| ```Hyperparameters ```        | ```value```          |    
| ----------------------        | --------             |
| embedding dimension           | total_words + 1      |
| maximum sequence length       | 11                   |
| truncation type               | pre                  |
| padding type                  | pre                  |
| out of vocab token            | oov                  |


              
  </td>
  <td>
    
| ```Hyperparameters ``` | ```value```               |    
| ---------------------- | -----------------         |
| activation             | relu                      |
| maximum epochs         | 150                       |
| loss                   | categorical cross entropy |
| optimizer              | Adam                      |
| Dropout                |   0.2                     |
              
   </td>
  </tr>
  <tr>
</table>


## Acknowledgements
[1]. Amazon Web servies. (1978). What is ... Amazon. https://aws.amazon.com/what-is/sentiment-analysis/ 

[2]. Data camp. (1978). Text generation. Amazon. https://www.datacamp.com/blog/what-is-text-generation 

[3]. C. (2022, January 5). Introduction to Natural Language Processing(NLP) — Part 1. Medium. https://medium.com/@chinmaychetan04/     introduction-to-natural-language-processing-nlp-part-1-2f2dfbc305d6

