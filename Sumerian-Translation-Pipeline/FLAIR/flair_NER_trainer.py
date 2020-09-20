from flair.data import Corpus
from flair.datasets import ColumnCorpus
from flair.embeddings import TokenEmbeddings, WordEmbeddings, StackedEmbeddings, FlairEmbeddings, CharacterEmbeddings
from torch.optim.adam import Adam
from typing import List


# define columns
columns = {0: 'text', 1: 'ner'}

# this is the folder in which train, test and dev files reside
data_folder = 'FLAIR/NER_corpus'

# init a corpus using column format, data folder and the names of the train, dev and test files
corpus: Corpus = ColumnCorpus(data_folder, columns,
                              train_file='train.txt',
                              test_file='test.txt',
                              dev_file='dev.txt')
                              
print(len(corpus.train))                              
print(corpus.train[0].to_tagged_string('ner'))

# tag to predict
tag_type = 'ner'
# make tag dictionary from the corpus
tag_dictionary = corpus.make_tag_dictionary(tag_type=tag_type)

print(tag_dictionary)

# initialize embeddings
embedding_types: List[TokenEmbeddings] = [

    # GloVe embeddings
    WordEmbeddings('FLAIR/word2vec50'),
    CharacterEmbeddings(),

    # contextual string embeddings, forward
    #FlairEmbeddings('resources/taggers/language_model/best-lm.pt'),
]

embeddings: StackedEmbeddings = StackedEmbeddings(embeddings=embedding_types)
    

# 5. initialize sequence tagger
from flair.models import SequenceTagger

tagger: SequenceTagger = SequenceTagger(hidden_size=64,
                                        embeddings=embeddings,
                                        tag_dictionary=tag_dictionary,
                                        tag_type=tag_type,
                                        use_crf=True)

# 6. initialize trainer
from flair.trainers import ModelTrainer

trainer: ModelTrainer = ModelTrainer(tagger, corpus, optimizer=Adam)

# 7. start training
trainer.train('FLAIR/resources/taggers/flairNer2',
              learning_rate=0.1,
              mini_batch_size=32,
              max_epochs=50)


