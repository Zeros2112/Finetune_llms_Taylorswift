# MelodyMuse LLM Refinement

This project involves fine-tuning a language model (LLM) on a Taylor Swift dataset and deploying the model for real-time inference. The fine-tuned model can generate responses to questions related to Taylor Swift.

## Table of Contents

- [Project Overview](#project-overview)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Fine-Tuning Process](#fine-tuning-process)
- [Deployment](#deployment)
- [Model Inference](#model-inference)
- [Directory Descriptions](#directory-descriptions)
- [Acknowledgments](#acknowledgments)
- [Author](#author)

## Project Overview

This project aims to leverage language models for generating context-aware responses to questions about Taylor Swift. The fine-tuned model is deployed as a web application to facilitate real-time interactions with users.

## Project Structure

- `finetuning_notebook.ipynb`: Jupyter notebook containing the fine-tuning process for the language model using the Taylor Swift dataset.
- `utilities.py`: Python module containing utility functions, configurations, and logging setup.
- `app.py`: Flask web application for deploying the fine-tuned model.
- `index.html`: HTML template for the web application.
- `taylorswift_docs_3915_steps_410/`: Directory containing the final fine-tuned model files.
- `templates/`: Directory for Flask HTML templates.
- `static/`: Directory for static assets (CSS, JS, etc.) used by the web application.
- `requirements.txt`: File listing Python dependencies for the project.

## Requirements

Ensure you have the following prerequisites installed:

- Python 3.x
- PyTorch
- Transformers library
- Flask
- Other dependencies (check `requirements.txt`)

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Fine-Tuning Process

Certainly! Below is an enhanced version of the README file with additional sections and details. Please adapt it to fit your project specifics.

## Fine-Tuning Process

1. Open the finetuning_notebook.ipynb notebook in Jupyter.

2. Follow the instructions in the notebook to fine-tune the language model using the Taylor Swift dataset.

3. Save the final fine-tuned model in the taylorswift_docs_3915_steps_410/ directory.


## Deployment

1. Run the Flask web application:

```
python app.py
```

2. Open a web browser and go to http://localhost:5000 to interact with the Taylor Swift language model.


## Model Inference

1. Enter a question about Taylor Swift in the provided form on the web page.

2. Click the "Predict" button to see the model-generated answer.


## Directory Descriptions

* taylorswift_docs_3915_steps_410/: Contains the final fine-tuned model files.
  
* templates/: Directory for Flask HTML templates.

* static/: Directory for static assets (CSS, JS, etc.) used by the web application.


## Acknowledgments

The base language model used for fine-tuning is "EleutherAI/pythia-410m."

The Taylor Swift dataset used for fine-tuning is available here.


## Author

Nguyen Gia Hy


