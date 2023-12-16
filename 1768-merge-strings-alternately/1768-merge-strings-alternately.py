class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        answer = []
        st=""

        for i,j in zip(word1, word2):
            answer.append(i)
            answer.append(j)

        if len(word1) > len(word2):
            index = len(word1)-len(word2)
            for i in range(index):
                answer.append(word1[len(word2)+i])

        if len(word1) < len(word2):
            index = len(word2)-len(word1)
            for i in range(index):
                answer.append(word2[len(word1)+i])        

        return ''.join(answer)