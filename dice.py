import random

def roll_three_dice():
    return sum(random.randint(1, 6) for _ in range(3))

def dalembert_system(initial_cash, base_unit, target_profit_pct, target_loss_pct):
    current_cash = initial_cash
    current_bet = base_unit
    total_profit = 0
    total_loss = 0
    session_results = []
    
    print("$Bet\tResult\t$Profit / Loss\t$Total Cash")
    print("-----------------------------------------")
    
    while True:
        # Simulating rolling three dice
        dice_sum = roll_three_dice()
        
        # Checking if the result falls in the "small" range (4-10)
        if 4 <= dice_sum <= 10:
            result = 'Win'
        else:
            result = 'Loss'
        
        session_results.append(result)
        
        if result == 'Win':
            total_profit += current_bet
            current_cash += current_bet
            current_bet -= base_unit
        elif result == 'Loss':
            total_loss += current_bet
            total_profit -= current_bet
            current_cash -= current_bet
            current_bet += base_unit

        if current_bet == 0:
            current_bet = base_unit

        print("{}\t{}\t{}\t\t{}".format(current_bet, result, total_profit, current_cash))

        # Check if target profit or target loss is reached
        if current_cash >= initial_cash * ((target_profit_pct / 100) + 1) or current_cash <= initial_cash * (1 - (target_loss_pct / 100)):
            print("Target profit/loss reached. Exiting...")
            break
    
    print("-----------------------------------------")
    print("Total profit/loss for the session: ${}".format(current_cash - initial_cash))

initial_cash = 300  # Initial cash in dollars
base_unit = 20  # Base unit in dollars
target_profit_pct = 30  # Target profit percentage
target_loss_pct = 20  # Target loss percentage
print("The target profit was ${} and the target loss was ${}".format(initial_cash * ((target_profit_pct / 100) + 1), initial_cash * (1 - (target_loss_pct / 100))))

dalembert_system(initial_cash, base_unit, target_profit_pct, target_loss_pct)
