import string
import pandas as pd
from os import path 

def check_file(filename: str):
    if path.exists(filename):
        print('''
                 ----------        
        |        The file exists !      |
                ----------   
                                   ''') 
    else:
        print('The file does not exist !')

def lower_case(line):
    '''this fuction transform all the text unifomely in lowercase'''
    return line.lower()

def remove_punct(line):
    '''the followinf function remove the punctuation from the text'''
    punct = str.maketrans(""""',?!-.:;[]()`*I_""", "                 ")
    return line.translate(punct)

def split_words(line):
    '''the following function returns a list of single words of the text splittend on the space '''
    return line.split(' ')

def words_(words):
    '''this function join the words one after another'''
    return "\n".join(words)

def word_count(file):
    '''count the occurrencies of each word'''
    diz = dict()
    for word in file:
        if word not in diz:
            diz[word] = 1
        else:
            diz[word]+=1
    return diz

def length(diz):
    '''count the length of each word'''
    dictim= dict()
    for key in diz.keys():
        dictim[key] = len(key)
    return dictim

def different_letters(dictionary):
    '''count the different letters of each word'''
    diz = dict()
    for word in dictionary.keys():
        diz[word] = len(set(word))
    return diz

def number_of_vowels(dictionary):
    '''count vowels in each word'''
    vowels = 'aeiou'
    diz = dict()
    for word in dictionary.keys():
        conta =0
        for achar in word:
            if achar in vowels:
                conta+=1
                diz[word] = conta
            else:
                diz[word] = 0
    return diz

def number_consonants(dictionary):
    '''count the consonants '''
    diz = dict()
    vowels = 'aeiou'
    for word in dictionary.keys():
        conta = 0
        for achar in word:
            if achar not in vowels:
                conta+=1
                diz[word] = conta
            else:
                diz[word] = 0
    return diz

def clean_dictionary(diz):
    '''this function clean each word from the newline character'''
    diz = {k.replace('\n',''): v for k,v in diz.items()}
    return diz 

def remove(diz):
    del(diz[''])
    return diz 
def dataframe(filename: str):
    '''this function loads the text file as a dataframe'''
    df = pd.read_csv(filename)
    return df

def media(dataframe):
    '''this function calculates the mean '''
    diz = {}
    for el in dataframe.columns[1:]:
        diz[el] = round(sum(dataframe[el])/len(dataframe[el]), 2)
    return diz

def standard_deviation(dataframe):
    '''this function calculates the std'''
    diz={}
    for el in dataframe.columns[1:]:
        diz[el]=round(std(dataframe[el]),2)
    return diz
  
def plot(dt):
    x = dt['length']
    y = dt['count']
    plt.plot(x,y, marker = '.',linestyle='' )
    plt.title('Words Plot')
    plt.xlabel('length')
    plt.ylabel('count')
    plt.show()

def log_plot(dt):
    x = dt['length']
    y = dt['count']
    plt.plot(x,y, marker = '.', linestyle='')
    plt.yscale('log')
    plt.title('Words Plot')
    plt.xlabel('length')
    plt.ylabel('log-countcount')
    plt.show()

def main():
    check_file('alice_in_wonderland.txt')
    with open('alice_in_wonderland.txt', 'r') as infile, open('alice_correct.txt', 'w') as outfile:
        for line in infile:
            clear_line = lower_case(line)
            clear_line = remove_punct(clear_line)
            words = split_words(clear_line)
            cleaned_words = words_(words)
            outfile.write(cleaned_words)
    with open('alice_correct.txt', 'r') as infile, open('report.txt', 'a') as outfile:
        wc = word_count(infile)
        w = clean_dictionary(wc)
        w = remove(w)
        print(f'words counts:\n {w}\n')
        le = length(w)

        #print(f'words lengths:\n {le}\n')
        dif = different_letters(w)
        #print(f'number different letters:\n {dif}\n')
        vo = number_of_vowels(w)
        #print(f'number of vowels:\n {vo}\n')
        co = number_consonants(w)
        #print(f'number of consonants: {co}')
        
        df = pd.DataFrame(list(w.items()), columns = ['word', 'count'])
        df1 = pd.DataFrame(list(le.items()), columns = ['word', 'length'])
        df2 = pd.DataFrame(list(dif.items()), columns = ['word', 'different letters'])
        df3 = pd.DataFrame(list(vo.items()), columns = ['word', 'vowels'])
        df4 = pd.DataFrame(list(co.items()), columns = ['word', 'consonants'])

        df_ = pd.merge(df, df1, on = 'word', validate = 'one_to_one')
        df = pd.merge(df_, df2, on = 'word', validate = 'one_to_one')
        df = pd.merge(df, df3, on = 'word', validate = 'one_to_one')
        df_ = pd.merge(df, df4, on = 'word', validate = 'one_to_one')

        print(df_)

df_.to_csv('report.txt', sep=',', header=True, index = False)
df = dataframe('report.txt')
m =media(df)
print(f'media di ogni colonna del file: {m}')
std = standard_deviation(df)
print (f'the standatrd deviation of the each feature is: {std}')

plot(df)
log_plot(df)

if __name__=='__main__':
    main()
