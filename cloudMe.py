import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import matplotlib


def remove_punctuation(doc):
    return [token for token in doc if not token.is_punct]


def lemmatize(tokens):
    return [token.lemma_ for token in tokens]


def remove_stopwords(tokens):
    return [word for word in tokens if word not in STOP_WORDS]


def generate_wordcloud(text):
    wordcloud = WordCloud(width=800, height=500, background_color="black",
                          random_state=1, collocations=False, colormap="Dark2").generate(text)

    plt.figure(figsize=(10, 10), facecolor="k")
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.show()
    wordcloud.to_file("cloudMe2.png")


def process_text(input_text):
    nlp = spacy.load('en_core_web_sm')
    spacy_doc = nlp(input_text.strip("\n").lower())

    tokens_without_punct = remove_punctuation(spacy_doc)
    lemmatized_text = lemmatize(tokens_without_punct)
    text_without_stopwords = remove_stopwords(lemmatized_text)
    processed_text = " ".join(text_without_stopwords)

    return processed_text


def generate_wordcloud_from_input(input_text):
    processed_text = process_text(input_text)
    generate_wordcloud(processed_text)


if __name__ == "__main__":
    sample_text = input("Enter the text: ")
    generate_wordcloud_from_input(sample_text)
