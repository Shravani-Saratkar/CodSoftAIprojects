user_item_matrix = {
    'User1': {'Item1': 5, 'Item2': 3, 'Item3': 4, 'Item4': 2, 'Item5': 1},
    'User2': {'Item1': 4, 'Item2': 5, 'Item3': 3, 'Item4': 1, 'Item5': 2},
    'User3': {'Item1': 3, 'Item2': 4, 'Item3': 5, 'Item4': 2, 'Item5': 1},
    'User4': {'Item1': 2, 'Item2': 3, 'Item3': 4, 'Item4': 5, 'Item5': 1},
    'User5': {'Item1': 1, 'Item2': 2, 'Item3': 3, 'Item4': 4, 'Item5': 5}
}

def jaccard_similarity(user1, user2):
    intersection = set(user1.keys()) & set(user2.keys())
    union = set(user1.keys()) | set(user2.keys())
    return len(intersection) / len(union)

def recommend(user, num_recommendations=3):
    similar_users = {}
    for other_user in user_item_matrix:
        if other_user != user:
            similarity = jaccard_similarity(user_item_matrix[user], user_item_matrix[other_user])
            similar_users[other_user] = similarity
    similar_users = sorted(similar_users.items(), key=lambda x: x[1], reverse=True)
    recommended_items = set()
    for similar_user, _ in similar_users:
        for item, rating in user_item_matrix[similar_user].items():
            if item not in user_item_matrix[user]:
                recommended_items.add(item)
                if len(recommended_items) == num_recommendations:
                    break
        if len(recommended_items) == num_recommendations:
            break
    return list(recommended_items)

print(recommend('User1'))  


