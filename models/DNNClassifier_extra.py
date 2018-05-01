#  Copyright 2016 The TensorFlow Authors. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
"""An Example of a DNNClassifier for the Iris dataset."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse

import tensorflow as tf

import json_data_advanced

parser = argparse.ArgumentParser()
parser.add_argument('--batch_size', default=100, type=int, help='batch size')
parser.add_argument('--train_steps', default=1000, type=int,
                    help='number of training steps')

def main(argv):
    args = parser.parse_args(argv[1:])

    sess = tf.get_default_session()

    # Fetch the data
    (train_x, train_y), (test_x, test_y) = json_data_advanced.load_data()

    # Feature columns describe how to use the input.
    my_feature_columns = []
    for key in train_x.keys():
        my_feature_columns.append(tf.feature_column.numeric_column(key=key))

    # Build 2 hidden layer DNN with 10, 10 units respectively.
    classifier = tf.estimator.DNNClassifier(
        feature_columns=my_feature_columns,
        # Two hidden layers of 10 nodes each.
        hidden_units=[10, 10],
        # The model must choose between 2 classes.
        n_classes=2)

    # Train the Model.
    classifier.train(
        input_fn=lambda: json_data_advanced.train_input_fn(train_x, train_y,
                                                  args.batch_size),
        steps=args.train_steps)

    # Evaluate the model.
    eval_result = classifier.evaluate(
        input_fn=lambda: json_data_advanced.eval_input_fn(test_x, test_y,
                                                 args.batch_size))

    print('\nTest set accuracy: {accuracy:0.3f}\n'.format(**eval_result))

    # Generate predictions from the model
    expected = ["Fail", "Win"]
    predict_x = {
        'p1champid': [0,0],
        'p1masterypts': [1000,200000],
        'p2champid': [0,0],
        'p2masterypts': [1000,200000],
        'p3champid': [0,0],
        'p3masterypts': [1000,200000],
        'p4champid': [0,0],
        'p4masterypts': [1000,200000],
        'p5champid': [0,0],
        'p5masterypts': [1000,200000],
    }

    predictions = classifier.predict(
        input_fn=lambda: json_data_advanced.eval_input_fn(predict_x,
                                                 labels=None,
                                                 batch_size=args.batch_size))

    template = ('\nPrediction is "{}" ({:.1f}%), expected "{}"')

    for pred_dict, expec in zip(predictions, expected):
	# print(pred_dict)
        class_id = pred_dict['class_ids'][0]
        probability = pred_dict['probabilities'][class_id]

        print(template.format(json_data_advanced.RESULT[class_id],
                              100 * probability, expec))
    '''
    super(classifier, self).exportsaved_model(
    '''
    tf.estimator.exportsaved_model(
        "", lambda: json_data_advanced.train_input_fn(train_x, train_y,
        args.batch_size,steps=args.train_steps))

if __name__ == '__main__':
    #tf.logging.set_verbosity(tf.logging.INFO)
    tf.app.run(main)
    
