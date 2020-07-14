stuff = {
  "cat": "bob",
  "dog": 23,
  19: 18,
  90: "fish"
}
total = 0
for i, v in stuff.items():
    if type(v) is int:
        total += v

print(total)