"""
pity变量池
变量池的生命周期与用例保持一致
"""
__author__ = "xiaoke"


class VarPool(object):

    def __init__(self, case_id):
        """

        :param case_id: 用来标识变量所处的主生命周期case
        """
        self.cache = dict()
        self.case_id = case_id

    def set(self, key, value):
        self.cache[key] = value

    def get(self, key):
        return self.cache.get(key)

    def get_default(self, key, default_value):
        return self.cache.get(key, default_value)
