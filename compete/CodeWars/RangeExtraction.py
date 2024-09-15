from time import time

# My solution
# def solution(args):
#     start=time()
#     res_arr = []
#     i = 0
#     while len(args) > i:
#         temp_arr = []
#         range_counter = 0
#         while len(args) > i+range_counter:
#             if args[i+range_counter] != args[i]+range_counter:
#                 break
#             temp_arr.append(args[i]+range_counter)
#             range_counter += 1
#         if(len(temp_arr) > 2):
#             res_arr.append(f'{temp_arr[0]}-{temp_arr[-1]}')
#             i += len(temp_arr)
#         else:
#             res_arr.append(args[i])
#             i += 1
#     end=time()
#     print(end-start)
#     return ",".join(map(str,res_arr))


# Best practice
def solution(args):
    out = []
    beg = end = args[0]

    for n in args[1:] + [""]:
        print(f'n{n} beg{beg} end{end}')
        if n != end + 1:
            if end == beg:
                print(f"end=beg")
                out.append(str(beg))
            elif end == beg + 1:
                print(f"end=beg+1")

                out.extend([str(beg), str(end)])
            else:
                out.append(str(beg) + "-" + str(end))
            beg = n
        end = n
    return ",".join(out)


print(solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11,
      14, 15, 17, 18, 19, 20]))  # '-6,-3-1,3-5,7-11,14,15,17-20'
