# oanda
Oanda Python

# to do
## Create a monitoring, which consist of:
a. [ ] Check if there's a running flag, if yes - exit send error message, else set running flag as true

b. Price update
[x] Pulled the latest recorded price from the database as X
[x] Pull the Oanda price from X to today as Y
~~[ ] Check if we are approaching weekends and when to start a new weekday, if true then exit~~
[ ] If false - then Insert Y into the database where not exists in X

c. [ ] Calculating the SMA, Stochastic in the database, get the database as relevant as possible

d. [ ] Check the balance, check if we have enough money to enter

e. [ ] Check if we have maxed out our positions (no more entry allowed)

f. [ ] Check if we are good to enter, check the stochastic and SMA

g. [ ] If all 3 checkers = Passed, then open a position

h. [ ] Update running flag to Completed
