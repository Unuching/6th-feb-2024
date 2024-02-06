auction_name_price = []

def add_new_client():
    new_client = {}
    new_client["Name"] = input("What is your name? ")
    new_client["Price"] = float(input("What is your price? "))
    auction_name_price.append(new_client)

# Initial client
add_new_client()

another_client = input("Is there any other? Type 'yes' or 'no': ")
while another_client.lower() == "yes":
    add_new_client()
    another_client = input("Is there any other? Type 'yes' or 'no': ")

print("\nAuction Participants and Prices:")
for client in auction_name_price:
    print(f"Name: {client['Name']}, Price: {client['Price']}")

# You can now further process the auction_name_price list as needed.
