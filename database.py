import sqlite3

conn = sqlite3.connect('database.db')

c = conn.cursor()

class mst_user:
    #CREATE TABLE
    c.execute("""CREATE TABLE IF NOT EXISTS Mst_user (
                user_id TEXT,
                password TEXT,
                identity TEXT,
                full_name TEXT,
                email TEXT,
                contact_number TEXT,
                address TEXT
                )""")
    
    def __init__(self, user_id, password, identity, full_name, email, contact_number, address):
        self.user_id = user_id
        self.password = password
        self.identity = identity
        self.full_name = full_name
        self.email = email
        self.contact_number = contact_number
        self.address = address

    def return_account (account):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        c.execute("SELECT * FROM Mst_user WHERE user_id = ? AND password = ?", (account.user_id, account.password))
        data = c.fetchone()
        return data

    def create_account (account):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        c.execute("INSERT INTO Mst_user VALUES (?, ?, ?, ?, ?, ?, ?)", (account.user_id, account.password, account.identity, account.full_name, account.email, account.contact_number, account.address))
        
        conn.commit()
        conn.close()
    
    def delete_account (account):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        c.execute("DELETE FROM Mst_user WHERE user_id = ? AND password = ? AND identity = ? AND full_name = ? AND email = ? AND contact_number = ? AND address = ?",
                  (account.user_id, account.password, account.identity, account.full_name, account.email, account.contact_number, account.address))
        
        conn.commit()
        conn.close()
    
    def change_account_detail (account):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        c.execute('''UPDATE Mst_user SET
                  password = ?,
                  full_name = ?,
                  email = ?,
                  contact_number = ?,
                  address = ?
                  WHERE user_id = ?''',
                  (account[1], account[3], account[4], account[5], account[6], account[0]))
        
        conn.commit()
        conn.close()
    
    def check_username(username):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        c.execute("SELECT * FROM Mst_user WHERE user_id = ?", (username,))
        data = c.fetchone()
        if data == None:
            return False
        else:
            return True

class mst_item:
    #CREATE TABLE
    c.execute('''CREATE TABLE IF NOT EXISTS Mst_item (
                item_code TEXT,
                item_name TEXT,
                category TEXT,
                price INTEGER,
                stock TEXT,
                bloom_or_addon TEXT,
                active BOOLEAN
                )''')

    def __init__(self, item_code, item_name, category, price, stock, bloom_or_addon):
        self.item_code = item_code
        self.item_name = item_name
        self.category = category
        self.price = price
        self.stock = stock
        self.bloom_or_addon = bloom_or_addon
        self.active = True
           
    def add_item(item):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        c.execute("INSERT INTO Mst_item VALUES (?, ?, ?, ?, ?, ?, ?)", (item.item_code, item.item_name, item.category, item.price, item.stock, item.bloom_or_addon, True))
        
        conn.commit()
        conn.close()
        
    def change_item_info(item):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        c.execute("UPDATE Mst_item SET item_name = ?, category = ?, price = ?, stock = ?, bloom_or_addon = ? WHERE item_code = ?",
                  (item.item_name, item.category, item.price, item.stock, item.bloom_or_addon, item.item_code))
        
        conn.commit()
        conn.close()
    
    def remove_item(item_code):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        c.execute("UPDATE Mst_item SET active = False WHERE item_code = ?", (item_code,))
        
        conn.commit()
        conn.close()
    
    def sort_item_price():
        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        c.execute("SELECT rowid, * FROM Mst_item WHERE active = True AND bloom_or_addon = 'bloom' ORDER BY price")
        data = c.fetchall()
        return data
    
    def sort_item_name():
        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        c.execute("SELECT rowid, * FROM Mst_item WHERE active = True AND bloom_or_addon = 'bloom' ORDER BY item_name")
        data = c.fetchall()
        return data
    
    def sort_item_category(category):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        c.execute("SELECT rowid, * FROM Mst_item WHERE active = True AND bloom_or_addon = 'bloom' AND category = ? ORDER BY category", (category,))
        data = c.fetchall()
        return data
    
    def search_name(name):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        c.execute("SELECT rowid, * FROM Mst_item WHERE active = True AND bloom_or_addon = 'bloom' AND item_name LIKE ?", ('%'+name+'%',))
        data = c.fetchall()
        return data
    
    def return_addon():
        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        c.execute("SELECT rowid, * FROM Mst_item WHERE active = True AND bloom_or_addon = 'add-on'")
        data = c.fetchall()
        return data
    
    def return_item(item_code):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        c.execute("SELECT * FROM Mst_item WHERE item_code = ?", (item_code,))
        data = c.fetchone()
        return data
    
    def return_itemname(item_code):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        c.execute("SELECT item_name FROM Mst_item WHERE item_code = ?", (item_code,))
        data = c.fetchone()
        if data is not None:
            item_name = data[0]
            return item_name
        else:
            return ""
        
    def check_itemcode(item_code):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        c.execute("SELECT * FROM Mst_item WHERE active = True AND item_code = ?", (item_code,))
        data = c.fetchone()
        if data is not None:
            return True
        else:
            return False

