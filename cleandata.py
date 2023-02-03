import pandas as pd
import numpy as np
tqp = pd.read_csv('trimmed-data/transientqualitypurity.csv')
v = pd.read_csv('trimmed-data/uncontaminatedvariables.csv')

def cleanColumn(dataset):
    for i in dataset.index:
        if dataset.loc[i,'redshift'] == '-':
            dataset.loc[i,'redshift'] = np.nan
        if dataset.loc[i,'peakabs'] == '-':
            dataset.loc[i,'peakabs'] = np.nan
    for col in ['rise','duration','fade','peakmag','peakabs','redshift']:
        if type(dataset.loc[0,col]) == str:
            dataset[col] = dataset[col].str.replace('<','')
            dataset[col] = dataset[col].str.replace('>','')
            dataset[col] = dataset[col].astype(float,copy=False)

def removeGarbage(dataset):
    garbageIndex1 = dataset[dataset['ZTFID'] == 'ZTF19acardcs'].index
    dataset.drop(garbageIndex1,inplace=True)
    
removeGarbage(tqp)
removeGarbage(v)

cleanColumn(tqp)
cleanColumn(v)

tqp['class'] = np.ones(len(tqp))
v['class'] = np.zeros(len(v))

data = pd.concat([tqp, v], axis=0)

tqp.to_csv('cleaned-data\ctransients.csv')
v.to_csv('cleaned-data\cvariables.csv')
data.to_csv('cleaned-data\data.csv')
