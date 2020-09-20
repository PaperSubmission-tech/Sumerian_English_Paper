<p align="center">
  <img src="https://github.com/cdli-gh/Unsupervised-NMT-for-Sumerian-English/blob/master/repoSum0.jpg" />
</p>

<p align="center">
  <b> Figure-1: </b> Shows a Cuneiform inscription, extracted from actual tablets.<br>
  <i> Sumerian: </i> pisan-dub-ba sza3-bi su-ga sag-nig2-gur11-ra u3 zi-ga lu2-kal-la i3-gal2 ... <br>
  <i> English: </i> Basket-of-tablets: therefroms, restitutions, debits, and credits, of Lukalla are here; ...
</p>

# Sumerian-English Neural Machine Translation
As a part of the MTAAC project at CDLI, we aim to build an end-to-end NMT Pipeline while making use of the extensive monolingual Sumerian Data. 

Previous models that have been used to carry out English<-->Sumerian Translation have only made use of the available parallel corpora. Presently we have only about 50K extracted sentences for both languages in the parallel corpora, whereas around 1.47M sentences in the Sumerian monolingual corpus. 

This huge amount of monolingual data can be used to improve the NMT system by combining it with techniques like Back Translation, Tranfer Learning and Dual Learning which have proved specially useful for Low-Resource languages like Sumerian which have a limited amount of parallel data. Moreover, we also look to implement models like XLM and MASS for the same.

<details>
<summary> Requirements </summary> 
- Python 3.5.2 or higher <br>
- NumPy <br>
- Pandas <br>
- PyTorch <br>
- Torch Text <br>
- OpenNMT-py <br>
- fairseq <br>

</details>


## Repository Structure

```
|__ translation/ --> all translation models used for Sumerian-English Translation 
        |__ transformer/ --> Supervised NMT using Vanilla Transformer
                |__ runTransformerSumEn.sh --> to perform training
                |__ README.md --> lists down all checkpoints and steps to run training and inference.
        |__ backtranslation/ --> fairseq usgae for Back Translation using Vanilla Transformers
        |__ backtranslation-onmt/ --> OpenNMT usage for Back Translation using Vanilla Transformers
                |__ backtranslateONMT.py --> to translate all Sumerian Text in a given shard using weights from the previous iteration
                |__ stack.py --> To stack the backtranslated sentences to the parallel corpora for training
                |__ runTransformerSumEn.sh --> To retrain the transformer model using the updated parallel data from the last step
                |__ README.md --> lists down all checkpoints and steps to run training and inference.
        |__ XLM/ --> Unsupervised and Semi-Supervised NMT using Cross-Lingual Langual Model Pretraining
                |__ XLM/ --> directory containing all model, data preperation and inference scripts
                |__ models.txt --> lists the possible commands and parameter combinations for XLM training and inference.
                |__ README.md --> lists down all checkpoints and steps to run training and inference.
        |__ MASS-unmt/ --> Unsupervised NMT using Masked Sequence to Sequence Pretraining
                |__ data_prep.sh --> to prepare and process data for training 
                |__ pre_training.sh --> to carry out pre training using Unsupervised Objectives
                |__ fine_tuning.sh --> to carry out fine tuning using parallel data
                |__ translate.sh --> to carry out inference using the specified checkpoints
                |__ README.md --> lists down all checkpoints and steps to run training and inference.
        |__ MASS-snmt/ --> Unsupervised NMT using Masked Sequence to Sequence Pretraining 
                |__ data_prep.sh --> to prepare and process data for training 
                |__ pre_training.sh --> to carry out pre training using Unsupervised Objectives
                |__ fine_tuning.sh --> to carry out fine tuning using parallel data
                |__ translate.sh --> to carry out inference using the specified checkpoints
                |__ README.md --> lists down all checkpoints and steps to run training and inference.

|__ dataset/ --> All Sumerian Language related textual dataset by CDLI
        |__ README.md --> Gives detailed description of the dataset and the different sub-folders.
        |__ dataToUse/ --> Contains all the parallel data divided among traing, test and dev sets, in 4 different categories
                |__ UrIIICompSents/ --> UrIII Admin Data with complete sentence translations
                |__ AllCompSents/ --> All kinds of Sumerian Data with complete sentence translations
                |__ UrIIILineByLine/ --> UrIII Admin Data with line by line translations
                |__ AllLineByLIne/ --> All kinds of Sumerian Dtaa with line by line translations
        |__ cleaned/ --> Contains data after cleaning using the helper scripts, including the monolingual data. Divided in the same 4 categories.
        |__ original/ --> Contains all of the data before cleaning
        |__ oldFormat/ --> Contains data from last year, for comparison
        
```

<p align="center">
  <b> Refer to the README of each folder and sub-folder to throughly know them and to reproduce the <a href="https://github.com/cdli-gh/Semi-Supervised-NMT-for-Sumerian-English/tree/master/translation">translation</a> models </b>
</p>

## Results
<p align="center">
  <img src="https://github.com/cdli-gh/Unsupervised-NMT-for-Sumerian-English/blob/master/nmt_results.png" width="60%"/>
</p>

<p align="center">
  <b> Table-1: </b> Sumerian-English Machine Translation.<br>All numeric values other than those in Human Evaluation represent the BLEU Score.<br>
</p>

## Visualisations and Interpretations 
<p align="center">
  <img src="https://github.com/cdli-gh/Unsupervised-NMT-for-Sumerian-English/blob/master/highlights.png" width="100%"/>
</p>

<p align="center">
  <b> Figure-2:</b> Selected output tokens for Sumerian Input text of <i>”sze-ba geme2 usz-bar kiszib3 ur-dasznan ugula”</i>, which translates to <i>”barley rations of the female weavers under seal of UrAnan the foreman”</i> <br> 
</p>
<!-- <p style="color: #00FF00">Green</p> and <p style="color: #FF0000">Red</p> fonts represent the correct and wrong output, respectively, while the <p style="background-color: #00FF00">Green</p> and <p style="background-color: #FF0000">Red</p> highlights represent positive and negative attributions, respectively. -->

<p align="center">
  <img src="https://github.com/cdli-gh/Semi-Supervised-NMT-for-Sumerian-English/blob/master/heatmaps.png" width="90%"/>
</p>

<p align="center">
  <b> Figure-3:</b> Feature Ablation and attention Attributions, respectively,<br>for a span of input and output text through the Data Augmented XLM</i> <br> 
</p>


## Tasks:

- [x] Preparing the parallel and monolingual texts for final usage. Using methods like BPE and BBPE to tokenize the text.
- [x] Implementing the Vanilla Transformer for Sumerian to English as well as English to Sumerian
- [x] Back Translation using Sumerian Monolingual data
- [x] Transfer Learning from pre-trained models of other languages
- [x] XLM for Unsupervised NMT.
- [x] XLM for Semi-Supervised NMT
- [x] MASS for Unsupervised NMT.
- [x] MASS for Semi-Supervised NMT.
- [x] Pre-training using Augmented Data
- [x] Interpretation of the NMT Models

...
