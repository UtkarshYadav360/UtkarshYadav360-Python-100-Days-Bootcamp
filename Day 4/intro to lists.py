# LISTS :
# list can store any data-type

# making a list
states_of_india = ["Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Hyderabad","Tripura","Uttar Pradesh","Uttarakhand","West Bengal"]

# printing the list
print(states_of_india,"\n")

# accessing items from the list using positive indexing
print(f"{states_of_india[0]} is on the 0th index.") # Andhra Pradesh
print(f"{states_of_india[5]} is on the 5th index.") # Goa
print(f"{states_of_india[12]} is on the 12th index.\n") # Madhya Pradesh

# accessing items from the list using negative indexing
print(f"{states_of_india[-1]} is the on the -1 index from the negative indexing.")
print(f"{states_of_india[-7]} is on the -7 index from the negative indexing.\n")

# changing items from the list
states_of_india[-3] = "Utkarsh Pradesh"
print(states_of_india,"\n")

# adding items to the end of the list
# .append() method is used to add single item at the end of the list
states_of_india.append("Restricted Area")
print(states_of_india,"\n")

# adding many items at the end of the list
# .extend() method is used to add multiple items to the end of the list
states_of_india.extend(["Area1","Area2","Area3"])
print(states_of_india)
