
# VIS-Llama: Automated Visualization of Food Cold Chain Data using Large Language Models

This repository contains the VIS-Llama model, an automatic visualization generation model based on large language models (LLM). VIS-Llama utilizes the Llama2 model optimized by Low-Rank Adaptation (LoRA) technology and is trained on a dataset of 131,910 pairs from a food cold chain corpus to generate high-quality Vega-Lite visualizations.

## Repository Structure

- **data**: This folder contains the dataset used to train the VIS-Llama model. The dataset consists of 131,910 pairs, each comprising a JSON file and the corresponding Vega-Lite syntax file, representing data and its visualization in cold chain processes.

- **code**: This folder contains code resources for implementing the VIS-Llama model. The code includes scripts and resources related to model training, inference, and visualization generation.

## Introduction to VIS-Llama

VIS-Llama is a large language model based on Llama2, optimized using LoRA technology, and focused on automatically generating high-quality Vega-Lite visualizations. The model is trained on a large-scale dataset from the food cold chain corpus, allowing it to automatically generate corresponding Vega-Lite syntax based on input JSON data.

### Key Features

- **LoRA Optimization**: Utilizes Low-Rank Adaptation (LoRA) technology to optimize the Llama2 model for Vega-Lite syntax generation tasks.
- **Large-Scale Training Data**: Trained on a dataset of 131,910 pairs from the food cold chain corpus, ensuring high accuracy and generation capabilities.
- **High-Quality Output**: Capable of generating standard-compliant Vega-Lite syntax, ready for data visualization.

## Quick Start

### 1. Set Up Environment
Before you begin, ensure that your system meets the minimum requirements for training Llama 2. You will need:

CUDA-enabled GPU (for efficient model training)
Python 3.8+ installed
Pytorch with CUDA support installed

### 2. Clone the Repository
Clone the repository containing the training scripts and Llama 2 model

### 3. Download Llama 2 Weights
You will need to download the pre-trained Llama 2 model weights from Hugging Face or Meta AI. You can do this using the Hugging Face Model Hub (make sure you have a Hugging Face account and have agreed to the model’s terms).

### 4. Training Script
Edit and run the following Python script train.sh  to fine-tune the Llama 2 model on your dataset

### 5. Run Training
Run the script on your server:
python train.sh

### Data Files

- The `.source` files contain the JSON data.
- The `.target` files contain the corresponding Vega-Lite syntax.

Each `.source` file is paired with a `.target` file in a one-to-one relationship, ensuring that the JSON data and its corresponding visualization specification are directly linked.

## Dataset Details

- **Total Tuples**: 131,909
- **Data Format**: JSON paired with Vega-Lite syntax
- **Dataset Split**:
  - Training Set: 80%
  - Validation Set: 10%
  - Test Set: 10%

## Privacy Considerations

Given the sensitive nature of the information contained within the food cold chain data, privacy-preserving techniques have been applied to anonymize the dataset. Specifically, all field names have been obfuscated to prevent the identification of any proprietary or sensitive information related to the cold chain processes. This ensures that the data can be shared and utilized for research and development purposes without compromising confidentiality.

## Usage

To use the dataset, simply download the files from the repository and load them into your preferred data processing or machine learning framework. The JSON data can be used directly for various tasks, while the paired Vega-Lite syntax can be employed for visualization-related projects.

Please ensure that you acknowledge the privacy measures taken when using this dataset in any public or academic work.





