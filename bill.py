import time as t
import mysql.connector
def bill():
    conn = mysql.connector.connect(
    host="localhost",
    user="root",        # apna username
    password="Mansi@123",    # apna password
    database="orders"   # apna database
)
    cursor= conn.cursor()
    order_id=int(input("Enter order id: "))
    product_name=input("Enter product name: ")
    p_price=float(input("Enter product price: "))
    p_quantity=int(input("Enter product quantity: "))
    amount=p_price*p_quantity

    sql = "INSERT INTO Products (order_id,product_name,p_price,p_quantity,amount) VALUES (%s,%s,%s,%s,%s)"
    values = (order_id,product_name,p_price,p_quantity,amount)
    cursor.execute(sql,values)
    conn.commit()
    print("✅ Data successfully inserted into Products table!")

    id=str(order_id)
    ordertime=t.ctime()
    x=open(id,"w")

    y=x.write(f'''         Bill for {id}
-------------------------------------
         Order Id: {order_id}
    Product name: {product_name}
        Quantity: {p_quantity}
-------------------------------------
Final amount: {amount}
-------------------------------------
{ordertime}
''')
    x.close()
    cursor.close()
    conn.close()
bill()