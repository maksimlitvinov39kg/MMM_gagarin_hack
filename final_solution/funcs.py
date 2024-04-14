import torch
from simpletransformers.ner import NERModel
import pandas as pd
import re
data = pd.read_pickle("data_files/my_dict.pkl")

# Проверяем, доступна ли CUDA
use_cuda = torch.cuda.is_available()

model = NERModel(
    model_type='bert',
    model_name='C:/Users/79802/gagrin/hakaton-gagarin-sentiment_interface/datafiles/model/model',
    use_cuda=use_cuda
)
def get_all_from_text(text):
    def get_org_from_text(text):
        prediction, model_output = model.predict([text])
        org_words = []
        for sentence in prediction:
            for word_dict in sentence:
                for word, tag in word_dict.items():
                    if "'ORG'," in tag:  
                        org_words.append(word) 
        def clean_text(text):
            return re.sub(r'[^\w\s]', '', text).lower()
        org_words = [clean_text(word) for word in org_words]
        return org_words
    def get_id_from_text(text):
        org_words = get_org_from_text(text)
        org_keys = {word: set() for word in org_words}

        for word in org_words:
            for key, names in data.items():
                if word in names:
                    org_keys[word].add(key)
        answer =[list(v) for v in org_keys.values()]

        answers = [[int(id_str) for id_str in id_list] for id_list in answer]

        return(answers)
    mas = get_id_from_text(text)
    def get_sent_for_text(text):
        a = text[0]
        return float(3)
    sas =[]
    for m in mas:
        sas.append((m[0],get_sent_for_text(text)))
    return(sas)
    
    