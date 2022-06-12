# MolGAN
Generative adversarial networks for molecules:
![image](https://user-images.githubusercontent.com/51278890/173227301-c8d644d8-77f3-44c0-8ca6-75550335871b.png)

## De-novo generation of molecules using GAN
This repository contains all the code necessary to train a GAN to generate new molecules using keras/tensorflow gpu.

### Dataset
The dataset used to train the model was downloaded from the enamine website: https://enamine.net/compound-libraries/diversity-libraries/dds-50240.
The dataset contains a total of 50,240 molecules.

### SmilesToImage
Use the SmilesToImage function to convert a csv file containing smiles to images with a resolution of 300X300 pixels.
Requires installation of RdKit.

### ImageToSmiles
Use the ImageToSmiles function to make a csv datafrane containing smiles for images of molecules in a folder.
Requires installation of decimer.

ImageToSmiles and SmilesToImage support use of multiple processors for quick conversion.

## Installation
1. Clone/Download the repository.
2. Install dependencies using conda env install -f environment.yml.
 
