import requests
import json

response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)

todos_by_user = {}

for todo in todos:
    try:
        if todo["completed"]:
            todos_by_user[todo["userId"]] += 1
    except KeyError:
        todos_by_user[todo["userId"]] = 1
    pass
# Create a sorted list of (userid, num_complete) pairs
# Descending Sort
# x is stand for each item in the tuple
top_users = sorted(todos_by_user.items(), key=lambda x: x[1], reverse=True)

# Get the maxium number of complete TODOS.
max_complete = top_users[0][1]

# print(todos_by_user)
# print(max_complete)

# Create a list of all users who have completed
# the maxium number of TODOs.

users = []

# Unpack the tuple
for user, num_complete in top_users:
    if num_complete < max_complete:
        break

    users.append(str(user))
print(top_users)
max_users = " and ".join(users)  # The string is the seperator.

# Write a function to filter out completed TODOs
# of users with max completed TODOs
def keep(todo):
    is_complete = todo["completed"]
    has_max_count = str(todo["userId"]) in users
    return is_complete and has_max_count

# Write filtered TODOs to file.
with open("filtered_data_file.json", "w") as output:
    filtered_todo = list(filter(keep, todos))
    json.dump(filtered_todo, output, indent=2)



s = "s" if len(users) < 1 else ""
print(f"user{s} {max_users} completed {max_complete} TODOs")
