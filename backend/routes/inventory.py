from fastapi import APIRouter
import mysql.connector

router = APIRouter(prefix="/api", tags=["Inventory"])

@router.get("/cleaned")
def get_cleaned_inventory():
    conn = mysql.connector.connect(
        host="localhost", user="root", password="password", database="gym_inventory"
    )
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM inventory_cleaned")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result
