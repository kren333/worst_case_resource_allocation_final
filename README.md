# Decision-Focused Evaluation of Worst-Case Distribution Shift

## Overview

This repository is the official implementation of Decision-Focused Evaluation of Worst-Case Distribution Shift (UAI 2024), containing code to implement our method and perform experiments. If you find this repository useful or use this code in your research, please cite the following paper:

[TODO add the link to the arxiv]

Note: To run a simplified version of our experiments (5 states, 25 individuals per optimization instance, 10,000 samples per iteration of the Frank-Wolfe algorithm) please switch to the `mini` branch via the following command

```
git checkout origin/mini
```

## Installing Dependencies

<!-- To install requirements, setup a conda environment using the following command: -->
To install requirements, simply run:

```
source install.sh
conda activate SPODR
```

## Experiments

<!-- ### Predictive Model Training -->

To use the provided checkpoints for our trained models, place and unzip them in the proper directories using the following command:

```
./move_models.sh
```

This can also be done manually:

- Move the `binary_final_results_models.zip` into the `binary_final_results` folder and unzip
- Move the `regression_final_results_models.zip` into the `regression_final_results` folder and unzip

To train the models from scratch, comment out `--no_train` in the `binary_experiments.sh` and `regression_experiments.sh` files.

<!-- To replicate our experiments, all trained predictive models must be placed and unzipped in the proper directories. This can either be done by training them directly by commenting out `--no_train` in the `binary_experiments.sh` and `regression_experiments.sh` files, or using the provided zip files in the root directory. To exercise the second option, run the procedure below. Otherwise (training predictive models from scratch), skip this step.

- move the `binary_final_results_models.zip` into the `binary_final_results` folder and unzip
- move the `regression_final_results_models.zip` into the `regression_final_results` folder and unzip

The process of reusing the pretrained predictive models can also be accomplished by running:

```
./move_models.sh
``` -->

To run all experiments, run the following command. The output results will be placed inside folders `_final_results_ci`, `efficiency_experiments`, and `paper_visualizations` under the root directory:

<!-- ### Experiment Running

After the above scripts have been run, the following command will run all experiments and output the results inside the folders `_final_results_ci`, `efficiency_experiments`, and `paper_visualizations` under the root directory: -->

```
./run_all.sh
```

The final figures in the paper (TODO: list figures) should be located within the `_final_results_ci`, `efficiency_experiments`, and `paper_visualizations` folders. This contains visualizations (for each worst-case distribution) of the model predictions and converged weights assigned to individuals within the corresponding optimization instance.


Read below for a more detailed description of each of the subtasks involved in our experiments, should you decide to run experiments one-at-a-time *as opposed* to simply running run_all.sh.

#### Individual Experiments

Once the models have been run, the following commands (which can be run in any order) will run all experiments on the binary prediction tasks (unemployment, income classification) and income regression task (identify worst-case distributions w.r.t. all loss functions, for all predictive models, compile the results, and then compare our method to Pyomo/IPOPT):

```
./binary_experiments.sh
./regression_experiments.sh
```

Once these have successfully run, the following will create our final results with confidence intervals, along with the results of an efficiency-related experiment comparing our method to Pyomo/IPOPT:

```
./final_experiments.sh
```

<!-- The final diagrams seen in the paper should be located within the folders `_final_results_ci`, `efficiency_experiments`, and `paper_visualizations` (this contains visualizations, for each worst-case distribution, of the model predictions and converged weights assigned to individuals within the corresponding optimization instance). -->

