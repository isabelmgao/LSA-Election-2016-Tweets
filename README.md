# LSA-Election-2016-Tweets
Project for SI 671 Data Mining

Part I

We performed latent semantic analysis on a corpus of 2,582,799 tweets. 
This implementation uses tfidf vectorizer to convert tweets into their tdidf vector representation (reduces problem of common, information-weak words) and SVD to decompose the term-document matrix and reduce dimensionality. 

The outline of our overall process for this project (completed and improved upon in iterations) is as follows: 
1.	Data retrieval, manipulation, and cleaning using Twitter Streaming API
2.	Text summarization over first 100,000 tweets; results a bit jumbled
3.	Extraction and visualization of all unix timestamps to see appropriate time boundaries 
4.	Search for noteworthy events during the Nov. 8th evening corresponding to the time ranges for which we had data 
5.	Split data according to time boundaries determined by part 4
6.	LSA on data separated by each time segment 
7.	LSA on pro-Trump versus pro-Clinton tweets 

Part II

In the second part of the analysis, we tried to find the sentiment associated with four keyword in
this election: “Trump”, “Clinton”, “Election 2016” and “Electoral College”. The analysis was done
over the course of 4 weeks, from 11/06/2016 to 12/03/2016 using 160,000 tweets from social
media website Twitter. We were interested in knowing whether the sentiment with a particular
word was positive, negative or neutral.
