"""5. Manchester United FC Talent Acquisition System:

The Manchester United FC is in search of new talents to enhance its player roster.
The head coach aims to recruit two forwards, two midfielders, a right-back, a defender, and a goalkeeper.
To achieve this, the club needs to sell some players to fund these new signings. Develop a system to assist
the head coach in choosing which players can be sold based on their market price, salary, position,
and performance within the club.

# Algorithm #

Select buy
    1. position
    2. perfo
    3. price / salary

Select sell
    1. same position to buy
    2. perfo
    3. high salary
    4. high price
    if sell-4 enouthg to pay buy-3
        end
    else:
        repeat sell to select other player.

-------------------------------------------------------------------------------------"""