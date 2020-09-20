## Abstract:

Natural Language Processing has shown great advancements in recent years and transformer networks have become the most popular techniques to achieve state-of-the-art (SOTA) results. However, attention-based deep learning architectures require abundant amounts of training data, which in fact poses a challenge for their application within a low-resource setting because pre-trained models do not exist for such languages. In this paper, we therefore explore a first attempt to apply these techniques to an extremely low-resource language -- Sumerian cuneiform -- one of the world's oldest written languages attested from at least the beginning of the 3rd millennium BC. Specifically, we introduce the first cross-lingual information extraction pipeline for Sumerian, which includes part-of-speech tagging, named entity recognition and machine translation. We experiment across supervised, semi-supervised and unsupervised learning techniques and achieve SOTA results for all three disciplines. We report on human evaluations by expert Assyriologists, demonstrating the usefulness of our models, and additionally make use of interpretation hooks to make sense of the model encoding and gradients to provide better comparison, explanation and interpretability of our results. Most components of our pipeline can be generalised to any other low-resource language to obtain an interpretable execution of the techniques and to uncover linguistic phenomena in a low-resource setting. To promote further research, we publicly release all our implementations and a novel dataset with domain specific pre-processing.

## Dataset and training subroutine

```
|__ Dataset_MT/ --> Dataset used for Machine Translation Impletatation as described in the paper.

|__ Dataset_POS+NER/ --> The dataset, used for POS Tagging and Named Entity Recognition (NER) Implementation, as described in the paper.

|__ MT_Implementation/ --> Training subroutine for Machine Translation methodologies, as described in the paper.

|__ POS+NER_Implementation/ --> Training subroutine for POS Tagging and Named Entity Recognition (NER) methodologies, as described in the paper.
```