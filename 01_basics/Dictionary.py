chai_types = {"Masala": "Spicy", "Ginger": "Zesty", "Green": "Mild"}
print(chai_types)  # {'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Mild'}
print(chai_types["Masala"])  # 'Spicy'
print(chai_types.get("Ginger"))  # 'Zesty'
print(chai_types.get("Gingery"))  # None
# chai_types["Gingery"]  # KeyError: 'Gingery'
print(chai_types)  # {'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Mild'}
chai_types["Green"] = ["Fresh"]
print(chai_types)  # {'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': ['Fresh']}
chai_types["Green"] = "Fresh"
print(chai_types)  # {'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh'}

# Iteration
for chai in chai_types:
    print(chai)
# Masala
# Ginger
# Green

for chai in chai_types:
    print(chai, chai_types[chai])
# Masala Spicy
# Ginger Zesty
# Green Fresh

for key, values in chai_types:
    for key, values in chai_types.items():
        pass
    # IndentationError: expected an indented block after 'for' statement on line 1

for key, value in chai_types.items():
    print(key, value)
# Masala Spicy
# Ginger Zesty
# Green Fresh

if "Masala" in chai_types:
    print("I have masala chai")
# I have masala chai

print(len(chai_types))  # 3
print(chai_types)  # {'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh'}
chai_types["Earl Grey"] = "Citrus"
print(chai_types)  # {'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh', 'Earl Grey': 'Citrus'}
print(chai_types.pop("Ginger"))  # 'Zesty'
print(chai_types)  # {'Masala': 'Spicy', 'Green': 'Fresh', 'Earl Grey': 'Citrus'}
print(chai_types.popitem())  # ('Earl Grey', 'Citrus')
print(chai_types)  # {'Masala': 'Spicy', 'Green': 'Fresh'}
del chai_types["Green"]
print(chai_types)  # {'Masala': 'Spicy'}

chai_types_copy = chai_types.copy()

tea_shop = {
    "chai": {"Masala": "Spicy", "Ginger": "Zesty"},
    "Tea": {"Green": "Fresh", "Black": "Strong"}
}
print(tea_shop)  # {'chai': {'Masala': 'Spicy', 'Ginger': 'Zesty'}, 'Tea': {'Green': 'Mild', 'Black': 'Strong'}}
print(tea_shop["chai"])  # {'Masala': 'Spicy', 'Ginger': 'Zesty'}
print(tea_shop["chai"]["Ginger"])  # 'Zesty'

squared_num = {x: x**2 for x in range(6)}
print(squared_num)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
squared_num.clear()
print(squared_num)  # {}

keys = ["Masala", "Ginger", "Lemon"]
print(keys)  # ['Masala', 'Ginger', 'Lemon']
default_value = "Delicious"
new_dict = dict.fromkeys(keys, default_value)
print(new_dict)  # {'Masala': 'Delicious', 'Ginger': 'Delicious', 'Lemon': 'Delicious'}
new_dict = dict.fromkeys(keys, keys)
print(new_dict)  # {'Masala': ['Masala', 'Ginger', 'Lemon'], 'Ginger': ['Masala', 'Ginger', 'Lemon'], 'Lemon': ['Masala', 'Ginger', 'Lemon']}