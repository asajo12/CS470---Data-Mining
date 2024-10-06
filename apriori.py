''' THIS CODE IS MY OWN WORK, IT WAS WRITTEN WITHOUT
CONSULTING CODE WRITTEN BY OTHER STUDENTS. Aisha Sajo '''

import pandas as pd
from itertools import combinations
import sys

def apriori_algo(min_supp, output_file):
    data = pd.read_csv('data.csv')
    #preprocess
    data['keywords_set'] = data['text_keywords'].apply(lambda x: set(x.split()))
    
    # extracting unique items 
    items = set(keyword for keywords in data['keywords_set'] for keyword in keywords)
    
    support_count = {}

    def get_supp_count(itemset):
        itemset = frozenset(itemset)  
        if itemset in support_count:
            return support_count[itemset]
        count = sum(itemset.issubset(keywords) for keywords in data['keywords_set'])
        support_count[itemset] = count
        return count

    #frequent 1-itemsets
    freq_itemsets = { (item,): get_supp_count([item]) for item in items if get_supp_count([item]) >= min_supp}
    all_freq_itemsets = freq_itemsets.copy()

    length = 2
    while freq_itemsets:
        #generate candidate itemsets of the next length only from previous frequent itemsets
        prev_freq_items = list(freq_itemsets.keys())
        candidates = [tuple(sorted(set(a).union(set(b)))) for a, b in combinations(prev_freq_items, 2) if len(set(a).union(set(b))) == length]

        #filter candidates by support count
        freq_itemsets = { candidate: get_supp_count(candidate) for candidate in candidates if get_supp_count(candidate) >= min_supp}
        
        #update all frequent itemsets with new ones
        all_freq_itemsets.update(freq_itemsets)
        length += 1

    with open(output_file, 'w') as f:
        for itemset, support in all_freq_itemsets.items():
            f.write(f"{itemset}: {support}\n")

if __name__ == "__main__":
    min_supp = int(sys.argv[1])
    output_file = sys.argv[2]
    
    apriori_algo(min_supp, output_file)
