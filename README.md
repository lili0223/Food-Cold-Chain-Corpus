# Food-Cold-Chain-Corpus

## Overview

This dataset comprises information related to the food cold chain, meticulously constructed to aid in the development and testing of visualization techniques using the Vega-Lite grammar. The dataset consists of 131,909 tuples, each representing a unique pairing between JSON data and its corresponding Vega-Lite syntax. To ensure the dataset is suitable for various machine learning tasks, it has been split into training, validation, and test sets following a 60/20/20 distribution.

### Data Files

- The `.source` files contain the JSON data.
- The `.target` files contain the corresponding Vega-Lite syntax.

Each `.source` file is paired with a `.target` file in a one-to-one relationship, ensuring that the JSON data and its corresponding visualization specification are directly linked.

## Dataset Details

- **Total Tuples**: 131,909
- **Data Format**: JSON paired with Vega-Lite syntax
- **Dataset Split**:
  - Training Set: 60%
  - Validation Set: 20%
  - Test Set: 20%

## Privacy Considerations

Given the sensitive nature of the information contained within the food cold chain data, privacy-preserving techniques have been applied to anonymize the dataset. Specifically, all field names have been obfuscated to prevent the identification of any proprietary or sensitive information related to the cold chain processes. This ensures that the data can be shared and utilized for research and development purposes without compromising confidentiality.

## Usage

To use the dataset, simply download the files from the repository and load them into your preferred data processing or machine learning framework. The JSON data can be used directly for various tasks, while the paired Vega-Lite syntax can be employed for visualization-related projects.

Please ensure that you acknowledge the privacy measures taken when using this dataset in any public or academic work.

## License

This dataset is released under the [Appropriate License], permitting its use for academic and non-commercial purposes. Please refer to the LICENSE file for more details.


