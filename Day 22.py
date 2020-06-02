class Solution(object):
    def frequencySort(self, str):
        """
        :type str: str
        :rtype: str
        """
        return "".join([char * times for char, times in collections.Counter(str).most_common()])
