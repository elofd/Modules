shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300], ['педаль', 100], ['седло', 1500],
        ['рама', 12000], ['обод', 2000], ['шатун', 200], ['седло', 2700]]
detail = input('Деталь: ')
count_details = 0
sum_details = 0
for positions in shop:
        for i in positions:
                if i == detail:
                        count_details += 1
                        sum_details += positions[1]
print('Кол-во деталей', count_details)
print('Общая стоимость', sum_details)
