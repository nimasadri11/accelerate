# A fully functioning example script. 

from fastai.vision.all import *
from accelerate import Accelerator
import accelerate.utils as utils # So we can have our own set_seed that works in a multiprocess setup
from accelerate_fastai_integration import *

def get_data():
    path = untar_data(URLs.PETS)/"images"
    dls = ImageDataLoaders.from_name_func(
        path, get_image_files(path), valid_pct=0.2,
        label_func=lambda x: x[0].isupper(), item_tfms=Resize(224)
    )
    return dls

# We define a `train_fn`. This also must be done if you're in a notebook and use the notebook launcher
# Documentation on that is available here: https://huggingface.co/docs/accelerate/launcher
def train_fn():
    "Trains a `vision_learner` on the PETs dataset"
    # This picks up the configuration after "accelerate config" was run on the CLI
    accelerator = Accelerator()
    utils.set_seed(42)
    dls = get_data()
    # We simply build our AcceleratorCallback
    cbs = [AcceleratorCallback(accelerator)]
    learn = vision_learner(dls, resnet34, metrics=error_rate, cbs=cbs)
    # And then train
    learn.fit_one_cycle(3)
    
@call_parse
def main():
    return train_fn()