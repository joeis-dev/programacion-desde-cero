# Requierement: Understand of binary numeric system. 

# 2 (00000010)
# 3 (00000011)
print(f"2 & 3: {2 & 3}")

# 8 (00001000)
# 4 (00000100)
print(f"8 | 4: {8 | 4}")

# 6 (00000110)
# 7 (00000111)
print(f"6 ^ 7: {6 ^ 7}")

# 12 (00001100)
# 5  
print(f"12 >> 5: {12 >> 5}")

# 3 (00000011)
# 2  
print(f"3 << 2: {3 << 2}")

# Binary representation using bin() from python
backyard_lights = 0b0110
desired_state = 0b1001
print(f"Backyard lights status: {bin(backyard_lights)}")
print(f"Backyard lights status: {bin(backyard_lights & desired_state)}")
