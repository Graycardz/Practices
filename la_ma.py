def doi_so_la_ma(s: str) -> int:
    gtri_la_ma = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if any(c not in gtri_la_ma for c in s):
        print(f"Không có số La Ma nào tương ứng với {nhap}")
        return 0
    result = 0
    for i in range(len(s)):
        if i > 0 and gtri_la_ma[s[i]] > gtri_la_ma[s[i - 1]]:
            result += gtri_la_ma[s[i]] - 2 * gtri_la_ma[s[i - 1]]
        else:
            result += gtri_la_ma[s[i]]
    return result

nhap = input("Nhập chữ số La Mã: ")
result = doi_so_la_ma(nhap)
if result != 0:
    print(f"Số La Mã tương ứng của {nhap} là {result}.")