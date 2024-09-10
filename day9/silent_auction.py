header = """
                         ___________
                          \        /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-'''---------'' '-'
                          )'''''''(
                         /_________\\
                       .-------------.
                      /_______________\\
"""
print(header)
bidders = {}
winner = ""
max = 0
while True:
    user = input("What is your name:?")
    bid = input("What is your bid $?")
    bidders[user] = bid
    x =input("Are there any more bidders?")
    if x =="no":
        break

for bidder in bidders.items():
    if max < int(bidder[1]):
        max = int(bidder[1])
        winner = bidder[0] +" with bet " + bidder[1]

print(winner)
