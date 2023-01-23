Lista_zakopow = {
    "piekarnia" : ["chleb", "pączek", "bułki"],
    "warzywniak" : ["marchew", "seler", "rukola"]
}

for k, v in Lista_zakopow.items():
    print("Idę do", k.capitalize(), "i kupuję tam", v[0].title(),v[1].title(),v[2].title() )
    
print("W sumie kupuję", sum(len(v) for v in Lista_zakopow.values()), "produktów")

print("Hiszpańska inkwizycja to najlepszy skecz")
