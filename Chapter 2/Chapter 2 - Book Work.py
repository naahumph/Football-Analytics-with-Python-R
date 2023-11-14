## Chapter 2
## Stable vs Unstable Quarterback Stats

# import libraries
import pandas as pd
import numpy as np
import nfl_data_py as nfl

# obtaining and filtering data
seasons = range(2016, 2022 + 1) # add 1 because python starts counting at 0
pbp_py = nfl.import_pbp_data(seasons)

# filtering for just passing plays
pbp_py_p = \
    pbp_py\
    .query("play_type == 'pass' & air_yards.notnull()")\
    .reset_index()

