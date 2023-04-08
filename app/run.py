import json
import plotly
import pandas as pd

from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

from flask import Flask
from flask import render_template, request, jsonify
from plotly.graph_objs import Bar
import joblib
from sqlalchemy import create_engine


app = Flask(__name__)

def tokenize(text):
    tokens = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()

    clean_tokens = []
    for tok in tokens:
        clean_tok = lemmatizer.lemmatize(tok).lower().strip()
        clean_tokens.append(clean_tok)

    return clean_tokens

# load data
engine = create_engine('sqlite:///../data/Disaster_Response.db')
df = pd.read_sql_table('Disaster_Response', engine)

# load model
model = joblib.load("../models/classifier.pkl")


# index webpage displays cool visuals and receives user input text for model
@app.route('/')
@app.route('/index')
def index():
    
    # extract data needed for visuals
    # TODO: Below is an example - modify to extract data for your own visuals
    genre_counts = df.groupby('genre').count()['message']
    genre_names = list(genre_counts.index)
    
    # Top 10 category distribution Direct
    direct_categories = df.loc[df['genre'] == 'direct', df.columns[4:]].sum().sort_values(ascending=False)
    top_category_direct_count = direct_categories[:10]
    top_category_direct_names = list(top_category_direct_count.index)

    # Top 10 category distribution News
    news_categories = df.loc[df['genre'] == 'news', df.columns[4:]].sum().sort_values(ascending=False)
    top_category_news_count = news_categories[:10]
    top_category_news_names = list(top_category_news_count.index)

    # create visuals
    # TODO: Below is an example - modify to create your own visuals
    graphs = [
        # GRAPH 1 - genre distribution
        {
            'data': [
                Bar(
                    x=genre_names,
                    y=genre_counts
                )
            ],

            'layout': {
                'title': 'Distribution of Message Genres',
                'yaxis': {
                    'title': "Count"
                },
                'xaxis': {
                    'title': "Genre"
                }
            }
        },
        # GRAPH 2 - Top 10 category distribution Direct
        {
            'data': [
                Bar(
                    x=top_category_direct_names,
                    y=top_category_direct_count
                )
            ],

            'layout': {
                'barmode': 'stack',
                'title': 'Top 10 Categories in Direct',
                'yaxis': {
                    'title': "Count"
                },
                'xaxis': {
                    'title': "Category",
                    'tickangle': 35,
                    'categoryorder':'total descending'
                }
            }
        },
        # GRAPH 3 - Top 10 category distribution News
        {
            'data': [
                Bar(
                    x=top_category_news_names,
                    y=top_category_news_count
                )
            ],

            'layout': {
                'barmode': 'stack',
                'title': 'Top 10 Categories in News',
                'yaxis': {
                    'title': "Count"
                },
                'xaxis': {
                    'title': "Category",
                    'tickangle': 35,
                    'categoryorder':'total descending'
                }
            }
        }
    ]
    
    # encode plotly graphs in JSON
    ids = ["graph-{}".format(i) for i, _ in enumerate(graphs)]
    graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)
    
    # render web page with plotly graphs
    return render_template('master.html', ids=ids, graphJSON=graphJSON)


# web page that handles user query and displays model results
@app.route('/go')
def go():
    # save user input in query
    query = request.args.get('query', '') 

    # use model to predict classification for query
    classification_labels = model.predict([query])[0]
    classification_results = dict(zip(df.columns[4:], classification_labels))

    # This will render the go.html Please see that file. 
    return render_template(
        'go.html',
        query=query,
        classification_result=classification_results
    )


def main():
    app.run(host='0.0.0.0', port=3000, debug=True)


if __name__ == '__main__':
    main()
