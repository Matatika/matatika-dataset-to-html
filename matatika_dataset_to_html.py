import bios
import json
import os
import sys

from pathlib import Path

from matatika.dataset import Dataset
from matatika import chartjs
from iplotter import ChartJSPlotter

plotter = ChartJSPlotter()

for file in os.listdir("."):
    if file.endswith(".yaml") or file.endswith('.yml'):
        yaml_dict = bios.read(file)
        
        new_dataset = Dataset.from_dict(yaml_dict)

        #Try to get env var of raw data
        try:
            yaml_file_name = Path(file).stem.upper()
        
            my_dataset = chartjs.to_chart(new_dataset, json.loads(os.getenv(yaml_file_name)))
        
        except:
            #Try to get raw data from the dataset yml
            try:
                my_dataset = chartjs.to_chart(new_dataset, json.loads(new_dataset.raw_data))
            except:
                print('Error getting raw data from either the enviroment variable or the dataset yaml file itself.')
                sys.exit(1)
        
        output_dir = os.getenv("datasource") or "pipeline"

        os.mkdir('datasets')

        os.mkdir('datasets/' + output_dir)

        plotter.save(**my_dataset, filename='datasets/' + output_dir + '/' + yaml_dict['title'], keep_html=True)
