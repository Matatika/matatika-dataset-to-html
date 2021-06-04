import bios
import json
import argparse
import glob

from matatika.dataset import Dataset
from matatika import chartjs
from iplotter import ChartJSPlotter

plotter = ChartJSPlotter()

for file in glob.glob("*.yaml"):
    yaml_dict = bios.read(file)

    new_dataset = Dataset.from_dict(yaml_dict)

    my_dataset = chartjs.to_chart(new_dataset, json.loads(new_dataset.raw_data))

    plotter.save(**my_dataset, filename=yaml_dict['title'], keep_html=True)
