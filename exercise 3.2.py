shopping_list = {
    "piekarnia": ["chleb", "bułki", "pączek"],
    "warzywniak": ["marchew", "seler", "rukola"],
    "monopolowy": ["piwo"]
}

for i, j in shopping_list.items():
    print(f"Idę do {i.capitalize()} i kupuję tam: {j}")

print(f"W sumie kupuję {[sum(len(i) for i in shopping_list.values())]} towarów")