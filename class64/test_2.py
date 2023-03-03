

class TrieNode:

    def __init__(self):

        self.charMap = {}

        self.isEnd = False



class Trie:

    def __init__(self):

        self.root = TrieNode()



    def insert(self, inputString):

        curr = self.root

        for x in inputString:

            if x not in curr.charMap:

                curr.charMap[x] = TrieNode()

            curr = curr.charMap[x]

        # set the last node's isEnd=True

        curr.isEnd = True



    def search(self, matchString):

        curr = self.root

        for x in matchString:

            if x not in curr.charMap:

                return False

            curr = curr.charMap[x]



        return True



class Solution:

    # @param A : list of strings

    # @param B : list of strings

    # @return a strings

    def solve(self, A, B):

        # insert all the strings in Trie first

        TrieObj = Trie()

        for x in A:

            TrieObj.insert(x)



        # search for each string in the Trie

        ans = ""

        n = len(B)

        for i in range(n):

            curr_string = B[i]

            # convert the string to list because string is immutable

            string_list = list(curr_string)

            nB = len(curr_string)

            match_found = False

            for j in range(nB):

                # save the current position character to restore for later iterations

                temp = string_list[j]

                # replace the curr index char with each char from a-z and

                # check whether the string exists in our Trie or not

                for k in range(ord('a'), ord('z')+1):

                    replace_char = chr(k)

                    if temp!=replace_char:

                        string_list[j]=replace_char

                        if TrieObj.search(''.join(string_list)):

                            # match with exactly 1 modification found,

                            # dont check for further alphabets, break

                            match_found = True

                            break



                # match with exactly 1 modification found,

                # dont check for further indexes,  break

                if match_found:

                    break

                else:

                    # replace back the current position character with original character

                    # and continue checking

                    string_list[j]=temp



            # update the answer string

            if match_found:

                ans+="1"

            else:

                ans+="0"



        return ans