# -*- coding: utf-8 -*-
"""https://www.tensorflow.org/tfx/serving/api_rest
"""
import requests


def main():
    url = 'http://localhost:8501/v1/models/half_plus_two:predict'
    data = {"instances": [1.0, 2.0, 5.0]}
    res = requests.request(method='POST', url=url, json=data)
    response = res.json()
    return


if __name__ == '__main__':
    main()
    print('\ndone')