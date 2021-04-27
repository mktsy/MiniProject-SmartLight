
from vault_for_app import(
    checkState,
    updateOneValueForAppCollection
)

check = checkState(1)

print(type(check))
print(check)

old_value = {"lightNumber": 1}
new_value = {"$set": {"state": True}}

updateOneValueForAppCollection(old_value, new_value)
