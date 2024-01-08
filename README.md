# ASL-to-Alphabet-Translator

## Overview

This Python project is an American Sign Language (ASL) to alphabet letters translator. The application utilizes a Convolutional Neural Network (CNN) implemented in a Jupyter notebook for accurate sign language recognition. Additionally, a spell checker is integrated to correct any potential mistakes made by the model during translation.

## Features

- **ASL to Alphabet Translation:** The core functionality of the project is to translate American Sign Language gestures into corresponding alphabet letters.

- **Convolutional Neural Network:** The ASL recognition model is built using a Convolutional Neural Network, providing robust and accurate predictions.

- **Jupyter Notebook Implementation:** The CNN model is developed and trained in a Jupyter notebook, allowing for easy experimentation and understanding of the model's architecture.

- **Spell Checker Integration:** To enhance the accuracy of translations, a spell checker is incorporated to correct any potential mistakes made by the model.

## Installation and Usage

1. **Clone the repository:**

   ```bash
   git clone https://github.com/channoun/ASL.git
   cd ASL
2. **Run the following commands:** (alternatively you can use the provided shell file)
   ```bash
   pip install -r requirements.txt
   python cam.py
Note that a trained version of the neural network has also been provided, so no additional training is necessary

## License

This project is licensed under the MIT License

## Acknowledgements

The dataset for training the network is sourced from Kaggle.

The network architecture is inspired from Pathan, R.K., Biswas, M., Yasmin, S. et al. Sign language recognition using the fusion of image and hand landmarks through multi-headed convolutional neural network. Sci Rep 13, 16975 (2023). https://doi.org/10.1038/s41598-023-43852-x. The application, however, uses a more simplistic version of the model for initial roll-out purposes. Despite this, it has been able to achieve a 94.95% training accuracy and very impressive testing results. Full model to be released in future commits.

The spell checker is powered by pyspellchecker.
   
