# weight-tracker
This repository contains a simple script which displays a list of dates and
weights as a graph.

## Usage
The script looks for a file called `.weights` in the user's home directory. This
file contains a list of weights and the dates of when the corresponding weight
was measured. The order of the entries does not matter, the script sorts the
entries based on their dates ascending.

The syntax is as follows:

```
2022-06-13 88.0
2022-06-06 89.6
2022-05-30 88.2
2022-05-23 89.7
2022-05-16 89.8
2022-05-09 91.0
```

## Dependencies
This script requires the following dependencies:
- Python 3 (https://www.python.org)
- Numpy (https://numpy.org)
- Matplotlib (https://matplotlib.org)

