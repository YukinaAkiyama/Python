price: dict = {1: 399, 2: 4369, 3: 539, 4: 288, 5: 109, 6: 749, 7: 235, 8: 190, 9: 99, 10: 1000}
price_ex: dict = {}
MinPrice = eval(input("输入商品最低价："))
MaxPrice = eval(input("输入商品最高价："))
for k, v in price.items():
    if MinPrice <= v <= MaxPrice:
        price_ex[k] = v
print("筛选结果：\n", price_ex)
print("请选择排序方式：\n"
      "1.升序\n"
      "2.降序\n"
      "3.退出")
choice = eval(input())
if choice == 1:
    upper = sorted(price_ex.items(), key=lambda x: x[1], reverse=False)
    print("结果：\n", upper)
elif choice == 2:
    downer = sorted(price_ex.items(), key=lambda x: x[1], reverse=True)
    print("结果: \n", downer)
elif choice == 3:
    exit()
