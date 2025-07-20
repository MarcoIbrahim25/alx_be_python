
Weather = input("What's the weather like today? (sunny/rainy/cold): ")

if Weather.lower() == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif Weather.lower() == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif Weather.lower() == "cold":
    print("Wear a jacket and stay warm.")
else:
    print("Sorry, I don't have recommendations for this weather.")