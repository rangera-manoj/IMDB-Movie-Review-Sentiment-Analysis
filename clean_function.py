def clean_text(texts):

  import re
  import nltk
  from nltk.corpus import stopwords
  nltk.download('stopwords')
  from nltk.stem import SnowballStemmer

  stop_words = stopwords.words('english')
  stemmer = SnowballStemmer('english') 

  clean_review = []

  for i in range(len(texts)):

      review = re.sub('[^a-zA-Z]', ' ', texts.iloc[i])

      review = review.lower().split()

      review = [stemmer.stem(word) for word in review if not word in stop_words]

      review = " ". join(review)

      clean_review.append(review)

  return clean_review  