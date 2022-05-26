list1 = []
l1 = []
rev_names = {}
names = {
"Australia" : ["Olivia", "Charlotte", "Emily", "Chloe", "Ella", "Jessica", "Isabella", "Sophie", "Mia", "Emma"],
"Belgium" : ["Emma", "Marie", "Laura", "Julie", "Sarah", "Clara", "Manon", "Léa", "Lisa", "Camille"],
"Denmark" : ["Mathilde", "Emma", "Laura", "Sofie", "Freja", "Caroline", "Ida", "Sara", "Julie", "Anna"],
"France" : ["Léa", "Manon", "Emma", "Chloé", "Camille", "Océane", "Clara", "Marie", "Sarah", "Inès"],
"Hungary" : ["Anna", "Viktória", "Réka", "Vivien", "Zsófia", "Petra", "Dorina", "Fanni", "Boglárka", "Eszter"],
"Norway" : ["Emma", "Thea", "Ida", "Sara", "Julie", "Emilie", "Hanna", "Nora", "Malin", "Ingrid"],
"Portugal" : ["Maria", "Joana", "Ana", "Catarina", "Inês", "Teresa", "Isabel", "Margarida", "Carolina", "Filipa"],
"Spain" : ["Lucía", "Sofia", "Martina", "Maria", "Paula", "Julia", "Emma", "Valeria", "Daniela", "Alba"],
"Sweden" : ["Emma", "Maja", "Julia", "Alice", "Ida", "Linnéa", "Elin", "Alva", "Hanna", "Ella"],
"United States" : ["Emily", "Emma", "Madison", "Abigail", "Olivia", "Isabella", "Hannah", "Samantha", "Ava", "Ashley"],
}
d1 =
for i in names.values():
    list1.extend(i)
for i, v in enumerate(list1):
    if int(list1.count(v)) >= 3:
        l1.append(v)
rev_names = set(l1)
l1 = list(rev_names)
a, b, c = l1
print("imiona, które wystąpiły conajmniej w 3 krajach:", a, b ,c)