import pickle
import string
import os

numbers = [1, 2, 3, 4, 5]
serialized_data = pickle.dumps(numbers)

print(f"serialized_data: {serialized_data}")
deserlalized_data = pickle.loads(serialized_data)
print(f"deserlalized_data: {deserlalized_data}")


def create_path(file_name):
    script_dir = os.path.dirname(os.path.realpath(__file__))
    print(f"script_dir: {script_dir}")
    return os.path.join(script_dir, file_name)

def serialize(file_name, data):
    with open(create_path(file_name), "wb") as file:
        pickle.dump(data, file)

def deserialize(file_name):
    with open(create_path(file_name), "rb") as file:
        data = pickle.load(file)
    return data

try:
    letters = [symbol for symbol in string.ascii_letters]
    file_name = "letters.txt"
    print(f"original data:\n {letters}")
    serialize(file_name, letters)
    letters_restored = deserialize(file_name)

    print(f"letters_restored:\n {letters_restored}")
except Exception as e:
    print(e)



# import json
# capitals = [
#     "Italy":"Rome"
# ]
#
# s.capitals = json.dumps(capitals)
# print(f" old capitals: {capitals}")
# print(f"serial capitals: {s.capitals}")
#
# print(join.loads(s.capitals))









