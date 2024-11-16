import pulp 

model = pulp.LpProblem("Contoh_Model", pulp.LpMinimize)

x = pulp.LpVariable("x", lowBound=0)
y = pulp.LpVariable("y", lowBound=0)

model += 2 * x + 3 * y, "Total_Cost"

model += x + 2 * y >= 6, "Kendala_1"
model += x - y <= 2, "Kendala_2"
model += 2 * x + 3 * y <= 12, "Kendala_3"

model.solve()

output_info = []

total_cost = pulp.value(model.objective)
output_info.append(f"Total Cost: {total_cost}")

for v in model.variables():
    try:
        variable_name = v.name
        variable_value = v.varValue
        output_info.append(f"{variable_name} = {variable_value}")
    except:
        output_info.append("Error: Couldn't find value")

for info in output_info:
    print(info)
