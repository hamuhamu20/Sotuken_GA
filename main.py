# -*- coding: utf-8 -*-
# 著作 Azunyan
# コーディング規約は基本的にPEP8に準じて作成します。
# 本コードはOneMax問題を遺伝的アルゴリズムを用いて解くプログラムコードである。

import GeneticAlgorithm as ga
import random
from decimal import Decimal

grade1 = 0
grade2 = 0
grade3 = 0
grade4 = 0
error = 0
def create_genom(length):
    """
    引数で指定された桁のランダムな遺伝子情報を生成、格納したgenomClassで返します。
    :param length: 遺伝子情報の長さ
    :return: 生成した個体集団genomClass
    """
    
    first_digit = random.randint(1,5)
    second_digit = random.randint(1,5)
    first_two_digits = f"{first_digit}{second_digit}"
    remaining_bits = ''.join(random.choice('01') for _ in range(length - 2))
    individual = [int(bit) for bit in first_two_digits + remaining_bits]
    return ga.genom(individual, 0)

def evaluation(ga):
    """評価関数です。今回は全ての遺伝子が1となれば最適解となるので、
    合計して遺伝子と同じ長さの数となった場合を1として0.00~1.00で評価します
    :param ga: 評価を行うgenomClass
    :return: 評価処理をしたgenomClassを返す
    """
    global grade1, grade2, grade3, grade4, error
    gene2 = ga.getGenom()[2]
    gene3 = ga.getGenom()[3]
    print(f"gene2: {gene2}, gene3: {gene3}") 

    if gene2 == 0 and gene3 == 0 and grade1 < 244:
        grade1+=1
        ##print(f"Grade1 incremented: {grade1}")
        return 1
    elif gene2 == 0 and gene3 == 1 and grade2 < 95:
        grade2+=1
        ##print(f"Grade2 incremented: {grade2}")
        return 1
    elif gene2 == 1 and gene3 == 0 and grade3 < 82:
        grade3+=1
        ##print(f"Grade3 incremented: {grade3}")
        return 1
    elif gene2 == 1 and gene3 == 1 and grade4 < 42:
        grade4+=1
        ##print(f"Grade4 incremented: {grade4}")
        return 1
    else:
        error+=1
        ##print("error")
        return -1


def days(gene1):
    if gene1 == 1:
        return 'mon'
    elif gene1 == 2:
        return 'tue'
    elif gene1 == 3:
        return 'wed'
    elif gene1 == 4:
        return 'thu'
    elif gene1 == 5:
        return 'fri'
    else:
        print("error")
    
def times(gene1):
    if gene1 == 1:
        return '1st'
    elif gene1 == 2:
        return '2nd'
    elif gene1 == 3:
        return '3rd'
    elif gene1 == 4:
        return '4th'
    elif gene1 == 5:
        return '5th'
    else:
        print("error")


# 遺伝子情報の長さ
GENOM_LENGTH = 8
# 遺伝子集団の大きさ
MAX_GENOM_LIST = 469
# 遺伝子選択数
SELECT_GENOM = 20
# 個体突然変異確率
INDIVIDUAL_MUTATION = 0.1
# 遺伝子突然変異確率
GENOM_MUTATION = 0.1
# 繰り返す世代数
MAX_GENERATION = 1


if __name__ == '__main__':

    day_time_count = {
        "mon1st": 0,
        "mon2nd": 0,
        "mon3rd": 0,
        "mon4th": 0,
        "mon5th": 0,
        "tue1st": 0,
        "tue2nd": 0,
        "tue3rd": 0,
        "tue4th": 0,
        "tue5th": 0,
        "wed1st": 0,
        "wed2nd": 0,
        "wed3rd": 0,
        "wed4th": 0,
        "wed5th": 0,
        "thu1st": 0,
        "thu2nd": 0,
        "thu3rd": 0,
        "thu4th": 0,
        "thu5th": 0,
        "fri1st": 0,
        "fri2nd": 0,
        "fri3rd": 0,
        "fri4th": 0,
        "fri5th": 0
    }


    # 一番最初の現行世代個体集団を生成します。
    current_generation_individual_group = []
    for i in range(MAX_GENOM_LIST):
        current_generation_individual_group.append(create_genom(GENOM_LENGTH))
    
    for count_ in range(1, MAX_GENERATION + 1):
        for i in range(MAX_GENOM_LIST):
            
            evaluation_result = evaluation(current_generation_individual_group[i])
            current_generation_individual_group[i].setEvaluation(evaluation_result)


    for i in current_generation_individual_group:
        gene0 = i.getGenom()[0]
        gene1 = i.getGenom()[1]
        

        day = days(gene0)
        time = times(gene1)

        day_time = f"{day}{time}"
        if day_time in day_time_count:
            day_time_count[day_time] += 1
    
    # 時間割形式で結果を表示する
    print("     | 1st | 2nd | 3rd | 4th | 5th |")
    print("-----+----+----+----+----+----+")
    for day in ["mon", "tue", "wed", "thu", "fri"]:
        print(f"{day.capitalize():>5}", end=" | ")
        for time in ["1st", "2nd", "3rd", "4th", "5th"]:
            key = f"{day}{time}"
            if key in day_time_count:
                print(f"{day_time_count[key]:4}", end=" | ")
            else:
                print("  0 ", end="| ")
        print() 

    for idx, individual in enumerate(current_generation_individual_group):
        print(f"Individual {idx + 1} Evaluation: {individual.getEvaluation()}")

    print(f"total grade1: {grade1}")
    print(f"total grade2: {grade2}")
    print(f"total grade3: {grade3}")
    print(f"total grade4: {grade4}")
    print(f"total error: {error}")

    """ for i in current_generation_individual_group:
        print(i.getGenom()) """  