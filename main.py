# -*- coding = utf-8 -*-
# @Python : 3.8
import random
import time
import os

ulpb_dict = {'iu': 'q', 'ei': 'w', 'e': 'e', 'uan': 'r', 'ue': 't', 'un': 'y', 'sh': 'u', 'ch': 'i', 'uo': 'o',
             'ie': 'p', 'a': 'a', 'ong': 's', 'iong': 's', 'ai': 'd', 'en': 'f', 'eng': 'g', 'ang': 'h', 'an': 'j',
             'uai': 'k', 'ing': 'k', 'iang': 'l', 'uang': 'l', 'ou': 'z', 'ia': 'x', 'ua': 'x', 'ao': 'c', 'zh': 'v',
             'ui': 'v', 'in': 'b', 'iao': 'n', 'ian': 'm'}


# ulpb_dict = {'iu': 'q', 'ei': 'w', 'e': 'e', 'uan': 'r'}
# def init():
#     with open("./ulpb.csv")as f:
#         lines = f.readlines()
#     kv = {line.replace("\n", "").split(",")[1]: line.replace("\n", "").split(",")[0] for line in lines}
#     return kv
#

#  创建文件夹
def path_creat(_path):
    if not os.path.exists(_path):
        os.mkdir(_path)
    return _path


def save(name, l, t):
    with open(f"./result/{name}.csv", "a+", encoding="utf-8-sig") as f:
        f.write(f"{t},{len(l)},{' '.join(l)}\n")


def loop(t) -> list:
    # ulpb_dict = init()
    errors = []
    print(f"训练答案：{ulpb_dict}\r\n")
    loading_list = list(ulpb_dict.keys())
    # print(loading_list)
    while len(loading_list) != 0:
        l = random.choice(loading_list)
        print("-" * 5, f"time_used:{int(time.time() - now)}s    left:{len(loading_list)}", "-" * 5)
        _input = input(f'*  {l}对应的字母是：')
        while _input == "?":
            print(f"Check:\n    Still left:{len(loading_list)}\n    {loading_list}")
            _input = input(f'   {l}对应的字母是：')
        if _input == ulpb_dict[l]:
            print(f"Right!")
            loading_list.remove(l)
        else:
            errors.append(l)
            loading_list.append(l)
            print(f"Error!   {l}:{ulpb_dict[l]}")

    return errors


if __name__ == '__main__':
    path_creat("./result")
    name = int(time.time())
    print(f"""
* 欢迎来到小鹤双拼训练                    *
* 程序开启循环练习                       *
* 请输入屏幕显示对应的字母                 *
* 当次循环不出现错误的时候挑战完成           *
* 每次循环成绩(用时,错误数,错误)会记录到{name}.scv""")
    time.sleep(2)
    print("-" * 20)
    with open(f"./result/{name}.csv", "w", encoding="utf-8-sig") as f:
        f.write("time_used,error_num,error_list\n")
    while True:
        print("-" * 20)
        now = time.time()
        errs = loop(now)
        t_u = int(time.time() - now)
        print("-" * 20)
        print(f"本次用时{t_u}秒")
        save(name=name, l=errs, t=t_u)
        if len(errs) == 0:
            print("恭喜，本次无错！")
            print(f"成绩记录在{name}.csv\n程序退出")
            break
        else:
            print(f"本次训练错误次数：{len(errs)}")
            print(f"错误列表：{errs}")
            print(f"已记录到本地{name}.csv")
