# Decision-Focused Evaluation of Worst-Case Distribution Shift

## Overview

This is the official code for our paper, "Decision-Focused Evaluation of Worst-Case Distribution Shift", which was accepted into UAI 2024.

[TODO add the link to the arxiv]

## Installing Dependencies

To create a Conda environment with all dependencies installed, simply run

```
source install.sh
```

The environment SPODR should now be activated; if this is not the case run

```
conda activate SPODR
```

to activate the environment.

## Replicating Experiments

### Predictive Model Training

To replicate our experiments, all trained predictive models must be placed and unzipped in the proper directories. This can either be done by training them directly by commenting out "--no_train" in the binary_experiments.sh and regression_experiments.sh files, or using the provided zip files in the root directory. To exercise the second option, run the command below. Otherwise (training predictive models from scratch), skip this step.

- move the "binary_final_results_models.zip" into the "binary_final_results" folder and unzip
- move the "regression_final_results_models.zip" into the "regression_final_results" folder and unzip

The process of reusing the pretrained predictive models can also be accomplished by running:

```
./move_models.sh
```

### Experiment Running

After the above scripts have been run, the following command will run all experiments and output the results inside the folders "_final_results_ci", "efficiency_experiments", and "paper_visualizations" under the root directory:

```
./run_all.sh
```

Read below for a more detailed description of each of the subtasks involved in our experiments, should you decide to run experiments one-at-a-time *as opposed* to simply running run_all.sh.

#### Replicating Individual Experiments

Once the models have been run, the following commands (which can be run in any order) will run all experiments on the binary prediction tasks (unemployment, income classification) and income regression task (identify worst-case distributions w.r.t. all loss functions, for all predictive models, compile the results, and then compare our method to Pyomo/IPOPT):

```
./binary_experiments.sh
./regression_experiments.sh
```

Once these have successfully run, the following will create our final results with confidence intervals, along with the results of an efficiency-related experiment comparing our method to Pyomo/IPOPT:

```
./final_experiments.sh
```

The final diagrams seen in the paper should be located within the folders "_final_results_ci", "efficiency_experiments", and "paper_visualizations" (this contains visualizations, for each worst-case distribution, of the model predictions and converged weights assigned to individuals within the corresponding optimization instance).

