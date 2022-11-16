from flask import current_app as app


class Cart:
    def __init__(self, uid, pid, quantity, u_price, name):
        self.uid = uid
        self.pid = pid
        self.quantity = quantity
        self.u_price = u_price
        self.name = name

    @staticmethod
    def get(uid):
        rows = app.db.execute('''
SELECT Carts.uid as uid, Carts.pid as pid, Carts.quantity as quantity, Products.price as price,
Products.name as name
FROM Carts, Products
WHERE uid = :uid and Products.id = Carts.pid
''',
                              uid=uid)
        return [Cart(*row) for row in rows]
    @staticmethod
    def updateCount(uid, pid, newValue):
        rows = app.db.execute('''
UPDATE Carts
SET quantity = :newValue
WHERE pid = :pid and uid = :uid
RETURNING uid
''',
                              uid = uid,
                              pid = pid, 
                              newValue=newValue)
        id = rows[0][0]
        return Cart.get(id)
    
    
    @staticmethod
    def delete_product(uid, pid):
       rows = app.db.execute('''
DELETE FROM Carts
WHERE pid= :pid and uid = :uid
RETURNING uid
''',
                              uid=uid,
                              pid=pid)
       id = rows[0][0]
       print(uid)
       return Cart.get(id) 