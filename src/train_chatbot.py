import nltk
from nltk.stem import WordNetLemmatizer
import json
import pickle
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers.legacy import SGD


nltk.download("punkt", "data/nltk_models")
nltk.download("wordnet", "data/nltk_models")


lemmatizer = WordNetLemmatizer()


words = []
classes = []
documents = []
ignore_words = ["?", "!"]

# open json file and load the data
data_file = open("data/intents.json").read()
intents = json.loads(data_file)

# Preprocessing the data
for intent in intents["intents"]:
    for pattern in intent["patterns"]:
        # tokenize each word
        w = nltk.word_tokenize(pattern)
        words.extend(w)
        # add documents in the corpus
        documents.append((w, intent["tag"]))
        # add to our classes list
        if intent["tag"] not in classes:
            classes.append(intent["tag"])


words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_words]

pickle.dump(words, open("data/words.pkl", "wb"))
pickle.dump(classes, open("data/classes.pkl", "wb"))


# create our training data
training = []
output_empty = [0] * len(classes)
for doc in documents:
    # initialize our bag of words
    bag = []
    # list of tokenized words for the pattern
    pattern_words = doc[0]
    # lemmatize each word - create base word, in attempt to represent related words
    pattern_words = [lemmatizer.lemmatize(word.lower()) for word in pattern_words]
    # create our bag of words array with 1, if word match found in current pattern
    for w in words:
        bag.append(1) if w in pattern_words else bag.append(0)

    # output is a '0' for each tag and '1' for current tag
    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1
    training.append([bag, output_row])


training = np.array(training, dtype=object)

# create train and test lists. X = patterns, Y = intents
train_x = list(training[:, 0])
train_y = list(training[:, 1])
print("Training data created")


# Create model - 3 layers. First layer 128 neurons, second layer 64 neurons and 3rd output layer contains number of neurons

# equal to number of intents to predict output intent with softmax
model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),), activation="relu"))
model.add(Dropout(0.5))
model.add(Dense(64, activation="relu"))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation="softmax"))

# Compile model
sgd = SGD(learning_rate=0.01)
model.compile(loss="categorical_crossentropy", optimizer=sgd, metrics=["accuracy"])

# fitting the model
hist = model.fit(
    np.array(train_x), np.array(train_y), epochs=500, batch_size=5, verbose=1
)

# saving the model
model.save("data/trained_models/chatbot_model.keras", hist)
print("Model created at path: data/trained_models/chatbot_model.keras")
