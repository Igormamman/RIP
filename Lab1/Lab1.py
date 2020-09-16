from math import sqrt
import sys

print("Шпак Игорь")
print("ИУ5-54Б")


def parseargs():
    listik = []
    i = 1
    args = str(sys.argv)
    while i < (len(sys.argv)):
        try:
            listik.append(float(sys.argv[i]))
            i += 1
        except Exception as e:
            print("%i параметр введен не верно" % i)
            listik.append(sys.argv[i])
            i += 1
            continue
    return listik


def readargs(list):
    i = 0
    while i < len(list):
        if type(list[i]) != float:
            print("Введите %i параметр" % (i + 1))
            list[i] = float(input())
        i += 1
    while True:
        try:
            if len(list) < 3:
                list.append(float(input()))
            elif len(list) == 3:
                break
        except Exception as e:
            print("Ошибка ввода параметров, повторите ввод")
    print(list)
    return list


def findroots(ICoef):
    roots = []
    D = ICoef[1] * ICoef[1] - 4 * ICoef[0] * ICoef[2]
    if D < 0:
        print("Корней не существует")
    if ICoef[0] == 0:
        if ICoef[1] == 0:
            if ICoef[2] == 0:
                print("Корни любые")
                return roots
            elif ICoef[2] != 0:
                print("Корней не существует")
                return roots
        if ICoef[1] / ICoef[2] <= 0:
            print(ICoef[1] / ICoef[2])
            roots.append(sqrt(-ICoef[2] / ICoef[1]))
            roots.append(-sqrt(-ICoef[2] / ICoef[1]))
        else:
            print("Корней не существует")
            return roots
    if D > 0:
        if ((-ICoef[1] - sqrt(D)) / (2 * ICoef[0]) >= 0) and ((-ICoef[1] + sqrt(D)) / (2 * ICoef[0]) >= 0):
            roots.append(sqrt((-ICoef[1] - sqrt(D)) / (2 * ICoef[0])))
            roots.append(-sqrt((-ICoef[1] - sqrt(D)) / (2 * ICoef[0])))
            roots.append(sqrt((-ICoef[1] + sqrt(D)) / (2 * ICoef[0])))
            roots.append(-sqrt((-ICoef[1] + sqrt(D)) / (2 * ICoef[0])))
        elif ((-ICoef[1] - sqrt(D)) / (2 * ICoef[0]) >= 0) or ((-ICoef[1] + sqrt(D)) / (2 * ICoef[0]) >= 0):
            if ((-ICoef[0] - D) / (2 * ICoef[0])) >= 0:
                D = (-ICoef[1] - sqrt(D)) / (2 * ICoef[0])
                roots.append(sqrt(D))
                roots.append(-sqrt(D))
            elif ((-ICoef[1] + sqrt(D)) / (2 * ICoef[0])) >= 0:
                D = ((-ICoef[1] + sqrt(D)) / (2 * ICoef[0]))
                roots.append(sqrt(D))
                roots.append(-sqrt(D))
    return roots


def printroots(list):
    if len(list) > 0:
        print("Корни уравнения:", end=" ")
        for x in list:
            print(x, end=" ")
    print()


printroots(findroots(readargs(parseargs())))