class sales_addon:
    #CREATE TABLE
    c.execute('''CREATE TABLE IF NOT EXISTS Sales_addon(
            order_id TEXT,
            addon_code TEXT
            )''')

    def __init__(self, sales_id, addon_code):
        self.sales_id = sales_id
        self.addon_code = addon_code
    
    def connect_addon(order_id, addon_code):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        c.execute("INSERT INTO Sales_addon VALUES (?, ?)", (order_id, addon_code))
        
        conn.commit()
        conn.close()
    
    def edit_addon(order_id, addon_list):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        c.execute("DELETE FROM Sales_addon where order_id = ?", (order_id,))
        for i in range(len(addon_list)):
            c.execute("INSERT INTO Sales_addon VALUES (?, ?)", (order_id, addon_list[i][1]))
        
        conn.commit()
        conn.close()

    def return_addon_code(order_id):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        c.execute("SELECT addon_code FROM Sales_addon WHERE order_id = ?", (order_id,))
        data = c.fetchall()

        return data
    
    def return_addon_name(order_id):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        c.execute("SELECT addon_name FROM Sales_addon WHERE order_id = ?", (order_id,))
        data = c.fetchall()

        return data
    
    def remove_addon(order_id):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        c.execute("DELETE FROM Sales_addon WHERE order_id = ?", (order_id,))
        
        conn.commit()
        conn.close()

class trx_sales:
    #CREATE TABLE
    c.execute('''CREATE TABLE IF NOT EXISTS Trx_sales(
            order_id TEXT,
            user_id TEXT,
            bloom_code TEXT,
            pickup_or_delivery TEXT,
            delivery_date TEXT,   
            same_day_delivery TEXT,         
            recipient_name TEXT,
            recipient_address TEXT,
            msg_for_recipient TEXT,
            total_sales INTEGER,
            order_status TEXT
            )''')

    def __init__ (self, order_id, user_id, bloom_code, pickup_or_delivery, delivery_date, same_day_delivery, recipient_name, recipient_address, msg_for_recipient, total_sales, order_status):
        self.order_id = order_id
        self.user_id = user_id
        self.bloom_code = bloom_code
        self.pickup_or_delivery = pickup_or_delivery
        self.delivery_date = delivery_date
        self.same_day_delivery = same_day_delivery
        self.recipient_name = recipient_name
        self.recipient_address = recipient_address
        self.msg_for_recipient = msg_for_recipient
        self.total_sales = total_sales
        self.order_status = order_status
    
    def add_order(order):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        c.execute("INSERT INTO Trx_sales VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (order.order_id, order.user_id, order.bloom_code, order.pickup_or_delivery, order.delivery_date, order.same_day_delivery, order.recipient_name, order.recipient_address, order.msg_for_recipient, order.total_sales, order.order_status))
        
        conn.commit()
        conn.close()

    def get_orderid():
        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        c.execute("SELECT rowid FROM Trx_sales ORDER BY rowid DESC")
        data = c.fetchone()
        if data == None:
            orderid = 1
        else:
            orderid = data[0] + 1
        return orderid
    
    def return_order(user_id):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        c.execute("SELECT * FROM Trx_sales WHERE user_id = ?", (user_id,))
        data = c.fetchall()
        return data
    
    def return_all_order():
        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        c.execute("SELECT * FROM Trx_sales")
        data = c.fetchall()
        return data
    
    def remove_order(order_id):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        c.execute("DELETE FROM Trx_sales WHERE order_id = ?", (order_id,))
        
        conn.commit()
        conn.close()
    
    def edit_status(status, order_id):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        c.execute("UPDATE Trx_sales SET order_status = ? WHERE order_id = ?", (status, order_id))
        
        conn.commit()
        conn.close()
    
    def edit_order(order):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        c.execute("""UPDATE Trx_sales SET
                  pickup_or_delivery=?,
                  delivery_date=?,
                  same_day_delivery=?,
                  recipient_name=?,
                  recipient_address=?,
                  msg_for_recipient=?,
                  total_sales=?
                  WHERE order_id = ?""",
                  (order.pickup_or_delivery, order.delivery_date, order.same_day_delivery, order.recipient_name, order.recipient_address, order.msg_for_recipient, order.total_sales, order.order_id))
        
        conn.commit()
        conn.close()

# Account
seller = mst_user("mschong", "EchoFlower", "seller", "Ms Chong", "echoflower@gmail.com", "+65 8123-4567", "461 Clementi Road, Singapore 599491")
if mst_user.check_username(seller.user_id) == False:
    mst_user.create_account(seller)

customer = mst_user("customer", "12345678", "customer", "Customer", "customer@gmail.com", "+65 1234-5678", "461 Clementi Road, Singapore 599491")
if mst_user.check_username(customer.user_id) == False:
    mst_user.create_account(customer)

# 2 initial bloom and 1 add-on
item1 = mst_item("D001", "Cheerful Love", "Romantic", "100", "Available", "bloom")
item2 = mst_item("D002", "Country Garden", "Grand Opening", "150", "Available", "bloom")
item3 = mst_item("ADD004", "Candy", "-", "3", "Available", "add-on")
if mst_item.check_itemcode("D001") == False:
    mst_item.add_item(item1)
if mst_item.check_itemcode("D002") == False:
    mst_item.add_item(item2)
if mst_item.check_itemcode("ADD004") == False:
    mst_item.add_item(item3)