# Planet gravitational acceleration in m/s^2 (as integers)
planet_gravity = {
    'Mercury': 3.7,
    'Venus': 8.87,
    'Earth': 9.81,
    'Mars': 3.71,
    'Jupiter': 24.79,
    'Saturn': 10.44,
    'Uranus': 8.69,
    'Neptune': 11.15,
    'Pluto': 0.62
}

# Display gravitational accelerations as integers
print("Gravitational acceleration on each planet in the solar system (rounded to nearest integer in m/s^2):")
for planet, gravity in planet_gravity.items():
    print(f"{planet}: {round(gravity)} m/s^2")
