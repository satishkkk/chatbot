
import nltk

text="My name is satish.you are boy and i am girl. we love you"
sent_text = nltk.sent_tokenize(text) # this gives us a list of sentences
print(sent_text)
# now loop over each sentence and tokenize it separately
for sentence in sent_text:
    tokenized_text = nltk.word_tokenize(sentence)
    tagged = nltk.pos_tag(tokenized_text)
    print(tagged)

