import re

el_exp = r"\$\{(.+)\}"
pattern = re.compile(el_exp)


def get_el_expression(string: str):
    """
    获取el表达式
    :param string:
    :return:
    """
    return re.findall(pattern, string)


if __name__ == "__main__":
    s = "select * from xxx where name = '${mygod}'"
    print(get_el_expression(s))
