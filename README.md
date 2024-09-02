# human-action-recognition

This project was made as part of a course project (Summer Project), in which I classify human activities based on sensor and vision datasets.

Primarily, I will be focusing on the Opportunity dataset, a sensor based dataset created in a sensor rich environment.

This is a timeseries classification task, which is usually solved by CNN-LSTM based models and more recently, using transformers.

Tasks Completed:

- [x] Missing Value handling (interpolation and extrapolation)
- [x] Sliding window computation
- [x] Label Encoding
- [x] Basic CNN-LSTM model (overfit)
- [x] Config update for columns

In Progress:

- Template Creation
- Wandb integration (automated logging)
- Missing values handling experimentation
- Tuning of window size, batch size, convolutional layers, learning rate
- Experimentation on sampling of data

To Do:

- [ ] Regularization to prevent overfit
- [ ] Improved missing value imputation (spline, polynomial)
- [ ] CNN based model only
- [ ] Shallow LSTM
- [ ] Feature Engineering
- [ ] Signal Processing (Butterworth low pass filter)
