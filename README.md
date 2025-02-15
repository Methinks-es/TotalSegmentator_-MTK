# TotalSegmentator

Tool for segmentation of 104 classes in CT images. It was trained on a wide range of different CT images (different scanners, institutions, protocols,...) and therefore should work well on most images. The training dataset with 1204 subjects can be downloaded from [Zenodo](https://doi.org/10.5281/zenodo.6802613). You can also try the tool online at [totalsegmentator.com](https://totalsegmentator.com/).

![Alt text](resources/imgs/overview_classes.png)

Created by the department of [Research and Analysis at University Hospital Basel](https://www.unispital-basel.ch/ueber-uns/departemente/theragnostik/kliniken/radiologie-und-nuklearmedizin/lehre-und-forschung/forschung/team-forschungskoordination).  
If you use it please cite our paper: [https://arxiv.org/abs/2208.05868](https://arxiv.org/abs/2208.05868).  



### Installation

Install dependencies:  
* Python >= 3.7
* [Pytorch](http://pytorch.org/)
* if you use the option `--preview` you have to install xvfb (`apt-get install xvfb`)
* You should not have any nnU-Net installation in your python environment since TotalSegmentator will install its own custom installation.
* TotalSegmentator was developed for Linux or Mac. To make it work for windows see [this comment](https://github.com/wasserth/TotalSegmentator/issues/10#issuecomment-1234160460).

Install Totalsegmentator
```
pip install TotalSegmentator
```


### Usage
```
TotalSegmentator -i ct.nii.gz -o segmentations --fast --preview
```
> Note: TotalSegmentator only works with a NVidia GPU. If you do not have one you can try our online tool: [www.totalsegmentator.com](https://totalsegmentator.com/)


### Advanced settings
* `--fast`: For faster runtime and less memory requirements use this option. It will run a lower resolution model (3mm instead of 1.5mm). 
* `--preview`: This will generate a 3D rendering of all classes, giving you a quick overview if the segmentation worked and where it failed (see `preview.png` in output directory).
* `--statistics`: This will generate a file `statistics.json` with volume (in mm³) and mean intensity of each class.
* `--radiomics`: This will generate a file `statistics_radiomics.json` with radiomics features of each class. You have to install pyradiomics to use this (`pip install pyradiomics`).


### Run via docker
We also provide a docker container which can be used the following way
```
docker run --gpus 'device=0' --ipc=host -v /absolute/path/to/my/data/directory:/workspace wasserth/totalsegmentator_container:master TotalSegmentator -i /workspace/ct.nii.gz -o /workspace/segmentations
```

### Resource Requirements
Totalsegmentator has the following runtime and memory requirements (using a Nvidia RTX 3090 GPU):  
(1.5mm is the normal model and 3mm is the `--fast` model)

![Alt text](resources/imgs/runtime_table.png)


### Train / validation / test split
The exact split of the dataset can be found in the file `meta.csv` inside of the [dataset](https://doi.org/10.5281/zenodo.6802613). This was used for the validation in our paper.  
The exact numbers of the results for the high resolution model (1.5mm) can be found [here](resources/results_all_classes.json). The paper shown these numbers in the supplementary materials figure 11.


### Retrain model on your own
You have to download the data and then follow the instructions of [nnU-Net](https://github.com/MIC-DKFZ/nnUNet) how to train a nnU-Net. We trained a `3d_fullres` model and the only adaptation to the default training is setting the number of epochs to 4000 and deactivating mirror data augmentation. The adapted trainer can be found [here](https://github.com/wasserth/nnUNet_cust/blob/working_2022_03_18/nnunet/training/network_training/custom_trainers/nnUNetTrainerV2_ep4000_nomirror.py).


### Other commands
If you want to combine some subclasses (e.g. lung lobes) into one binary mask (e.g. entire lung) you can use the following command:
```
totalseg_combine_masks -i totalsegmentator_output_dir -o combined_mask.nii.gz -m lung
```

### Install latest master branch (contains latest bug fixes)
```
pip install git+https://github.com/wasserth/TotalSegmentator.git
```

### Reference 
For more details see this paper [https://arxiv.org/abs/2208.05868](https://arxiv.org/abs/2208.05868).
If you use this tool please cite it as follows
```
Wasserthal J., Meyer M., Breit H., Cyriac J., Yang S., Segeroth M. TotalSegmentator: robust segmentation of 104 anatomical structures in CT images, 2022. URL: https://arxiv.org/abs/2208.05868.  arXiv: 2208.05868
```
Moreover, we would really appreciate if you let us know what you are using this tool for. You can also tell us what classes we should add in future releases. You can do so [here](https://github.com/wasserth/TotalSegmentator/issues/1).