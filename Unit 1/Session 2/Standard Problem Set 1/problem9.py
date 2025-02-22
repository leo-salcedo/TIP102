def merge_alternately(word1, word2):
    res = ""
    start = 0
    min_len = min(len(word1), len(word2))

    for i in range(min_len):
        res += word1[i]
        res += word2[i]
        
    res += word1[min_len:]
    res += word2[min_len:]
    
    return res



word1 = "wol"
word2 = "oze"
print(merge_alternately(word1, word2))

word1 = "hfa"
word2 = "eflump"
print(merge_alternately(word1, word2))

word1 = "eyre"
word2 = "eo"
print(merge_alternately(word1, word2))