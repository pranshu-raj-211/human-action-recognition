# human-action-recognition

This project was made as part of a course project (Summer Project), in which I classify human activities based on sensor and vision datasets. I'm extending the work on this because it's interesting and allowing me to learn a lot of things that I could not get to earlier.

Primarily, I will be focusing on the Opportunity dataset, a sensor based dataset created in a sensor rich environment.

This is a timeseries classification task, which is usually solved by CNN-LSTM based models and more recently, using transformers.

Tasks Completed:

- [x] Missing Value handling (interpolation and extrapolation)
- [x] Sliding window computation
- [x] Label Encoding
- [x] Basic CNN-LSTM model (overfit)
- [x] Config update for columns
- [x] CNN based model only 

In Progress:

- Template Creation
- Wandb integration (automated logging)
- Missing values handling experimentation
- Tuning of window size, batch size, convolutional layers, learning rate
- Experimentation on sampling of data
- Implement DropBlock1D
- Logging metrics (modularize metric checking)
- Log visuals
- Modularize dataset creation and splitting
- Track different dataset split as config params, test with different models

To Do:

- [ ] Regularization to prevent overfit
- [ ] Improved missing value imputation (spline, polynomial)
- [ ] Shallow LSTM
- [ ] Feature Engineering
- [ ] Signal Processing (Butterworth low pass filter)
- [ ] Edge Detection (Issue #4)
- [ ] Make a tree like visual/tool to show results obtained from combination of different dataset splits, models, hyperparameters etc.
