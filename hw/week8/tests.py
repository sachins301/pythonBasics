import hw8 as hw

# parts = hw.Parts()
# parts.reset_database()
# parts.delete(7)

inventory = hw.Inventory()
# inventory.reset_database()
inventory.add_inv("Bottled water", 84, "1.75")
inventory.update_inv(1, 16, "2.5")
# print(inventory.fetch_inv(1))
# print(inventory.delete_inv(3))
print(inventory.fetch_inv())