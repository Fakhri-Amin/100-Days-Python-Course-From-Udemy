import prettytable

table = prettytable.PrettyTable()

table.add_column(
    "Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

table.align = "l"

# num_list = []
# for i in range(1, 101):
#     num_list.append(i)
# table.add_column("Number", num_list)

print(table)
