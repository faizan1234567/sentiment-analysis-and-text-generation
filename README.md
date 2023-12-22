# Sentiment Analysis & Text Generation

Sentiment analysis on ```Sarcasm dataset``` and text generation on William Shakespere sonnets have been implemened in this repo.
Sentiment analysis is the process of analyzing digital text to determine if the emotional tone of the message is positive, negative, or neutral, however, in our case we are dealing with sarcastic and non sarcastic headlines from the news articles. Today, companies have large volumes of text data like emails, customer support chat transcripts, social media comments, and reviews. Sentiment analysis tools can scan this text to automatically determine the author’s attitude towards a topic. Companies use the insights from sentiment analysis to improve customer service and increase brand reputation. ```[1]```

Text generation is a process where an AI system produces written content, imitating human language patterns and styles. The process involves generating coherent and meaningful text that resembles natural human communication. Text generation has gained significant importance in various fields, including natural language processing, content creation, customer service, and coding assistance. ```[2]```, in this project, I am using ```LSTM``` based model to generate text based on William Shakespere's sonnet dataset.

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


## Acknowledgements
[1]. Amazon Web servies. (1978). What is ... Amazon. https://aws.amazon.com/what-is/sentiment-analysis/ 
[2]. Data camp. (1978). Text generation. Amazon. https://www.datacamp.com/blog/what-is-text-generation 

