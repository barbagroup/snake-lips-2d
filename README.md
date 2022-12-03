# Two-dimensional study of the lateral lips of a gliding snake using PetIBM on Azure

[![BSD-3 clause](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)

The motion of the flying snake *Chrysopelea paradisi* is characterized by active deformations of the whole body to generate aerodynamic forces necessary for gliding, stabilization, and maneuvering.
One active deformation is the expansion of the rib cage to produce a concave ventral surface with the formation of a pair of ventrally-oriented lips.
Here, we aim to identify the role of the lips and quantify their effect on the aerodynamic performance of the glider.
Our approach is to modify the anatomically accurate cross-section by removing one or both lips and measure the relative change in aerodynamic forces.

![geometries](data/figures/modified_sections_aoa35.png)

**Figure:** Original and modified geometries of the snake section (oriented at a $35$-degree angle of attack).}{From left to right: (1) original profile, (2) profile with the front lip only, (3) profile with the back lip only, and (4) profile with no lips.

The original geometry of the body cross-section of the snake *Chrysopelea paradisi* is available on [FigShare](https://doi.org/10.6084/m9.figshare.705877.v1):

> Krishnan, Anush; J. Socha, John; P. Vlachos, Pavlos; Barba, Lorena A. (2013): Body cross-section of the flying snake Chrysopelea paradisi. figshare. Dataset. https://doi.org/10.6084/m9.figshare.705877.v1

We used our in-house software, [PetIBM](https://github.com/barbagroup/PetIBM) (version `0.5.1`), to compute the flow past the original and modified cross-sections of the gliding snake at Reynolds number $1000$ and $2000$ over a range of angles of attack.
All simulations ran inside Docker containers on Microsoft Azure.
We used [Batch Shipyard](https://github.com/Azure/batch-shipyard) (version `3.9.1`) and [Azure CLI](https://github.com/Azure/azure-cli) (version `2.3.1`) to deploy resources on Azure and submit containerized jobs to Azure Batch.

## Create a conda environment for pre- and post-processing of the simulations

```shell
conda env create --name=py37-snakelips-2d --file=environment.yml
conda activate py37-snakelips-2d
```

## Example of running a simulation on Azure Batch

Navigate to a simulation directory, e.g., `runs/Re2000/both_lips/2k35`:

```shell
SNAKELIPS_DIR=$(pwd)
cd runs/Re2000/both_lips/2k35
```

Copy and update the template `credentials.yaml` with your credentials:

```shell
cp ${SNAKELIPS_DIR}/misc/template-credentials.yaml config_shipyard/credentials.yaml
# Edit the file with your credentials
```

Create the geometry of the snake section:

```shell
python scripts/create_body.py
```

Create a directory in your Azure Storage fileshare to save the output of the simulation:

```shell
az storage directory create --name snake2d/Re2000/both_lips/2k35 --account-name <your-account-name> --share-name fileshare
```

Upload input files to Azure Storage:

```shell
az storage file upload-batch --source . --destination fileshare/snake2d/Re2000/both_lips/2k35 --account-name <your-account-name>
```

Deploy resources (1 dedicated Ubuntu-based NC12 instance) on Azure and submit the job with Batch Shipyard:

```shell
export SHIPYARD_CONFIGDIR=config_shipyard
shipyard pool add
shipyard jobs add
```

Once the job has completed, delete the compute resources and download the numerical solution output from Azure Storage:

```shell
shipyard pool del
mkdir output
az storage file download-batch --source fileshare/snake2d/Re2000/both_lips/2k35 --destination output --account-name <your-account-name>
```

## Results: mean force coefficients

|  |  |
|:-:|:-:|
| ![cl_re1000](runs/Re1000/figures/avg_lift_coefficients_vs_aoa.png) | ![cl_re2000](runs/Re2000/figures/avg_lift_coefficients_vs_aoa.png) |
| ![cd_re1000](runs/Re1000/figures/avg_drag_coefficients_vs_aoa.png) | ![cd_re2000](runs/Re2000/figures/avg_drag_coefficients_vs_aoa.png) |

**Figure:** Time-averaged lift (top) and drag (bottom) coefficients at Reynolds numbers $1000$ and $2000$ versus the angle of attack on all four sections. All averages are computed between $50$ and $80$ non-dimensional time units of flow simulation.

|  |  |
|:-:|:-:|
| ![ld_re1000](runs/Re1000/figures/avg_lift_drag_ratio_vs_aoa.png) | ![ld_re2000](runs/Re2000/figures/avg_lift_drag_ratio_vs_aoa.png) |

**Figure:** Time-averaged lift-to-drag ratio at Reynolds numbers $1000$ and $2000$ versus the angle of attack on all four sections. All averages are computed between $50$ and $80$ non-dimensional time units of flow simulation.

## Reproducibility packages

* Olivier Mesnard, & Lorena A. Barba. (2022). Effect of the lips on the gliding performance of the Chrysopelea paradisi snake with 2D PetIBM on Azure (repro-packs). [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4732946.svg)](https://doi.org/10.5281/zenodo.7394758)

To reproduce the figures, download the Zenodo archive (4.8 GB), create a conda environment, and execute the `misc/process_all.py` script located in the `snake-lips-2d-repropacks` folder.

```shell
cd snake-lips-2d-repropacks
conda env create --name=py37-snakelips-2d --file=environment.yml
conda activate py37-snakelips-2d
python misc/process_all.py
```
