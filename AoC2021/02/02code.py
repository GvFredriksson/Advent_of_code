a = [
    "forward 8",
    "down 9",
    "up 1",
    "forward 2",
    "down 6",
    "forward 6",
    "down 5"
]

# Part 1

position = {
    "forward": 0,
    "down": 0,
    "up": 0
}
for i in a:
    x = i.split(" ")
    position[x[0]] += int(x[1])

depth = position["down"] - position["up"]
horizontal = position["forward"]

# -------------------------------------------------------------------
# Part 2

position = {
    "forward": 0,
    "depth": 0,
    "down": 0,
    "up": 0
}
for i in a:
    x = i.split(" ")
    position[x[0]] += int(x[1])
    if x[0] == "forward":
        direction = position["down"] - position["up"]
        position["depth"] += (int(x[1]) * direction)
