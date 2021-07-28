import bios
import json
import os
import sys

from pathlib import Path

from matatika.dataset import Dataset
from matatika import chartjs
from iplotter import ChartJSPlotter

plotter = ChartJSPlotter()

try:
    raw_data_file = bios.read("dataset_rawdata.yaml")
except:
    print("No dataset_rawdata.yaml file found")

# Set the cwd to this python files location after trying to get raw_data above.
# This is here to allow the makefile with a different cwd to work.
os.chdir(os.path.dirname(__file__))

for file in os.listdir("."):
    if file.endswith(".yaml") or file.endswith('.yml'):
        output_dir = os.getenv("MATATIKA_IMPORT_DATASOURCE") or "pipeline"

        yaml_dict = bios.read(file)
        
        new_dataset = Dataset.from_dict(yaml_dict)

        yaml_file_name = Path(file).stem

        if raw_data_file[yaml_file_name]:
            my_dataset = chartjs.to_chart(new_dataset, json.loads(raw_data_file[yaml_file_name]))
        else:
            try:
                my_dataset = chartjs.to_chart(new_dataset, json.loads(new_dataset.raw_data))
            except:
                print(f"No raw data found for dataset {file}")
                sys.exit(1)
        
        output_dir = os.getenv("datasource") or "pipeline"

        os.mkdir(output_dir)

        plotter.save(**my_dataset, filename=output_dir + '/' + yaml_dict['title'], keep_html=True)