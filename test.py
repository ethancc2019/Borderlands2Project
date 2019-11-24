import pymysql
import xlrd


def connectToDB():
    db = pymysql.connect(
        host="ethan.cikeys.com",
        user="ethancik_root",
        passwd="Rebels19!",
        database="ethancik_borderlands")
    cursor = db.cursor()
    return cursor


def getManufacturerId(manu_name_param):
    switcher = {
        'Bandit': 1,
        'Dahl': 2,
        'Hyperion': 3,
        'Jakobs': 4,
        'Maliwan': 5,
        'Tediore': 6,
        'Torgue': 7,
        'Vladof': 8,
        'Shredifier': 9
    }
    return switcher.get(manu_name_param, 'No Manufacturer')


if __name__ == "__main__":
    cursor = connectToDB()

    wb = xlrd.open_workbook('/Users/EthanCC/Desktop/Borderlands2Project/CSVs/Master Weapon List.xlsx')
    sheet = wb.sheet_by_index(0)
    counter = 0
    for i in range(sheet.nrows):
        manu_id_p = getManufacturerId(sheet.cell_value(i,4))

        # split[0] = sheet.cell_values(i,0)
        # split[1] = sheet.cell_values(i,1)
        # split[2] = sheet.cell_values(i,2)
        # spit[3] = sheet.cell_values(i,3)
        # split[4] = sheet.cell_values(i,4)
        # split[5] = sheet.cell_values(i,5) , damage type
        # split[6] = dropped by sheet.cell_values(i,6)
        # split[7] = min Task, sheet.cell_value(i,7)
        # split[8] = location, sheet.cell_value(i,8)
        # split[9] = rarity, sheet.cell_value(i,9)

        query = "insert into gun(manu_id, gun_name, type, damage_type, dropped_by, minimum_task, rarity, " \
                "manufacturer, perk, location, dlc) value(%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s)"
        cursor.execute(query, (manu_id_p,
                               sheet.cell_value(i,2),
                               sheet.cell_value(i,1),
                               sheet.cell_value(i,5),
                               sheet.cell_value(i,6),
                               sheet.cell_value(i, 7),
                               sheet.cell_value(i,9),
                               sheet.cell_value(i,4),
                               sheet.cell_value(i,3),
                               sheet.cell_value(i,8),
                               sheet.cell_value(i,0)))
        cursor.connection.commit()
        print('Finished: ' + sheet.cell_value(i,4))
