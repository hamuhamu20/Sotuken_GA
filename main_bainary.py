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
daytime_error = 0

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

num = 0
# 初期集団の生成
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

# 評価関数
def evaluation(ga):
    """評価関数です。今回は全ての遺伝子が1となれば最適解となるので、
    合計して遺伝子と同じ長さの数となった場合を1として0.00~1.00で評価します
    :param ga: 評価を行うgenomClass
    :return: 評価処理をしたgenomClassを返す
    """
    global grade1, grade2, grade3, grade4, error, daytime_error, num
    #適応度の初期値
    fitness = 0
    
    num += 1
    print(f"番号: {num}")
    print(f"遺伝子: {ga.getGenom()}")
    ##時間割にある遺伝子化
    fitness += timetable(ga, fitness)
    fitness += calculateMaxCoursesPerGrade(ga)
    print(f"時間割、学年別後のポイント: {fitness}")
    fitness += evaluateSoftConditions(ga) 
    print(f"総合評価値: {fitness}")
    print(" ")
    
    return fitness

    
    """ global grade1, grade2, grade3, grade4, error
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
        return -1 """

#時間割にある遺伝子かどうか
def timetable(ga, fit):
    global daytime_error
    gene2 = ga.getGenom()[2]
    gene3 = ga.getGenom()[3]
    gene4 = ga.getGenom()[4]
    gene5 = ga.getGenom()[5]
    gene6 = ga.getGenom()[6]
    gene7 = ga.getGenom()[7]
    day = days(gene2, gene3, gene4)
    time = times(gene5, gene6, gene7)
    day_time = f"{day}{time}"
    print(f"{day} : {time}")
    if day == 'error' or time == 'error':
        daytime_error += 1
        ##print(f"{day}{time}")
        return fit
    else:
        if day_time in day_time_count: 
            day_time_count[day_time] += 1
            return int(1) 

#学年別開講講義数の上限に達していないかどうか
def calculateMaxCoursesPerGrade(ga):
    global grade1, grade2, grade3, grade4, error

    ##遺伝子を学年別に割り振る
    gene0 = ga.getGenom()[0]
    gene1 = ga.getGenom()[1]
    ##print(f"gene2: {gene2}, gene3: {gene3}") 

    if gene0 == 1 and gene1 == 1 and grade4 < 48:
        grade4 += 1
        # print(f"Grade4 incremented: {grade4}")
        print("grade4")
        return int(1)
    elif gene0 == 1 and gene1 == 0 and grade3 < 82:
        grade3 += 1
        # print(f"Grade3 incremented: {grade3}")
        print("grade3")
        return int(1)
    elif gene0 == 0 and gene1 == 1 and grade2 < 95:
        grade2 += 1
        # print(f"Grade2 incremented: {grade2}")
        print("grade2")
        return int(1)
    elif gene0 == 0 and gene1 == 0 and grade1 < 244:
        grade1 += 1
        # print(f"Grade1 incremented: {grade1}")
        print("grade1")
        return int(1)
    else:
        print("grade error")
        return int(0)
    
        ##print(f"gene2 changed to: {gene2}, gene3 changed to: {gene3}")

# ソフト条件
def evaluateSoftConditions(ga):
    gene0 = ga.getGenom()[0]
    gene1 = ga.getGenom()[1]
    gene2 = ga.getGenom()[2]
    gene3 = ga.getGenom()[3]
    gene4 = ga.getGenom()[4]
    gene5 = ga.getGenom()[5]
    gene6 = ga.getGenom()[6]
    gene7 = ga.getGenom()[7]
    gene8 = ga.getGenom()[8]
    gene9 = ga.getGenom()[9]

    global day_time_count

    grade = grades(gene0, gene1)
    time = times(gene5, gene6, gene7)
    day = days(gene2, gene3, gene4)
    day_time = f"{day}{time}"

    #ゼミがあるか
    if time == 'error' or day == 'error':
        print("曜日か時限がエラーです")
        return int(0)
    elif gene8 == 1 and grade in (4, 3) and day_time in ('tue4th', 'tue5th', 'thu5th'):
        print("ゼミポイント")
        return int(10)
    elif gene9 == 1 and grade == 1 and day_time == 'wed1st':#教養演習があるか
        print("教養演習ポイント")
        return int(10)
    elif time in ('2nd', '3rd', '4rd'):
        point = 0
        if time == '2nd':
            point += 3
        elif time == '3rd':
            point += 2
        elif time == '4th':
            point += 1
        else:
            print("point time error")
            point += 0

        if gene0 == 0 and gene1 == 0:
            point *= 4
        elif gene0 == 0 and gene1 == 1:
            point *= 3
        elif gene0 == 1 and gene1 == 0:
            point *= 2
        elif gene0 == 1 and gene1 == 1:
            point *= 1
        else:
            print("point grade error")
            point *= 0

        print(f"point: {point}")
        return int(point)
    else:
    # elif time != 'error' and day != 'error':
        print(f"{time}は0ポイントです")
        return int(0)

