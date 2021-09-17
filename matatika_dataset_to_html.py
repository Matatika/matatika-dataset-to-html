import bios
import json
import os
import sys
import argparse

from pathlib import Path

from matatika.dataset import Dataset
from matatika import chartjs
from iplotter import ChartJSPlotter

plotter = ChartJSPlotter()

my_parser = argparse.ArgumentParser()
my_parser.add_argument("--datasets", help="path to datasets dir", required=True)
my_parser.add_argument("--rawdata", help="path to rawdata dir")

args = my_parser.parse_args()

path_to_datasets = Path(args.datasets)

try:
    path_to_rawdata = Path(args.rawdata)
except:
    path_to_rawdata = False

def save_converted_chart(my_dataset_chart, yaml_file_name):
    yaml_file_name = yaml_file_name.title().replace("-", "_")
    plotter.save(**my_dataset_chart, filename=str(output_path.joinpath(yaml_file_name)), keep_html=True)

for file in path_to_datasets.iterdir():
    if file.name.endswith(".yaml") or file.name.endswith(".yml"):

        output_path = path_to_datasets

        output_path = output_path.joinpath("html_charts")

        if not output_path.exists():
            output_path.mkdir(parents=True)
        
        yaml_dict = bios.read(str(file.absolute()))
        
        new_dataset = Dataset.from_dict(yaml_dict)

        yaml_file_name = Path(file).stem

        my_dataset_chart = None
        
        if path_to_rawdata:
            if path_to_rawdata.is_dir():
                for rawdata_file in path_to_rawdata.iterdir():
                    if rawdata_file.name == file.name:
                        imported_rawdata_file = bios.read(str(path_to_rawdata.joinpath(rawdata_file.name).absolute()))

                        my_dataset_chart = chartjs.to_chart(new_dataset, json.loads(imported_rawdata_file[yaml_file_name]))

        else:
            try:
                my_dataset_chart = chartjs.to_chart(new_dataset, json.loads(new_dataset.raw_data))
            except:
                print(f"No raw data found for dataset {file}")

        try:
            save_converted_chart(my_dataset_chart, yaml_file_name)
        except:
                print(f"Did not convert {file}")
    