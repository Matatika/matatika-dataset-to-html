## matatika-dataset-to-html

Converts a matatika dataset (yaml) file into a html chart.

Currently requires:
- `matatika`
- `matatika-iplotter`
- `bios`

### Current Use

This script is used in out dataset pipelines to create `html` files containing interative versions of our dataset charts.

You can also use this script locally but invoking `make datasets` in any of our `analyze-{datasource-name}` directories. (There is a make file that uses this script, and there is `rawData` for the datasets to use when converted in each of the `analyze-{datasource-name}` repos.)

### How It Works

#### Running the script yourself

This script looks for all `.yml` or `.yaml` files in the current working directory and loops through them.

It attempts to find an variable in a `dataset-rawdata.py` which is included in each of our `analyze-{datasource-name}` repos. If you are converting your own datasets to `.html` files, you will need to provide the `rawData` yourself. (Putting your rawData within the dataset will be the easiest way to achieve this, for more information about our dataset files check out our [dataset documentaion](https://www.matatika.com/docs/data-visualisation/dataset-yaml) or you can see examples datasets with raw data in our [examples repository](https://github.com/Matatika/matatika-examples/tree/master/example_datasets)).

The script will then add the `rawData` to the loaded `.yml` or `.yaml` (or default back to using the `rawData` included in the dataset file), the convert that loaded dataset file into a Matatika dataset object.

The script will then take the newly created dataset object and convert into a `.html` file containing the chart with the datasets filename. 

The output `.html` file will be place in the following location: `./datasets/{datasource-name}/{dataset_filename}.html`

#### `make datasets`

By invoking this script through the make file in any of our analyze-{datasouce-name} repositories, the `rawData` you need to have a `.html` chart file that displays something is already included. In each of the `analyze-{datasource-name}` repos there is a `{datasource-name}-rawdata.py` files that are used for this, and the output `.html` files will be placed inside `bundle/analyze/datasets/datasets/{datasouce-name}/` if you have the `datasource` set an env var, if you dont it will be `bundle/analyze/datasets/datasets/pipeline/`.
