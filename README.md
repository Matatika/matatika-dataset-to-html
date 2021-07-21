## matatika-dataset-to-html

Converts a matatika dataset (yaml) file into a html chart.

Currently requires:
- `matatika==1.9.0.dev5` (The version currently (04/06/21) in dev)
- `matatika-iplotter=1.2.1` (The version currently (04/06/21) in dev)
- `bios` (Pip install most recent)

### Current Use

This script is used in out dataset pipelines to create `html` files containing interative versions of our dataset charts.

As such this script requires the following enviroment variables:

- `DATASOURCE=my_datasource`
In the case of our azure pipelines this is the extractor being used. We set this so the SITs can run generic datasource test using our chosen datasource, so for this script we also use it as the name of the folder to put our converted datasets into.

If this is not set it defaults to the value of `pipeline`

- `NAME_OF_MY_DATASET_YML_FILE_WITHOUT_FILE_EXTENSION={this_datasets_raw_data}
This is how we provide our converted datasets with actual data to display. For more info on the format see: [this example](https://www.matatika.com/docs/getting-started/publish-a-dataset-cli). (Under Dataset File Preperation, scroll to the bottom of the YAML format example).

If this is not set, there needs to be raw data inside you dataset yaml file, or no chart will display in the `html`. (Having no raw data will cause the script to exit with an error).


### How It Works

This script looks for all `.yml` or `.yaml` files in the current working directory and loops through them.

It attempts to find an enviroment variable with the same name as the currently selected `.yml` or `.yaml` file and will add that variables value to the `rawData` field in the dataset object being created. (The chart will only display something if `rawData` has been passed in!)

Using the newly created dataset object, created using the selected `.yml` or `.yaml` file and enviroment variable for `rawData` if applicable, it will be converted into a `.html` file containing the chart with the same name as the datasets title. 

The output `.html` file will be place in the following location: current working directory/datasets/{DATASOURCE}/{dataset_title}.html