''' THIS CODE IS MY OWN WORK, IT WAS WRITTEN WITHOUT
CONSULTING CODE WRITTEN BY OTHER STUDENTS. Aisha Sajo '''

import pandas as pd
from itertools import combinations
import sys

def apriori_algo(min_supp, output_file):
    data = pd.read_csv('data.csv')
    
    #extract from "text_keywords"
    items = set(keyword for keywords in data['text_keywords'] for keyword in keywords.split())
    
    #calc support for the itemsets
    def get_supp_count(itemset):
        return sum(all(word in keywords.split() for word in itemset) for keywords in data['text_keywords'])
    
    #generating freq 1-itemsets (seen in part 1 where we just found the support for each item w min-supp = 2)
    freq_itemsets = { (item,) : get_supp_count([item]) for item in items if get_supp_count([item])>= min_supp}
    all_freq_itemsets = freq_itemsets.copy()
    
    # higher-order freq itemsets
    length = 2
    while freq_itemsets:
        candidates = list(combinations(set(item for itemset in freq_itemsets for item in itemset), length))
        freq_itemsets = {candidates: get_supp_count(candidate) for candidate in candidates if get_supp_count([candidate]) >= min_supp}
        all_freq_itemsets.update(freq_itemsets)
        length+=1
        
    with open(output_file, 'w') as f:
        for itemset, support in all_freq_itemsets.items():
            f.write(f"{itemset}: {support}\n")
            
if __name__ == "__main__":
    min_supp = int(sys.argv[1])
    output_file = sys.argv[2]
    
    apriori_algo(min_supp, output_file)