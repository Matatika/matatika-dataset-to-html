import bios
import json
import os
import sys

from pathlib import Path

from matatika.dataset import Dataset
from matatika import chartjs
from iplotter import ChartJSPlotter

plotter = ChartJSPlotter()

os.chdir(os.path.dirname(__file__))

# Look for raw data included in a analzye-{datasouce} directory
if os.path.isdir("../../../rawdata"):
    rawdata = Path("../../../rawdata")
    print("rawdata directory found")
else:
    rawdata = False
    print("rawdata directory not found")

for file in os.listdir("."):
    if file.endswith(".yaml") or file.endswith(".yml"):
        output_dir = os.getenv("MATATIKA_IMPORT_DATASOURCE") or "html_charts"

        yaml_dict = bios.read(file)
        
        new_dataset = Dataset.from_dict(yaml_dict)

        yaml_file_name = Path(file).stem
        
        if rawdata:
            for rawdata_file in os.listdir(rawdata):
                if rawdata_file == file:
                    imported_rawdata_file = bios.read(os.path.join(rawdata, rawdata_file))

                    my_dataset = chartjs.to_chart(new_dataset, json.loads(imported_rawdata_file[yaml_file_name]))
        else:
            try:
                my_dataset = chartjs.to_chart(new_dataset, json.loads(new_dataset.raw_data))
            except:
                print(f"No raw data found for dataset {file}")
                sys.exit(1)

        if not os.path.isdir(output_dir):
            os.mkdir(output_dir)
            if output_dir != "html_charts":
                os.mkdir(output_dir + '/html_charts/')

        if output_dir != "html_charts":
            plotter.save(**my_dataset, filename=output_dir + "/html_charts/" + yaml_file_name.title().replace("-", "_"), keep_html=True)
        else:
            plotter.save(**my_dataset, filename=output_dir + "/" + yaml_file_name.title().replace("-", "_"), keep_html=True)