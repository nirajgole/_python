import math
def movie(card, ticket, perc):
    count = 0;
    ticket_price =  0
    while math.ceil(card) >= ticket_price:
        count += 1
        card+=ticket*(perc**count)
        ticket_price+=ticket
    return count

movie(30, 5, 0.95)
movie(500, 15, 0.9)# 43
movie(100, 10, 0.95)# 24