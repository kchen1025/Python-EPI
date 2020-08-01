from typing import List

from test_framework import generic_test
import math

# RECURSIVEEEEE dont delete
def minimum_messiness(words: List[str], line_length: int) -> int:
    memo = [(line_length - len(words[0]))**2] + [math.inf for i in range(len(words)-1)]

    for i in range(1,len(words)):
        # calculate current line as if it were by itself
        current_line_spaces = line_length - len(words[i])
        # add that to our memo for this word's messiness
        memo[i] = memo[i-1] + current_line_spaces**2

        # loop backwards from the current word, adding the previous word into the current line and adjusting the messiness
        for j in reversed(range(i)):
            # subtract word plus a space into our current_line_spaces
            current_line_spaces -= (len(words[j]) + 1)
            # if we overflowed out of this line, we cannot do anymore computation
            if current_line_spaces < 0:
                break

            # otherwise, we want to calculate our new messiness with this line
            # we calculate that by taking the messiness of the words right before the beginning of our line
            # because we are assuming that is the min messiness
            first_j_messiness = memo[j-1] if j-1>=0 else 0
            memo[i] = min(memo[i], current_line_spaces**2 + first_j_messiness)

    return memo[-1]












































    # memo = [math.inf for i in range(len(words))]
    #
    # def traverse(idx):
    #     if idx < 0: return 0
    #     if memo[idx] != math.inf: return memo[idx]
    #
    #     current_spaces = line_length - len(words[idx])
    #     memo[idx] = current_spaces**2 + traverse(idx-1)
    #
    #     for j in reversed(range(idx)):
    #         # get messiness of current plus that word
    #         current_spaces -= (len(words[j]) + 1)
    #         if current_spaces < 0:
    #             break;
    #
    #         # get previous line and add to current messiness
    #         memo[idx] = min(memo[idx], current_spaces**2 + traverse(j-1))
    #
    #     return memo[idx]
    #
    # yeet = traverse(len(words)-1)
    # print(memo)
    # return yeet






































    #
    # min_messiness = [math.inf for i in range(len(words))]
    #
    # def getMinMessiness(idx):
    #     if idx < 0:
    #         return 0
    #     if min_messiness[idx] != math.inf:
    #         return min_messiness[idx]
    #
    #     # set for if only current word was by itself
    #     number_of_spaces = line_length - len(words[idx])
    #     min_messiness[idx] = number_of_spaces**2 + getMinMessiness(idx-1)
    #
    #     for j in reversed(range(0,idx)):
    #         number_of_spaces -= (len(words[j]) + 1)
    #         if number_of_spaces < 0:
    #             break
    #
    #         min_messiness[idx] = min(min_messiness[idx], number_of_spaces**2 + getMinMessiness(j-1))
    #
    #     return min_messiness[idx]
    #
    # return getMinMessiness(len(words)-1)


    # # create memo list with first calculated
    # min_messiness = [(line_length - len(words[0]))**2] + [math.inf for i in range(1,len(words))]
    #
    # # loop through each word 1 to end
    # for i in range(1,len(words)):
    #     # first, insert the 'max', which is assuming each word is on a separate line
    #     # and add that to our total messiness
    #     number_of_spaces = line_length - len(words[i])
    #     min_messiness[i] = number_of_spaces**2 + min_messiness[i-1]
    #
    #     # then, loop starting from i-1 to 0, simulating what the adjusted messiness is if you add that char into the current line
    #     for j in reversed(range(0,i)):
    #         # subtract the spaces from the current word
    #         number_of_spaces -= (len(words[j]) +1)
    #         # if number of spaces is less than 0, we have overflowed out of current line
    #         if number_of_spaces < 0:
    #             break
    #         # get min_messiness of j-1
    #         first_j_messiness = 0 if j-1 < 0 else min_messiness[j-1]
    #         # get messiness of current line
    #         current_messiness = number_of_spaces**2
    #         min_messiness[i] = min(min_messiness[i], first_j_messiness + current_messiness)
    # return min_messiness[-1]




if __name__ == '__main__':
    # print(minimum_messiness(["aaa", "bbb", "c", "d", "ee"],11))
    #print(minimum_messiness(['mesr', 'jwdqwgycd', 'vw', 'j', 'g', 'pbkduivw', 'vyu', 'ucop', 'k', 'qmobppce', 't', 'gawtasqleg', 's', 'onsgiam', 'zdcjixtr', 'm', 'rqrds', 'xql', 'de', 'klxs', 'ia', 'kothct', 'gd', 'mombpskbrm', 'trmq', 'gseiperkze', 'qwix', 'crxdvfrjy', 'lrqaaumf', 'zmwex', 'czlc'], 18))
    # print(minimum_messiness(['aa','bbb','cc','dddd'],10))
    exit(
        generic_test.generic_test_main('pretty_printing.py',
                                       'pretty_printing.tsv',
                                       minimum_messiness))
