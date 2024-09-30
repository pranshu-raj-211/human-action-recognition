# Human-Action-Recognition

This project was made as part of a course project (Summer Project), in which I classify human activities based on sensor and vision datasets. I'm extending the work on this because it's interesting and allowing me to learn a lot of things that I could not get to earlier.

Primarily, I will be focusing on the Opportunity dataset, a sensor based dataset created in a sensor rich environment.

This is a timeseries classification task, which is usually solved by CNN-LSTM based models and more recently, using transformers and GNNs.

Till date my best performing model has achieved a **test accuracy of 88.6%**, with a test set consisting of the S4 and S5 files for all 4 subjects.

### Tasks Completed:

- [x] Missing Value handling (interpolation and extrapolation)
- [x] Sliding window computation
- [x] Label Encoding
- [x] Basic CNN-LSTM model (overfit)
- [x] Config update for columns
- [x] CNN based model only
- [x] Keras, wandb based template creation - model, metric tracking and report generation
- [x] Missing values handling experimentation

### In Progress:

- Tuning of window size, batch size, convolutional layers, learning rate
- Experimentation on sampling of data
- Implement DropBlock1D
- Logging metrics (modularize metric checking)
- Log visuals
- Modularize dataset creation and splitting
- Track different dataset split as config params, test with different models

### To Do:

- [ ] Regularization to prevent overfit (use Dropblock, kernel regularizers are not great for this alone)
- [ ] Improved missing value imputation (spline, polynomial)
- [ ] Shallow LSTM
- [ ] Feature Engineering
- [ ] Signal Processing (Multiple methods used in series)
- [ ] Edge Detection (Issue #4)
- [ ] Make a tree like visual/tool to show results obtained from combination of different dataset splits, models, hyperparameters etc.
- [ ] Learn and apply Graph convolutional networks (GCNs) to improve performance.
- [ ] Analyze where the model is predicting incorrectly, if it is affected by labeling criteria, window size, find optimal.


## Reproducing results
The repository contains many notebooks that I have used in my experimentation, as well as some utility scripts for config setting and data processing tasks. 

I'll try my best to update these as quickly as I complete another experiment, and subsequently improve on the documentation.

Till then the best way to reproduce the results are to download the dataset, run the individual scripts for various setup tasks, then run the notebook of your choice to reproduce the results obtained by it.
Further scripts will soon be published containing other data processing methods which are a bit more compute intensive. I also intend to publish a whole document detailing different data processing methods, seeing as there are so many used in my experiments. 
