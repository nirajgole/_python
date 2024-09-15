#Solution 1:
# def rps(p1, p2):
#     hand = {'rock':0, 'paper':1, 'scissors':2}
#     results = ['Draw!', 'Player 1 won!', 'Player 2 won!']
#     return results[hand[p1] - hand[p2]] # based on positive and negative indexing

#Solution 2:
def rps(p1, p2):
    return p1 == p2 and 'Draw!' or f"Player {(p2[0] + p1[0] in 'rspr') + 1} won!"

print(rps('scissors','paper')) # Player 1 won!
print(rps('scissors','rock')) # Player 2 won!
print(rps('paper','paper')) # Draw!