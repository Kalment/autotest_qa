first_name = 'Александр'
second_name = 'Паркаренко'
full_work_experience_in_Tensor = '4 года 10 месяцев'
first_position = 'Специалист по обслуживанию программного обеспечения'
first_position_experience = '11 месяцев'
second_position = 'Инженер-тестировщик'
second_position_experience = '3 года 11 месяцев'
current_category = '2 категории'

resume = f"""
Меня зовут %s %s. 
Работаю в компании Тензор уже %s. 
Начиная с должности %s, где проработал %s - смог перейти на должность %s, где работаю уже %s. 
За это время дорос до %s, на которой не хотелось бы останавливаться.
На данный курс записался для того, что бы повысить свои навыки в яп python и начать полноценно поддерживать автотесты
""" % (second_name, first_name, full_work_experience_in_Tensor, first_position, first_position_experience,
       second_position, second_position_experience, current_category)

print(resume)