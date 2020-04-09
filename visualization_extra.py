import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import json
import os

#visualization for the audio analysis

try:
    dir = os.path.dirname(__file__)
    full_path = os.path.join(dir,"data.json")
    in_file = open(full_path, 'r')
    data = in_file.read()
    lst_of_dictionary = json.loads(data)
    in_file.close()
except:
    print("Problem reading the input file")
    lst_of_dictionary = {}

import matplotlib
import matplotlib.pyplot as plt
import numpy as np


fig.savefig("audio_analysis.png")
plt.show()

# # save the figure

# plt.show()




