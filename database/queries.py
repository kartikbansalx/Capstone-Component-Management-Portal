from database.db import get_connection

def get_components():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT ComponentID, ComponentName, Quantity FROM Components")
    data = cur.fetchall()
    conn.close()
    return data

def add_component(name, category, desc, spec, qty, cond, cost, vendor, minstock, consumable):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO Components (
            ComponentName, Category, Description, Specification,
            Quantity, ComponentCondition, UnitCost, VendorID, MinStockLevel, IsConsumable
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (name, category, desc, spec, qty, cond, cost, vendor, minstock, consumable))
    conn.commit()
    conn.close()

def get_teams():
 conn = get_connection()
 cur = conn.cursor()
 cur.execute("SELECT TeamID, TeamName FROM Teams")
 data = cur.fetchall()
 conn.close()
 return data

def record_lending(component_id, team_id, qty, remarks):
 conn = get_connection()
 cur = conn.cursor()
 cur.execute("""
INSERT INTO ComponentLending(ComponentID, TeamID, Quantity, Remarks, LendDate, DueDate)
       VALUES (%s, %s, %s, %s, NOW(), DATE_ADD(NOW(), INTERVAL 30 DAY))
    """, (component_id, team_id, qty, remarks))
 conn.commit()
 conn.close()

def get_lending_records():
 conn = get_connection()
 cur = conn.cursor()
 cur.execute("""
 SELECT L.LendingID, C.ComponentName, T.TeamName,
 L.Quantity, L.LendDate, L.DueDate, L.Remarks
 FROM ComponentLending L
 JOIN Components C ON L.ComponentID = C.ComponentID
 JOIN Teams T ON L.TeamID = T.TeamID
 ORDER BY L.LendingID DESC
 """)
 data = cur.fetchall()
 conn.close()
 return data

def submit_reimbursement(component_id, team_id, requested, method, authority):
 conn = get_connection()
 cur = conn.cursor()
 cur.execute("""
 INSERT INTO Reimbursements
 (ComponentID, TeamID, ReimbursementStatus,
 ApprovalAuthority, PaymentMethod, RequestedAmount)
 VALUES (%s, %s, 'Pending', %s, %s, %s)
 """, (component_id, team_id, authority, method, requested))
 conn.commit()
 conn.close()

def get_reimbursements():
 conn = get_connection()
 cur = conn.cursor()
 cur.execute("""
 SELECT R.ReimbursementID, C.ComponentName, T.TeamName,
 R.ReimbursementStatus, R.RequestedAmount, R.ApprovedAmount,
 R.PaymentMethod, R.ApprovalAuthority
 FROM Reimbursements R
 JOIN Components C ON R.ComponentID = C.ComponentID
 JOIN Teams T ON R.TeamID = T.TeamID
 ORDER BY R.ReimbursementID DESC
 """)
 data = cur.fetchall()
 conn.close()
 return data
