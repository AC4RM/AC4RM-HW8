from homework import *
from pathlib import Path
from typing import Generator
import sklearn_extra
import urllib.request
import sqlite3
import pandas as pd


def test_python():
    urllib.request.urlretrieve('https://raw.githubusercontent.com/AC4RM/AC4RM-dataset/main/homework/example.txt',
                               'example.txt')

    text_generator = search('lorem', 'example.txt')

    assert isinstance(text_generator, Generator)
    assert len(list(text_generator)) == 2

    Path('data.db').unlink(missing_ok=True)


def test_sql():
    urllib.request.urlretrieve('https://github.com/AC4RM/AC4RM-dataset/blob/main/sql/data.db?raw=true', 'data.db')

    con = sqlite3.connect('data.db')
    con.execute(sql_query_1)
    con.execute(sql_query_2)
    con.commit()

    customer_df = pd.read_sql_query('SELECT * FROM customers', con)
    order_df = pd.read_sql_query('SELECT * FROM orders', con)

    assert max(customer_df.query('birth_date <= "1990-01-01"')['points']) == 3725
    assert min(customer_df.query('birth_date <= "1990-01-01"')['points']) == 507
    assert order_df.query('comments == "Gold Customer"').shape[0] == 4

    Path('data.db').unlink(missing_ok=True)


def test_model():
    model = train_model()

    assert isinstance(model, sklearn_extra.cluster._k_medoids.KMedoids)
    assert np.array_equal(model.cluster_centers_, np.array([[6.5, 3., 5.2, 2.], [5.7, 2.8, 4.1, 1.3], [5., 3.4, 1.5, 0.2]]))


def test_regex():
    number_1 = extract_number('Today is July 4h')
    number_2 = extract_number('Yesterday was July 3rd')

    assert number_1 == '4'
    assert number_2 == '3'


def test_monte_carlo():
    results = []
    np.random.seed(42)
    for i in range(50):
        result = general_bettor_quick(10000, 100, 20)
        results.append(result)

    assert len(list(filter(lambda x: x < 10000, results))) == 22
    assert max(results) == 11000