# 曜日を求める
def days(gene1, gene2, gene3):
    if gene1 == 0 and gene2 == 0 and gene3 == 0:
        return 'mon'
    elif gene1 == 0 and gene2 == 0 and gene3 == 1:
        return 'tue'
    elif gene1 == 0 and gene2 == 1 and gene3 == 0:
        return 'wed'
    elif gene1 == 0 and gene2 == 1 and gene3 == 1:
        return 'thu'
    elif gene1 == 1 and gene2 == 1 and gene3 == 1:
        return 'fri'
    else:
        return 'error'

# 時限を求める    
def times(gene1, gene2, gene3):
    if gene1 == 0 and gene2 == 0 and gene3 == 0:
        return '1st'
    elif gene1 == 0 and gene2 == 0 and gene3 == 1:
        return '2nd'
    elif gene1 == 0 and gene2 == 1 and gene3 == 0:
        return '3rd'
    elif gene1 == 0 and gene2 == 1 and gene3 == 1:
        return '4th'
    elif gene1 == 1 and gene2 == 1 and gene3 == 1:
        return '5th'
    else:
        return 'error'

# 学年を求める
def grades(gene0, gene1):
    if gene0 == 1 and gene1 == 1:
        # print(f"Grade4 incremented: {grade4}")
        return 4
    elif gene0 == 1 and gene1 == 0:
        # print(f"Grade3 incremented: {grade3}")
        return 3
    elif gene0 == 0 and gene1 == 1:
        # print(f"Grade2 incremented: {grade2}")
        return 2
    elif gene0 == 0 and gene1 == 0:
        # print(f"Grade1 incremented: {grade1}")
        return 1
    else:
        # print("error")
        print("error")
    

# 遺伝子情報の長さ
GENOM_LENGTH = 10
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
    # 一番最初の現行世代個体集団を生成します。
    current_generation_individual_group = []
    for i in range(MAX_GENOM_LIST):
        current_generation_individual_group.append(create_genom(GENOM_LENGTH))
    
    for count_ in range(1, MAX_GENERATION + 1):
        for i in range(MAX_GENOM_LIST):
            
            evaluation_result = evaluation(current_generation_individual_group[i])
            current_generation_individual_group[i].setEvaluation(evaluation_result)


    """ for idx, individual in enumerate(current_generation_individual_group):
        print(f"Individual {idx + 1} | Evaluation: {individual.getEvaluation()} | GA: {individual.getGenom()}") """
    
    print(f"total grade1: {grade1}")
    print(f"total grade2: {grade2}")
    print(f"total grade3: {grade3}")
    print(f"total grade4: {grade4}")
    print(f"total error: {error}")
    print(f"total daytime_error: {daytime_error}")
    
    # 時間割形式で結果を表示する
    print("      |  1st |  2nd |  3rd |  4th |  5th |")
    print("------+------+------+------+------+------+")
    for day in ["mon", "tue", "wed", "thu", "fri"]:
        print(f"{day.capitalize():>5}", end=" | ")
        for time in ["1st", "2nd", "3rd", "4th", "5th"]:
            key = f"{day}{time}"
            if key in day_time_count:
                print(f"{day_time_count[key]:4}", end=" | ")
            else:
                print("  0 ", end="| ")
        print() 

    total = 0
    for key in day_time_count:
        total += day_time_count[key]
    
    print(f"total: {total}")

    

    """ for i in current_generation_individual_group:
        print(i.getGenom()) """  