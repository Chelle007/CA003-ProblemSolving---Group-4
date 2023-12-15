import database

#BLOOM
def readitem_txt(file):
    items_each = []
    with open(file, "r+") as pf :
        for line in pf :
            line = line.replace('\n', '')
            items = line.split(",")
            items_each.append(items)
    #return list
    return items_each

def additem_txt(file, item):
    items_each = []
    with open(file, "r+") as pf :
        for line in pf :
            items = line.split(",")
            items_each.append(items)

        new_item = [item.item_code, item.item_name, item.category, str(item.price), item.stock]
        with open(file, "a") as pf :
            pf.write("\n" + ",".join(new_item))

def removeitem_txt(file, item_code):
    items_each = []
    with open(file, "r+") as pf :
        for line in pf :
            items = line.split(",")
            items_each.append(items)
    with open(file, "w") as pf :
        for data in items_each :
            if data[0] != item_code :
                pf.write(",".join(data))

def edititem_txt(file, item):
    items_each = []
    with open(file, "r+") as pf :
        for line in pf :
            items = line.split(",")
            items_each.append(items)

        for i in range(len(items_each)) :
            if items_each[i][0] == item.item_code:
                items_each[i][1] = item.item_name
                items_each[i][2] = item.category
                items_each[i][3] = str(item.price)
                if i == len(items_each)-1:
                    items_each[i][4] = item.stock
                else:
                    items_each[i][4] = item.stock + "\n"

        with open(file, "w") as pf :
            for i in range(len(items_each)) :       
                pf.write(",".join(items_each[i]))

#ADD-ON
def readaddon_txt(file):
    addons_each = []
    with open(file, "r+") as pf :
        for line in pf :
            line = line.replace('\n', '')
            addons = line.split(",")
            addons_each.append(addons)
    #return list
    return addons_each

def addaddon_txt(file, item):
    items_each = []
    with open(file, "r+") as pf :
        for line in pf :
            items = line.split(",")
            items_each.append(items)

        new_item = [item.item_code, item.item_name, str(item.price), item.stock]
        with open(file, "a") as pf :
            pf.write("\n" + ",".join(new_item))

def removeaddon_txt(file, item_code):
    items_each = []
    with open(file, "r+") as pf :
        for line in pf :
            items = line.split(",")
            items_each.append(items)
    with open(file, "w") as pf :
        for data in items_each :
            if data[0] != item_code :
                pf.write(",".join(data))

def editaddon_txt(file, item):
    items_each = []
    with open(file, "r+") as pf :
        for line in pf :
            items = line.split(",")
            items_each.append(items)

        for i in range(len(items_each)) :
            if items_each[i][0] == item.item_code:
                items_each[i][1] = item.item_name
                items_each[i][2] = str(item.price)
                if i == len(items_each)-1:
                    items_each[i][3] = item.stock
                else:
                    items_each[i][3] = item.stock + "\n"

        with open(file, "w") as pf :
            for i in range(len(items_each)) :       
                pf.write(",".join(items_each[i]))