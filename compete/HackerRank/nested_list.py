if __name__ == '__main__':
    # for _ in range(int(input())):
    #     name = input()
    #     score = float(input())
    students = [['Harry', 37.21], ['Berry', 37.21], [
        'Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
    second_lowest_score = sorted(set(map(lambda x: x[1], students)))[1]
    print('\n'.join(sorted([i[0]
          for i in students if i[1] == second_lowest_score])))
