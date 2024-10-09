# -*- coding: utf-8 -*-
# 著作 Azunyan
# コーディング規約は基本的にPEP8に準じて作成します。
# 本コードはOneMax問題を遺伝的アルゴリズムを用いて解くプログラムコードである。
#テスト中です。
import GeneticAlgorithm as ga
import random
from decimal import Decimal

# 遺伝子情報の長さ
GENOM_LENGTH = 12
# 遺伝子集団の大きさ
MAX_GENOM_LIST = 469
# 遺伝子選択数
SELECT_GENOM = 20
# 個体突然変異確率
INDIVIDUAL_MUTATION = 0.1
# 遺伝子突然変異確率
GENOM_MUTATION = 0.1
# 繰り返す世代数
MAX_GENERATION = 10


def create_genom(length):
    """
    引数で指定された桁のランダムな遺伝子情報を生成、格納したgenomClassで返します。
    :param length: 遺伝子情報の長さ
    :return: 生成した個体集団genomClass
    """
    genome_list = []
    for i in range(length):
        genome_list.append(random.randint(0, 1))
    return ga.genom(genome_list, 0)

def evaluation(ga):
    """評価関数です。今回は全ての遺伝子が1となれば最適解となるので、
    合計して遺伝子と同じ長さの数となった場合を1として0.00~1.00で評価します
    :param ga: 評価を行うgenomClass
    :return: 評価処理をしたgenomClassを返す
    """
    genom_total = sum(ga.getGenom())
    return Decimal(genom_total) / Decimal(GENOM_LENGTH)

def days(gene1, gene2, gene3):
    if gene1 == 0 and gene2 == 0 and gene3 == 1:
        return 'mon'
    elif gene1 == 0 and gene2 == 1 and gene3 == 0:
        return 'tue'
    elif gene1 == 0 and gene2 == 1 and gene3 == 1:
        return 'wed'
    elif gene1 == 1 and gene2 == 0 and gene3 == 0:
        return 'thu'
    elif gene1 == 1 and gene2 == 0 and gene3 == 1:
        return 'fri'
    else:
        return 'fri'
    
def times(gene1, gene2, gene3):
    if gene1 == 0 and gene2 == 0 and gene3 == 1:
        return '1st'
    elif gene1 == 0 and gene2 == 1 and gene3 == 0:
        return '2nd'
    elif gene1 == 0 and gene2 == 1 and gene3 == 1:
        return '3rd'
    elif gene1 == 1 and gene2 == 0 and gene3 == 0:
        return '4th'
    elif gene1 == 1 and gene2 == 0 and gene3 == 1:
        return '5th'
    else:
        return '5th'

if __name__ == '__main__':
    grade1 = 0
    grade2 = 0
    grade3 = 0
    grade4 = 0

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

    """ mon1st = 0
    mon2nd = 0
    mon3rd = 0
    mon4th = 0
    mon5th = 0
    tue1st = 0
    tue2nd = 0
    tue3rd = 0
    tue4th = 0
    tue5th = 0
    wed1st = 0
    wed2nd = 0
    wed3rd = 0
    wed4th = 0
    wed5th = 0
    thu1st = 0
    thu2nd = 0
    thu3rd = 0
    thu4th = 0
    thu5th = 0
    fri1st = 0
    fri2nd = 0
    fri3rd = 0
    fri4th = 0
    fri5th = 0 """

    # 一番最初の現行世代個体集団を生成します。
    current_generation_individual_group = []
    for i in range(MAX_GENOM_LIST):
        current_generation_individual_group.append(create_genom(GENOM_LENGTH))
    
    for i in current_generation_individual_group:
        gene1 = i.getGenom()[0]
        gene2 = i.getGenom()[1]
        
        if gene1 == 0 and gene2 == 0:
            grade1+=1
        elif gene1 == 0 and gene2 == 1:
            grade2+=1
        elif gene1 == 1 and gene2 == 0:
            grade3+=1
        elif gene1 == 1 and gene2 == 1:
            grade4+=1
        else:
            pass
    
    print(grade1)
    print(grade2)
    print(grade3)
    print(grade4)

    for i in current_generation_individual_group:
        gene3 = i.getGenom()[2]
        gene4 = i.getGenom()[3]
        gene5 = i.getGenom()[4]
        gene6 = i.getGenom()[5]
        gene7 = i.getGenom()[6]
        gene8 = i.getGenom()[7]

        day = days(gene3, gene4, gene5)
        time = times(gene6, gene7, gene8)

        """ if day == "mon" and time == "1st":
            mon1st += 1
        elif day == "mon" and time == "2nd":
            mon2nd += 1  """

        day_time = f"{day}{time}"
        if day_time in day_time_count:
            day_time_count[day_time] += 1
    
    # 時間割形式で結果を表示する
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



    """ for i in current_generation_individual_group:
        print(i.getGenom())  """