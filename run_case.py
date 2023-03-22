import yaml

# file = open('case.yaml', mode='r', encoding='utf-8')
# case_dict = yaml.safe_load(file)


class Run_Case:
    def __init__(self):
        file = open('case.yaml', mode='r', encoding='utf-8')
        self.steps = yaml.safe_load(file)

    @staticmethod
    def run_step(func, value):
        func(*value)

    def run_case(self, cases_file, lunch):
        cases = cases_file['cases']
        for case in cases:
            # 获取函数名
            func = lunch.__getattribute__(case['method'])
            # 获取参数
            case_list = list(case.value)
            self.run_step(func, case_list[2:])
