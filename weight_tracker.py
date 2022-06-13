#!/bin/python

import os
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt

weights_file_path = os.environ['HOME'] + '/.weights'


def parse_weights_file():
    weights_file = get_weights_file()
    lines = weights_file.readlines()
    return extract_date_weight_pairs(lines)


def get_weights_file():
    return open(weights_file_path, "r")


def extract_date_weight_pairs(lines):
    return [split_line_at_space(line) for line in lines]


def split_line_at_space(line):
    return line.rstrip('\n').split(' ')


def sort_by_ascending_dates(date_weight_pairs):
    convert_date_strings_to_date_objects(date_weight_pairs)
    date_weight_pairs.sort(key=lambda pair:pair[0])
    convert_date_objects_to_date_strings(date_weight_pairs)


def convert_date_strings_to_date_objects(date_weight_pairs):
    for pair in date_weight_pairs:
        date_string = pair[0]
        pair[0] = dt.datetime.strptime(date_string, "%Y-%m-%d")


def convert_date_objects_to_date_strings(date_weight_pairs):
    for pair in date_weight_pairs:
        date_object = pair[0]
        pair[0] = dt.datetime.strftime(date_object, "%Y-%m-%d")


def extract_dates(date_weight_pairs):
    return [pair[0] for pair in date_weight_pairs]


def extract_weights(date_weight_pairs):
    return [float(pair[1]) for pair in date_weight_pairs]


def plot_date_weight_series(dates, weights):
    weights = np.array(weights)
    plt.plot(dates, weights)
    apply_plot_decorations(weights.min(), weights.max())
    plt.show()


def apply_plot_decorations(min_weight, max_weight):
    plt.xticks(rotation=45)

    weight_interval = 0.5
    plt.yticks(np.arange(min_weight, max_weight + 1, weight_interval))

    plt.title('Weight Tracker')
    plt.xlabel('Date')
    plt.ylabel('Weight in Kg')


date_weight_pairs = parse_weights_file()
sort_by_ascending_dates(date_weight_pairs)
dates = extract_dates(date_weight_pairs)
weights = extract_weights(date_weight_pairs)
plot_date_weight_series(dates, weights)

