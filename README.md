# ESUN-Money-Laundering-Detection-Competition

## Overview

The "Suspicious Money Laundering Transaction Prediction" project, initiated by E.SUN Bank, aims to address the critical challenge of money laundering in the financial industry. Utilizing artificial intelligence, this project seeks to enhance the identification and reporting of suspicious transactions, improving upon the traditional, labor-intensive review process.

## Introduction

Money laundering poses a significant challenge to the financial sector, facilitating crime by disguising illegal gains. Financial institutions, if not vigilant, can inadvertently become conduits for such activities, damaging their reputation and the broader financial market. Given the evolving nature of financial crimes, leveraging AI to detect suspicious transactions is crucial for maintaining a secure and orderly financial environment.

## Project Description

E.SUN Bank has committed to its corporate social responsibility and the maintenance of financial order by integrating AI technology to recognize suspicious activities more accurately. This competition invites talented individuals to develop algorithms capable of identifying potential money laundering transactions with reduced false positive rates. The bank provides anonymized customer account transactions and Suspicious Activity Report (SAR) results for model training.

## Dataset Description

The provided dataset includes anonymized details of customer account transactions along with the outcomes of SAR filings. Participants are expected to design algorithms using this data to efficiently identify transactions that warrant reporting, with an emphasis on minimizing false positives.

## Methodology

### Preprocessing

- Handling missing values, outliers, and normalization.
- Categorical and numerical data preparation.
- Data transformation techniques such as one-hot encoding.

### Model Structure

- Implementation of LSTM and XGBoost algorithms for transaction classification.
- Exploration of parameterized and non-parameterized models.
- Utilization of embedding layers and neural network structures with imbalanced weight handling.

### Experiments

- Adjusting model weights, layers, and datasets for optimization.
- Emphasis on precision and recall metrics to balance the model performance.

## Getting Started

To contribute to this project or replicate the results, please follow the setup instructions detailed below:

1. **Environment Setup**: Ensure you have Python 3.x installed along with necessary libraries such as scikit-learn, TensorFlow, and XGBoost.
2. **Dataset Preparation**: Download the dataset from the provided link (Note: Add a placeholder or actual link if available).
3. **Model Training**: Execute the training scripts with the command `python train_model.py` (Note: Adjust according to your actual script names).

## Contributing

We welcome contributions from the community. If you wish to contribute, please follow the guidelines outlined in our contribution policy (Note: Link to contribution guidelines if available).

## License

This project is licensed under the MIT License - see the LICENSE file for details (Note: Adjust according to your project's licensing).

## Acknowledgments

- Ideal Lab for their support and guidance.
- Group 11 members: Debby, Kevin, Jerry, Brian, and Louis for their dedication and hard work.

