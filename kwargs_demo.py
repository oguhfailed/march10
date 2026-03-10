def greet(**kwargs):
    """kwargs lets you pass any number of keyword arguments."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print("=== Basic kwargs ===")
greet(name="Alice", age=30, city="New York")

print("\n=== kwargs in a real use case ===")
def create_profile(**kwargs):
    profile = {}
    profile.update(kwargs)
    return profile

user = create_profile(username="bob", email="bob@example.com", role="admin")
print(user)

print("\n=== Combining normal args with kwargs ===")
def order(item, quantity, **extras):
    print(f"Item: {item}, Qty: {quantity}")
    if extras:
        print(f"Extras: {extras}")

order("Pizza", 2, size="large", crust="thin", extra_cheese=True)

print("\n=== Passing a dict as kwargs using ** ===")
settings = {"color": "blue", "font": "Arial", "size": 14}

def apply_settings(**kwargs):
    for setting, val in kwargs.items():
        print(f"  {setting} = {val}")

apply_settings(**settings)
