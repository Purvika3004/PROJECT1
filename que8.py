import pickle

num_records = int(input("Enter the number of records: "))

records = []
for _ in range(num_records):
    item_no = int(input("Enter Item No: "))
    item_name = input("Enter Item Name: ")
    qty = int(input("Enter Quantity: "))
    price = float(input("Enter Price per item: "))
    
    amount = qty * price
    
    record = {'Item No': item_no, 'Item Name': item_name, 'Quantity': qty, 'Price per item': price, 'Amount': amount}
    records.append(record)

file_name = "records.dat"
with open(file_name, 'wb') as file:
    pickle.dump(records, file)


print("Records in the file:")
with open(file_name, 'rb') as file:
    loaded_records = pickle.load(file)
    for record in loaded_records:
        print(f"Item No: {record['Item No']}")
        print(f"Item Name: {record['Item Name']}")
        print(f"Quantity: {record['Quantity']}")
        print(f"Price per item: {record['Price per item']}")
        print(f"Amount: {record['Amount']}\n")
