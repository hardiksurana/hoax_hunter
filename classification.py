from sklearn.datasets import load_files
from sklearn.cross_validation import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn import metrics

bunch = load_files('Topics')
X_train, X_test, y_train, y_test = train_test_split(bunch.data, bunch.target, test_size=0.05)
count_vect = CountVectorizer()

X_train_counts = count_vect.fit_transform(X_train)
vectorizer = TfidfVectorizer(sublinear_tf=True,max_df=0.5, stop_words='english')
X_train_counts = vectorizer.fit_transform(X_train)
clf = MultinomialNB(alpha=0.01).fit(X_train_counts, y_train)

X_new_counts = vectorizer.transform(X_test)
l = clf.predict(X_new_counts)

print(accuracy_score(y_test, l))

# use custom input
custom = vectorizer.transform("narendra modi is PM of india")
l = clf.predict(custom)
print(l)
