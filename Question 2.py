# Let A=[‘abc’, ‘xyz’, ‘aba’, 1221’] be a given string, and write a Python
# program that prints the string or strings and their index from the given list,
# ensuring that the first and last characters of the strings to be printed are
# identical.


A=['abc', 'xyz', 'aba', '1221']

for itr in A :
    if itr[0] == itr[len(itr)-1] :
        print(f"Identical String {itr} found at index {A.index(itr)}")