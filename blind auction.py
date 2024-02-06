auction_name_price = []

def add_new_client():
    new_client = {}
    new_client["Name:"] = input("What is your name?\n")
    new_client["Price:"] = int(input("What is your price?\n"))
    auction_name_price.append(new_client)
add_new_client()
another_client = input("Is there any other? Type 'yes' or 'no'\n")
while another_client.lower() == "yes":
    add_new_client()
    another_client = input("Is there any other? Type 'yes' or 'no'\n")


for client in auction_name_price:
    print(client['Price'])
    # print(f"Price: {client['Price']}")

