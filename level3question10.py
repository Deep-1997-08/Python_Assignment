def count_customers_walked_away(N, S):
    in_cafe = set()
    using_computer = set()
    walked_away = 0

    for customer in S:
        if customer in using_computer:
            using_computer.remove(customer)
            in_cafe.remove(customer)
        elif customer not in in_cafe:
            in_cafe.add(customer)
            if len(using_computer) < N:
                using_computer.add(customer)
            else:
                walked_away += 1

    return walked_away

N1 = 3
S1 = "GACCBDDBAGEE"
print(count_customers_walked_away(N1, S1))  

N2 = 1
S2 = "ABCBAC"
print(count_customers_walked_away(N2, S2))  
