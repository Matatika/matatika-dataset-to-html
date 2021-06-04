## matatika-dataset-to-html

Converts a matatika dataset (yaml) file into a html chart.

Currently requires:
- `matatika==1.9.0.dev5` (The version currently (04/06/21) in dev)
- `matatika-iplotter=1.2.1` (The version currently (04/06/21) in dev)
- `bios` (Pip install most recent)


### WIP

Currently the script finds all yaml files in the same directory as the matatika_dataset_to_html.py, and tries to convert them into html canvases.

The output html chart will scale to the size of the window it is in, and at a 2:1 Height:Width ratio.