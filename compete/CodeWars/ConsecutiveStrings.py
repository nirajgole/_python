def longest_consec(strarr, k):
    longest_str = ''
    n = len(strarr)
    if k > 0 and n >= k:
        for i in range(n-(k-1)):
            temp_str = "".join(strarr[i:i+k])
            if(len(longest_str) < len(temp_str)):
                longest_str = temp_str
    return longest_str


print(longest_consec(["zone", "abigail", "theta", "form",
      "libe", "zas", "theta", "abigail"], 2))  # "abigailtheta"
