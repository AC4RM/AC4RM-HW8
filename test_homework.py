from homework import *
from pathlib import Path
import urllib.request
import sqlite3
import pandas as pd
import sklearn
import re


def test_python():

    assert calculator(20, 2, 'mul') == 40
    assert calculator(5, 0, 'div') == 'Invalid Operation'


def test_sql():
    urllib.request.urlretrieve('https://github.com/AC4RM/AC4RM-dataset/blob/main/sql/data.db?raw=true', 'data.db')

    con = sqlite3.connect('data.db')

    customer_df = pd.read_sql_query(sql_query, con)

    assert customer_df.shape == (1, 4)
    assert round(customer_df['total_sales'][0], 2) == 157.92
    assert customer_df['last_name'][0] == 'Brushfield'

    Path('data.db').unlink(missing_ok=True)


def test_model():
    model, predictions = train_model()

    assert isinstance(model, sklearn.tree._classes.DecisionTreeClassifier)
    assert sum(predictions) == 75


def test_regex():
    assert re.search(regex_pattern, 'abc123@gmail.com') is not None
    assert re.search(regex_pattern, 'abc123@gmail.net') is not None
    assert re.search(regex_pattern, 'abc123@gmail.xyz') is None
