import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer 
from sklearn.decomposition import TruncatedSVD
#thank you Mike Bernico for the tutorial 

def lsa(tweet_list):
	stopset = set(stopwords.words('english'))
	vectorizer = TfidfVectorizer(stop_words = stopset, use_idf=True, ngram_range = (1,3))
	X = vectorizer.fit_transform(tweet_list)

	lsa = TruncatedSVD(n_components = 10, n_iter = 100)
	lsa.fit(X)
	terms = vectorizer.get_feature_names()

	# sys.exit()
	for i, comp in enumerate(lsa.components_):
		termsIncomp = zip(terms, comp)
		sortedTerms = sorted(termsIncomp, key=lambda x:x[1], reverse=True) [:10]
		print "Concept %d:" %i
		for term in sortedTerms:
			print term[0]
		print " "