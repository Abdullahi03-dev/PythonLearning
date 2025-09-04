import json

def normalize_list(lst):
    return sorted([item.strip().lower() for item in lst])

# Load the original JSON file
with open("rough.json", "r", encoding="utf-8") as file:
    data = json.load(file)

seen = set()
unique_questions = []
duplicates = []

for index, item in enumerate(data):
    question = item["question"].strip().lower()
    options = normalize_list(item["options"])

    key = (question, tuple(options))  # make hashable

    if key not in seen:
        seen.add(key)
        unique_questions.append(item)
    else:
        duplicates.append((index, item["question"]))

# Save cleaned list to a new file
with open("cleaned_questions.json", "w", encoding="utf-8") as f:
    json.dump(unique_questions, f, indent=2, ensure_ascii=False)

# Print report
print("✅ Duplicate removal complete.")
print(f"🧮 Total questions originally: {len(data)}")
print(f"✅ Unique questions saved   : {len(unique_questions)}")
print(f"❌ Duplicates removed       : {len(duplicates)}")

if duplicates:
    print("\n📌 Duplicates removed:")
    for idx, question in duplicates:
        print(f"- At index {idx}: \"{question}\"")
else:
    print("🎉 No duplicates were found.")
    
    
    
    
    
    
    