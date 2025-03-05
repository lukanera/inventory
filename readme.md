# Inventory Management

ეს აპლიკაცია გამოიყენება საწყობის მენეჯმენტისთვისი.

1. BaseModel:
   - create_date : DateTimeField : auto_add_now
   - write_date : DateTimeField : auto_now
   - archived : BooleanField : default True

2. Item:
   - name : CharField
   - description : TextField
   - height : FloatFiled : nullable
   - width : FloatField : nullable
   - length : FloatField : nullable
   - weight : FloatField : nullable
   - category : m2o -> Category
   - stock_qty : PositiveInteger
   - expiration_date : DateField : nullable
   - barcode : CharField : max_length 13 : auto generated : unique
   
ვალიდაციები:
name მინიმალური სიმბოლოების რაოდენობა იყოს 5
description მინიმალური სიტყვების რაოდენობა 2
width, lenth, weight არ შეიძლება იყოს უარყოფითი
experation_date სავალდებულოა თუ cateogry.name-ში ურევია სიტყვა food ან drink
   
3. Category:
    - name : CharField

### EndPoints
- api/about : GET
- api/products : GET
- api/products : POST
- api/products/id : GET
- api/products/id : POST
- api/products/id : PUT
- api/products/id : PATCH
- api/products/id : DELETE
- api/categories : GET
- api/categories : POST
- api/categories/id : GET
- api/categories/id : POST
- api/categories/id : PUT
- api/categories/id : PATCH
- api/categories/id : DELETE
- api/categories/id/products : GET
- api/categories/id/products : POST
- api/categories/id/products/id : GET
- api/categories/id/products/id : POST
- api/categories/id/products/id : PUT
- api/categories/id/products/id : PATCH
- api/categories/id/products/id : DELETE

