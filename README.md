# Kanji stroke predictor(in progress)
 A neural netwrok that predicts the stroke count of Kanji

This is a convolutional neural network model that takes pictures of kanji as arrays and outputs the number of strokes required to write the kanji.
This repository includes a saved model(kanjiCNN.h5) which predicted with around 82% accuracy on the test set. However this is misleading as I have trained it on oictures of kanji typed in a specific font. No augmentation of any kind was implemented. Depending on the type of font, the prediction accuracy could fall significantly.

Latest performance:

- 65% accuracy on the test set. 74.9% on a font which the model has not seen.
- 66.6% accuracy on the test set. 77.1% on a font which the model has not seen.
- 72% accuracy on the test set. 79.9% on a font which the model has not seen.
- 77% accuracy on the test set. 85.1% on a font which the model has not seen.
* - Accuracy dropping to ~40% on unseen kanji typed in an unseen font.

To-do list:

- Train on datasets on more than SEVEN different fonts.
- Augment the dataset by transforming the images. Erosion seems to be a good choice. Note that rotating the images could cause the model to get confused as the stroke number changes depending on the direction of writing.
- (Major) Create a better dataset but spilling the kanji and fonts such that the model does not see the same kanji in tow different fonts.

Notes:
- I hit a plateau where the test set accuracy was not going above ~62%. Finally I managed 72% accuracy buy increasing the number of nodes in the final convolutional layer and adding 25% Dropout() after Flatten().
- The latest model named kanjiCNN_77pct.h5 achieves 84.9% accuracy on unseen data. However, while training the validation accuracy fluctuates rather sporadically. I should fix this by first tweaking the Dropout() parameters.