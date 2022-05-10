# Integration of Accelerate into fastai

This contains an nbdev-style subrepository with a somewhat completed fastai X huggingface integration.

To run the example script, first make sure accelerate is installed either via the dev version or pypi:
```bash
pip install accelerate
```
```bash
pip install git+https://github.com/huggingface/accelerate
```

Then clone this repository, and install the integration with:
```bash
cd accelerate/examples/fastai_integration
pip install -e .
```

## Run Example Script
To run the example script, first run `accelerate config` in bash.

Then to launch you can perform any of the options shown in the [README](https://github.com/huggingface/accelerate/tree/fastai-integration/examples) here, or just make your life easy and do:
```bash
accelerate launch fastai_example.py
```
This script will then train on the PETs dataset, and is less than 40 lines of code!
