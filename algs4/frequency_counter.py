"""
    Execution:
        python frequency_counter L < input.txt
    Data files:   
        https://algs4.cs.princeton.edu/31elementary/tnyTale.txt
        https://algs4.cs.princeton.edu/31elementary/tale.txt
        https://algs4.cs.princeton.edu/31elementary/leipzig100K.txt
        https://algs4.cs.princeton.edu/31elementary/leipzig300K.txt
        https://algs4.cs.princeton.edu/31elementary/leipzig1M.txt

    Read in a list of words from standard input and print out
    the most frequently occurring word that has length greater than
    a given threshold.

    % python frequency_counter 1 < tinyTale.txt
    it 10
  
    % python frequency_counter 8 < tale.txt
    business 122
  
    % python frequency_counter 10 < leipzig1M.txt
    government 24763
"""

#from algs4.st import ST
from algs4.sequential_search_st import SequentialSearchST


class FrequencyCounter:
    pass

if __name__ == "__main__":
    import sys
    minlen = int(sys.argv[1])
    st = SequentialSearchST()
    for line in sys.stdin:
        words = line.split()
        for word in words:

            if len(word) < minlen:
                continue
            if not st.contains(word):
                st.put(word, 1)
            else:
                st.put(word, st.get(word) + 1)
    maxstr = ""
    st.put(maxstr, 0)
    for word in st.keys():
        if st.get(word) > st.get(maxstr):
            maxstr = word
    print(maxstr, " ", st.get(maxstr))
