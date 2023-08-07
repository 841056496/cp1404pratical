
COLOR_CODES = {
    "AliceBlue": "#f0f8ff",
    "Coral": "#ff7f50",
    "DarkGreen": "#006400",
    "Gold": "#ffd700",
    "Gray": "#808080",
    "Lavender": "#e6e6fa",
    "Magenta": "#ff00ff",
    "Olive": "#808000",
    "SkyBlue": "#87ceeb",
    "Tomato": "#ff6347"
}

color_name = input("Enter color name: ").strip()
while color_name != "":
    color_name = color_name.title()
    try:
        print(color_name, "is", COLOR_CODES[color_name])
    except KeyError:
        print("Invalid color name")
    color_name = input("Enter color name: ").strip()
