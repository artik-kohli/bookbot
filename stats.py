def word_count(content: str):
    return len(content.split())

def get_character_count(content: str):
    char_count = dict()
    for c in content:
        n = c.lower()
        char_count[n] = char_count.get(n, 0) + 1
    return char_count

def get_sorted_dict_list(char_dict: dict):
    final_list = []
    for key in char_dict:
        final_list.append({
            "char": key,
            "num": char_dict[key]
        })
    final_list = sorted(final_list, key=lambda x: -x["num"])
    return final_list