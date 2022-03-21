InfoDb = []
# List with dictionary records placed in a list
InfoDb.append({
               "Name": "Connor",
               "FavoriteSport": "Football",
               "Team": "Broncos",
               "TopFoods":["Burger", "Sushi", "Sandwich"]
              })
InfoDb.append({
               "Name": "Jean",
               "FavoriteSport": "Basketball",
               "Team": "Magic",
               "TopFoods":["Pizza", "Hot Dogs", "Bacon"]
              })
InfoDb.append({
               "Name": "Nathan",
               "FavoriteSport": "Basketball",
               "Team": "Lakers",
               "TopFoods":["Noodles", "Rice", "Sushi"]
              })
InfoDb.append({
               "Name": "Paul",
               "FavoriteSport": "Football",
               "Team": "Lions",
               "TopFoods":["Pasta", "Pizza", "Turkey"]
              })
# for loop iterates on length of InfoDb
def print_data(n):
    print(InfoDb[n]["Name"], "loves", InfoDb[n]["FavoriteSport"], "and the", InfoDb[n]["Team"])  # using comma puts space between values
    print("\t", "Top 3 Foods: ", end="")  # \t is a tab indent, end="" make sure no return occurs
    print(", ".join(InfoDb[n]["TopFoods"]))  # join allows printing a string list with separator
    print("\t", "Favorite Food: ", end="")
    print(InfoDb[n].get("TopFoods")[0])
    print()
def for_loop():
    for n in range(len(InfoDb)):
        print_data(n)
# while loop contains an initial n and an index incrementing statement (n += 1)
def while_loop(n):
    while n < len(InfoDb):
        print_data(n)
        n += 1
    return
def recursive_loop(n):
    if n < len(InfoDb):
        print_data(n)
        recursive_loop(n + 1)
    return
def main():
  print("For loop")
  for_loop()
  print("While loop")
  while_loop(0)
  print("Recursive loop")
  recursive_loop(0)
# print data