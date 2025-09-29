import mysql.connector

# Hàm kiểm tra PIN của thẻ ATM
def verify_pin(card_no, input_pin):
    try:
        # Kết nối MySQL (sửa user/pass theo máy bạn)
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",       # nếu có password thì điền vào
            database="atm_db"  # tên database demo
        )
        cursor = conn.cursor()

        # Truy vấn PIN từ database
        cursor.execute("SELECT pin FROM accounts WHERE card_no = %s", (card_no,))
        result = cursor.fetchone()

        if result:
            db_pin = result[0]
            return input_pin == db_pin
        else:
            return False

    except mysql.connector.Error as err:
        print(f"Lỗi kết nối: {err}")
        return False
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()

# ------------------- TEST DEMO -------------------
if __name__ == "__main__":
    card_no = input("Nhập số thẻ: ")
    pin = input("Nhập PIN: ")

    if verify_pin(card_no, pin):
        print("✅ PIN đúng, đăng nhập thành công!")
    else:
        print("❌ PIN sai hoặc không tồn tại!")
