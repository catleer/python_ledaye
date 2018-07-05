"""
Created by catleer on 2018-05-21.
"""
__author__ = 'catleer'

import os, codecs, json


def get_case_file():
    if __name__ == '__main__':
        parent_path = os.path.abspath('..')
    else:
        parent_path = os.path.abspath('.')
    dir = parent_path + r'\casedatas'
    case_files = os.listdir(dir)
    for case_file in case_files:
        case_file = os.path.join(dir, case_file)
        yield case_file


def get_case():
    case_files = get_case_file()

    for case_file in case_files:
        try:
            with codecs.open(case_file, 'r', encoding='utf-8') as f:
                f_dict = json.load(f)
                for case in f_dict['CaseInfo']:
                    if case['Flag']:
                        yield case
        except json.decoder.JSONDecodeError:
            yield


def get_case_data():
    cases = get_case()
    for case in cases:
        if case:
            case_module = case['CaseModule']
            case_id = case["CaseId"]
            case_title = case["Title"]
            case_info = case_module + case_id + ":" + case_title

            url_path = case['UrlPath']
            url_data = case['UrlData']
            case_data = (url_path, url_data)
            for k, v in case['HttpData'].items():
                case_data = case_data + (v,)

            case_result = case['Result']
            yield [case_info, case_data, case_result]


if __name__ == '__main__':
    file_data = get_case()
    for i in file_data:
        print(i)




