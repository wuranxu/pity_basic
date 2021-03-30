"""
pity变量池
变量池的生命周期随着用例而
"""
__author__ = "xiaoke"


class VarPool(object):

    def __init__(self, case_id, prefix="pity"):
        """

        :param case_id: 用来标识变量所处的主生命周期case
        :param prefix: 前缀，默认为pity，可以自行更改
        """
        self.cache = dict()
        self.prefix = prefix
        self.case_id = case_id

    def get_key(self, key):
        return f"{self.prefix}_{key}"

    def set(self, key, value):
        self.cache[self.get_key(key)] = value

    def get(self, key):
        return self.cache.get(self.get_key(key))

    def get_default(self, key, default_value):
        return self.cache.get(self.get_key(key), default_value)
