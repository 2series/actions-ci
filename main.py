# Script: training model and saving model

# Import Library
from train import fit

# Train Model
model, history = fit()

# Save Trained Model in Keras Format
model.save("model.keras")