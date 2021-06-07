import bios
import json
import os

from matatika.dataset import Dataset
from matatika import chartjs
from iplotter import ChartJSPlotter

plotter = ChartJSPlotter()

for file in os.listdir("."):
    if file.endswith(".yaml") or file.endswith('.yml'):
        yaml_dict = bios.read(file)

        new_dataset = Dataset.from_dict(yaml_dict)

        my_dataset = chartjs.to_chart(new_dataset, json.loads(new_dataset.raw_data))

        plotter.save(**my_dataset, filename=yaml_dict['title'], keep_html=True)
