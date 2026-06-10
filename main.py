import os
import zipfile
import urllib.request
import torch
from torch.utils.data import DataLoader, Dataset
from torchvision import transforms
from sklearn.model_selection import train_test_split
import numpy as np

# -------------------------------------------------------------------------
# TASK 1.1 & 1.2: Creating Folders & Downloading Sample 2D BraTS Data
# -------------------------------------------------------------------------
print("--- Task 1.1: Setting up folders and downloading data ---")

# Standard project folder structure banana (Syllabus requirement)
os.makedirs('data/raw', exist_ok=True)
os.makedirs('data/processed/tumor', exist_ok=True)
os.makedirs('data/processed/normal', exist_ok=True)

# Ek small pre-processed 2D BraTS sample link (for easy educational use)
# Agar aapke paas full 3D .nii files hain, to unhein nibabel se slice karte hain.
url = "https://github.com" # Placeholder text/data url
# Note: Real scenario mein aap Kaggle se direct Brain Tumor 2D images download karte hain.

print("Folders created successfully.")

