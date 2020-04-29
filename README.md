Reddit_Flair_Detector
======================

A Reddit Flair Detector web application to detect flairs of India subreddit posts using Machine Learning algorithms. The application can be found live at [Reddit Flair Detector](https://flair--detector.herokuapp.com/).

About
=======================

This repository illustrates the process of scraping reddit posts from the subreddit r/india, text preprocessing/cleaning of data, building a classifier to classify the posts into 7 different flairs and deploying the suitable machine learning model as a web application.

Dependencies
=======================

The following dependencies can be found in requirements.txt:
1. beautifulsoup4
2. bs4
3. Flask
4. gunicorn
5. html5lib
6. json5
7. nltk
8. numpy
9. numpydoc
10. pandas
11. path
12. pathlib2
13. praw
14. prawcore
15. py
16. requests
17. scikit-learn
18. scipy
19. unicodecsv
20. win-unicode-console

Approach
======================

Going through various literatures available for text processing and suitable machine learning algorithms for text classification, I based my approach using various machine learning models like Naive-Bayes, Linear SVM, Random Forest, Multi-Layer Perceptron and Logistic Regression for text classification with code snippets. I have obtained test accuracies on various scenarios which can be found in the next section.

**Approach taken for the task:**
1. Collected various India subreddit posts using Pushshift Reddit API.
2. The data includes *flair, score, url, title, time-created*.
3. Title was considered for the detection task.
4. Then the following ML Algorithms are applied on the database.
  * Naive-Byes
  * Linear Support Vector Machine
  * Logistic Regression
  * Random Forest
  * MLP
5. Training and Testing on the dataset showed the **Random Forest showed the best testing accuracy of 92.617%** when title is used as the feature.
6. The best model is saved and is used for prediction of the flair from the URL of the post.
7. The model was deployed on a web application build on **Flask** to predict the flair of the url from India subreddit.
8. Algorithm with best accuracy was **Random Forest**, but since models with >500 MB cannot be deployed to Heroku, so model based on **Linear SVM** is deployed on Heroku.

**Results from algorithms used, using title as the feature**
| Algorithm | Accuracy |
|:---------|:--------:|
| Naive Bayes	| 73.154% |
| Linear SVM	| 81.879% |
| Logistic Regression	| 89.932% |
| Random Forest	| 92.617% |
| MLP | 87.248% |

References
=======================

1. [Using Pushshift Reddit API](https://github.com/pushshift/api)
2. [Converting json to Python](https://www.w3schools.com/python/python_json.asp)
3. [Scrapping Reddit data with Python](https://www.storybench.org/how-to-scrape-reddit-with-python/)
4. [Making Graphs with Python](https://www.w3resource.com/graphics/matplotlib/piechart/matplotlib-piechart-exercise-4.php)
5. [Multi-Class Text Classification Model Comparison and Selection](https://towardsdatascience.com/multi-class-text-classification-model-comparison-and-selection-5eb066197568)
6. [Preprocessing of text](https://mlwhiz.com/blog/2019/01/17/deeplearning_nlp_preprocess/)
7. [Cleaning and preprocessing of text](https://towardsdatascience.com/nlp-text-preprocessing-a-practical-guide-and-template-d80874676e79)
8. [Deploying ML model using flask](https://towardsdatascience.com/how-to-easily-deploy-machine-learning-models-using-flask-b95af8fe34d4)
9. [Deploying a Python Flask app on Heroku](https://medium.com/the-andela-way/deploying-a-python-flask-app-to-heroku-41250bda27d0)
