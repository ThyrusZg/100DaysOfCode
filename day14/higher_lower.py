import random

header = '''
  _    _  _         _                 
 | |  | |(_)       | |                
 | |__| | _   __ _ | |__    ___  _ __ 
 |  __  || | / _` || '_ \  / _ \| '__|
 | |  | || || (_| || | | ||  __/| |   
 |_|  |_||_| \__, ||_| |_| \___||_|   
  _           __/ |                   
 | |         |___/                    
 | |      ___ __      __ ___  _ __    
 | |     / _ \\ \ /\ / // _ \| '__|   
 | |____| (_) |\ V  V /|  __/| |      
 |______|\___/  \_/\_/  \___||_|                                            
'''
data =[
    {
        "id":1,
        "Name": "Vatican",
        "Population": 518
    },
    {
        "id":2,
        "Name": "Gibraltar",
        "Population": 32688
    },
    {
        "id": 3,
        "Name": "Liechtenstein",
        "Population": 39585
    },
    {
        "id": 4,
        "Name": "Andorra",
        "Population": 80088
    },
    {
        "id":5,
        "Name": "Iceland",
        "Population": 375319
    },
    {
        "id":6,
        "Name": "Malta",
        "Population": 535065
    },
    {
        "id": 7,
        "Name": "Montenegro",
        "Population": 626485
    },
    {
        "id": 8,
        "Name": "Cyprus",
        "Population": 1260138
    },
    {
        "id": 9,
        "Name": "Slovenia",
        "Population": 2119675
    },
    {
        "id": 10,
        "Name": "Bosnia and Herzegovina",
        "Population": 3210848
    },
    {
        "id": 11,
        "Name": "Croatia",
        "Population": 4008617
    },
    {
        "id": 12,
        "Name": "Ireland",
        "Population": 5056935
    },
    {
        "id": 13,
        "Name": "Norway",
        "Population": 5475020
    },
    {
        "id": 14,
        "Name": "Switzerland",
        "Population": 8796699
    },
    {
        "id": 15,
        "Name": "Hungary",
        "Population": 9604000
    },
    {
        "id": 16,
        "Name": "Belgium",
        "Population": 11686250
    },
    {
        "id": 17,
        "Name": "Poland",
        "Population": 41026068
    },
    {
        "id": 18,
        "Name": "Spain",
        "Population": 47519628
    },
    {
        "id": 19,
        "Name": "Italy",
        "Population": 58870763
    },
    {
        "id": 20,
        "Name": "France",
        "Population": 64756584
    },
    {
        "id": 21,
        "Name": "UK",
        "Population": 67736802
    },
    {
        "id": 22,
        "Name": "Germany",
        "Population": 83294633
    },
    {
        "id": 23,
        "Name": "Turkey",
        "Population": 85816199
    },
    {
        "id": 24,
        "Name": "Russia",
        "Population": 144444359
    }
]


a = random.choice(data)
b = random.choice(data)
score = 0
while True:
    print(header)
    print("Which country has higher population?")
    print(f"A: {a['Name']} or B: {b['Name']}")
    user_choice = input(": ")
    if a['Population'] > b['Population'] and user_choice.lower() =='a':
        score += 1
        print(f"Correct, score: {score}")
        b = random.choice(data)
        if b['Name'] == a['Name']:
            b = random.choice(data)
        print(20 * "\n")
    elif a['Population'] < b['Population'] and user_choice.lower() =='b':
        score += 1
        print(f"Correct, score: {score}")
        a = b
        b = random.choice(data)
        if b['Name'] == a['Name']:
            b = random.choice(data)
        print(20*"\n")
    else:
        print(f"Game over, score: {score}")
        break
