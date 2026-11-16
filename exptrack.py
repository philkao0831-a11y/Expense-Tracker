expenses = []
while True:
  item = input("請輸入消費項目 (輸入 q 結束記帳):")
  if item.lower() == "q":
    break
  else:
    amount = int(input("請問你花了多少錢? "))
    record = {"item":item, "amount":amount}
    expenses.append(record)
total = 0
for record in expenses:
  total += record["amount"]
  print(f"- {record['item']}: {record['amount']} 元")
print(f"總花費：{total} 元")
