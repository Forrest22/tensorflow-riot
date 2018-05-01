import pandas as pd
import tensorflow as tf

# TRAIN_URL = "http://download.tensorflow.org/data/iris_training.csv"
# TEST_URL = "http://download.tensorflow.org/data/iris_test.csv"
# TRAIN_URL = "C:\\Users\\doddfm14\\Documents\\CS 391\\Riot-API\\json data\\matches800_adv.csv"
# TEST_URL = "C:\\Users\\doddfm14\\Documents\\CS 391\\Riot-API\\json data\\matches200_adv.csv"
TRAIN_URL = "/home/doddfm14/tensorflow-riot/json-data/matches800_adv.csv"
TEST_URL = "/home/doddfm14/tensorflow-riot/json-data/matches200_adv.csv"

# CSV_COLUMN_NAMES = ["firstBlood","firstTower","firstInhibitor","firstDragon","towerKills","inhibitorKills","baronKills","dragonKills","win"]
CSV_COLUMN_NAMES = ["p1champid", "p1masterypts", "p2champid", "p2masterypts", "p3champid", "p3masterypts", "p4champid", "p4masterypts", "p5champid", "p5masterypts", "result"]
RESULT = ['Fail','Win']

def maybe_download():
    # train_path = tf.keras.utils.get_file(TRAIN_URL.split('/')[-1], TRAIN_URL)
    # test_path = tf.keras.utils.get_file(TEST_URL.split('/')[-1], TEST_URL)
    train_path = TRAIN_URL
    test_path = TEST_URL

    return train_path, test_path

def load_data(y_name='result'):
    """Returns the iris dataset as (train_x, train_y), (test_x, test_y)."""
    train_path, test_path = maybe_download()

    train = pd.read_csv(train_path, names=CSV_COLUMN_NAMES, header=0)
    train_x, train_y = train, train.pop(y_name)

    test = pd.read_csv(test_path, names=CSV_COLUMN_NAMES, header=0)
    test_x, test_y = test, test.pop(y_name)

    return (train_x, train_y), (test_x, test_y)


def train_input_fn(features, labels, batch_size):
    """An input function for training"""
    # Convert the inputs to a Dataset.
    dataset = tf.data.Dataset.from_tensor_slices((dict(features), labels))

    # Shuffle, repeat, and batch the examples.
    dataset = dataset.shuffle(1000).repeat().batch(batch_size)

    # Return the dataset.
    print(dataset)
    return dataset


def eval_input_fn(features, labels, batch_size):
    """An input function for evaluation or prediction"""
    features=dict(features)
    if labels is None:
        # No labels, use only features.
        inputs = features
    else:
        inputs = (features, labels)

    # Convert the inputs to a Dataset.
    dataset = tf.data.Dataset.from_tensor_slices(inputs)

    # Batch the examples
    assert batch_size is not None, "batch_size must not be None"
    dataset = dataset.batch(batch_size)

    # Return the dataset.
    return dataset


# The remainder of this file contains a simple example of a csv parser,
#     implemented using a the `Dataset` class.

# `tf.parse_csv` sets the types of the outputs to match the examples given in
#     the `record_defaults` argument.
CSV_TYPES = [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]]

def _parse_line(line):
    # Decode the line into its fields
    fields = tf.decode_csv(line, record_defaults=CSV_TYPES)

    # Pack the result into a dictionary
    features = dict(zip(CSV_COLUMN_NAMES, fields))

    # Separate the label from the features
    label = features.pop('result')

    #'''
    features.pop('p1champid')
    features.pop('p2champid')
    features.pop('p3champid')
    features.pop('p4champid')
    features.pop('p5champid')
    #'''
    # print(label)
    # print(features)

    return features, label


def csv_input_fn(csv_path, batch_size):
    # Create a dataset containing the text lines.
    dataset = tf.data.TextLineDataset(csv_path).skip(1)

    # Parse each line.
    dataset = dataset.map(_parse_line)

    # Shuffle, repeat, and batch the examples.
    dataset = dataset.shuffle(1000).repeat().batch(batch_size)

    # Return the dataset.
    return dataset
