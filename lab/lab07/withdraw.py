import mysql.connector
import hashlib

def verify_pin(card_no, pin):
    conn = mysql.connector.connect(user="root", password="123456", database="atm_demo")
    cur = conn.cursor()
    cur.execute("SELECT pin_hash FROM cards WHERE card_no=%s", (card_no,))
    row = cur.fetchone()
    conn.close()
    return row and row[0] == hashlib.sha256(pin.encode()).hexdigest()

def withdraw(card_no, amount):
    conn = mysql.connector.connect(user="root", password="123456", database="atm_demo")
    cur = conn.cursor()
    try:
        conn.start_transaction()
        cur.execute("""
            SELECT a.account_id, a.balance
            FROM accounts a
            JOIN cards c ON a.account_id = c.account_id
            WHERE c.card_no=%s FOR UPDATE
        """, (card_no,))
        row = cur.fetchone()
        if not row:
            raise Exception("Card not found")
        account_id, balance = row

        if balance < amount:
            raise Exception("Insufficient funds")

        # Update balance
        cur.execute("UPDATE accounts SET balance=balance-%s WHERE account_id=%s", (amount, account_id))

        # Insert transaction log
        cur.execute("""
            INSERT INTO transactions(account_id, card_no, atm_id, tx_type, amount, balance_after)
            VALUES(%s, %s, 1, 'WITHDRAW', %s, %s)
        """, (account_id, card_no, amount, balance - amount))

        conn.commit()
        print(f"Withdraw {amount} success. New balance: {balance - amount}")
    except Exception as e:
        conn.rollback()
        print("Error:", e)
    finally:
        conn.close()

if __name__ == "__main__":
    card_no = "1234567890"
    pin = "1234"

    if verify_pin(card_no, pin):
        withdraw(card_no, 1000)
    else:
        print("Invalid PIN")
