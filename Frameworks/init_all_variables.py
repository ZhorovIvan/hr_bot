from telebot import types

start_message = '''
Привет! 👋🏻
Здесь ты можешь познакомиться с Объединённым центром обслуживания компании «Уралхим» и нашими вакансиями. 
Возможно, сейчас ты не рассматриваешь предложения о работе, но полезные контакты никогда не будут лишними. 
Присоединяйся к нам на конференции Infostart — каждый день мы разыгрываем 5 крутых комплектов мерча!
'''

uralchem_message = '''
<b>Объединённый центр обслуживания «Уралхим»</b> предоставляет услуги по сервисам: IT, HR, Финансы, Закупки, - для трёх крупных холдингов: 
«Уралхим», «Уралкалий», «Галополимер». 
<b>Основная задача ОЦО</b> — квалифицированная поддержка 
бизнес-процессов холдинга.Мы обслуживаем все производственные площадки, 
торговые дома и транспортные компании холдингов. 

3 холдинга | 43 организации | 500+ сотрудников в команде 

<b>IT в ОЦО:</b>
- центр компетенций по развитию информационных систем 1С;
- центр роботизации процессов; 
- платформа корпоративных данных и глубокой аналитики;
- направление по цифровизации производственных систем; 
- центр компетенций по развитию инфраструктуры; 
- сервисный офис; 
- управление IT-активами.
'''

project_epr_message = '''
Основная цель проекта – переход с действующих учётных систем на ERP. 
Масштабы проекта – тиражирование решения на 3 холдинга. 
Команды в проекте объединены по основным 
направлениям: финансовое, операционное, интеграции и миграции.
'''

activity_info_1_part_message = '''
Приходи к нам на стенд и участвуй в наших активностях  🕹
'''

activity_info_2_part_message = '''
Выполняй задания и получай стикеры. 
Набери 6 стикеров и стань участником розыгрыша мерча от Уралхима: рюкзака, портативного зарядного устройства и бутылки для воды🎁
'''

trasling_message = '''
«Треслинг» — задорный микс «Тетриса» и армрестлинга. 
Два игрока занимают свои места за игровым столом, чтобы «побороться на руках».

Задача не в том, чтобы положить руку соперника на стол. А в том, чтобы лучше оппонента сыграть в «Тетрис» на экране, который подключен к игровому столу. 

Ты можешь проверить свои силы в «Треслинге» в течение всего дня. Победил соперника — получай 3 стикера!    
'''

find_solution_message = '''
Приходи на стенд, реши предложенные задачи и получи 3 стикера.
'''

break_system_message = '''
Ты же любишь поломать голову над кодом? 
На нашем стенде ты найдёшь интересные задачки. 
Разомни мозг и получай стикер за каждую головоломку!
'''

another_speakers_message = '''
1.  Не хватает стикеров?  Просто отправляй нам своё резюме. 
Мы получаем твоё CV, а ты дополнительный шанс на выигрыш. 
Пиши <a href="https://t.me/HR_CSC_Uralchem">Юле</a> 
2.  Подписывайся на наш телеграм-канал <a href="https://t.me/csc_uralchem">Уралхим | ОЦО</a>
3.  Пройди <a href="https://madte.st/fXbazvZ1">онлайн-викторину</a>
Переходи по ссылке и решай нашу онлайн-викторину. Удалось взять 10 из 10? Подходи к нам на стенд, показывай результат и получай стикер! 🏆
'''

jobs_message = '''
Выбери направление, которое тебя интересует:
Если есть вопросы, или ты хочешь отправить 
своё резюме, напиши <a href="https://t.me/HR_CSC_Uralchem">Юле</a>'''

architects_1c_before_zup_message = '''
•  <a href="https://perm.hh.ru/vacancy/68670804?hhtmFrom=employer_vacancies"> Главный архитектор (ТОиР)</a>
•  <a href="https://perm.hh.ru/vacancy/51021493?hhtmFrom=employer_vacancies"> Архитектор 1С ДО / ЗУП / УПП</a>
'''

developer_1c_message = '''
•  <a href="https://perm.hh.ru/vacancy/67807219?hhtmFrom=employer_vacancies"> Разработчик 1С-Битрикс(ТОиР)</a>
•  <a href="https://perm.hh.ru/vacancy/69615625?hhtmFrom=employer_vacancies"> Ведущий инженер-программист 1С</a>
'''

architects_1c_erp_message = '''
•  <a href="https://perm.hh.ru/vacancy/67168164?hhtmFrom=employer_vacancies"> Главный Архитектор 1С ERP (Блок Финансы) (ТОиР)</a>
•  <a href="https://perm.hh.ru/vacancy/66770210?hhtmFrom=vacancy_edit"> Ведущий архитектор 1С ERP (Миграция и интеграция)</a>
'''

business_analysis_message = '''
•  <a href="https://perm.hh.ru/vacancy/68423179?hhtmFrom=employer_vacancies"> Бизнес-аналитик (БУ НУ)</a>
'''

developer_1c_erp_message = '''
•  <a href="https://hh.ru/vacancy/69722521?hhtmFrom=employer_vacancies"> Ведущий инженер-программист 1С ERP</a>
'''

merch_drawing_message = '''
Среди участников конференции Infostart мы проводим розыгрыш крутого мерча: 
рюкзака, портативного зарядного устройства и бутылки для воды. 

<b>Как стать участником?</b>
Условия очень просты:
1. Приходи к нам на стенд, выполняй задания и получай стикеры. Набери 6 стикеров, заполни карточку и оставь её нашим кураторам. Каждый день в 17:00 с помощью лототрона будут выбраны 5 случайных победителей, которые получат призы от Уралхима.

2. Оставляй свои контакты в боте. Так мы сможем связаться с тобой в случае победы. Можно участвовать каждый день, можно собирать несколько карточек со стикерами.

<b>Присоединяйтесь к активностям. Удачи!</b>
'''

save_contacts_message = '''
Нажимая «Продолжить», я даю свое согласие на обработку моих персональных данных в соответствие с законом №152-ФЗ «О персональных данных» от 27.07.2006 и принимаю условия Политики конфиденциальности  
'''

write_job_interest_message = '''
<b>Напиши одну или несколько вакансий, которые тебя заинтересовали, через запятую:</b>

Архитекторы 1С ДО/ЗУП/УПП
Разработчик 1С
Архитекторы 1С ERP
Бизнес-аналитики 1С ERP
Разработчик 1С ERP
'''

choose_what_do_u_want = 'Выберете что вас интересует:'

write_bio_message = 'Давай познакомимся! Напиши свое имя и фамилию:'
write_title_message = 'Введите свою должность:'
write_number_message = 'Введите номер телефона:'
write_email_message = 'Введите адрес электронной почты:'
data_save_successfully_message = 'Данные успешно сохранены'

#Buttons for main menu
start_btn = 'Поехали🚀'
return_to_menu_btn = 'Возврат в главное меню'
save_contacts_btn = 'Оставить контакты'
return_back_to_jobs_btn = 'Вернуться ко всем вакансиям'

#Button for general menu
urlchem_btn = 'ОЦО «Уралхим»'
project_epr_btn = 'Проект ERP'
activity_info_btn = 'Активности на Infostart'
jobs_btn = 'Вакансии'
merch_drawing_btn = 'Розыгрыш мерча'

#Button for activity
trasling_btn = 'Треслинг'
find_solution_btn = 'Найди решение'
break_system_btn = 'Сломай систему'
another_speakers_btn = 'Дополнительные стикеры'
return_back_btn = 'Назад'

#Button for jobs
architects_1c_before_zup_btn = 'Архитекторы 1С ДО/ЗУП/УПП'
developer_1c_btn = 'Разработчик 1С'
architects_1c_erp_btn = 'Архитекторы 1С ERP'
business_analysis_btn = 'Бизнес-аналитики 1С ERP'
developer_1c_erp_btn = 'Разработчик 1С ERP'

#button for adding info
next_step_btn = 'Продолжить'
cancel_btn = 'Отмена'
try_again_btn = 'Исправить свои данные'
save_data_to_db_btn = 'Да, сохранить данные'


data_dict = dict()

buttons_for_gemeral_menu = [start_btn, return_to_menu_btn, cancel_btn]
buttons_dict_info_for_job = {architects_1c_before_zup_btn : architects_1c_before_zup_message,
                            developer_1c_btn : developer_1c_message,
                            architects_1c_erp_btn : architects_1c_erp_message,
                            business_analysis_btn : business_analysis_message,
                            developer_1c_erp_btn : developer_1c_erp_message}

# Init all keyboard buttons
urlchem_button = types.KeyboardButton(urlchem_btn)
project_epr_button = types.KeyboardButton(project_epr_btn)
activity_info_button = types.KeyboardButton(activity_info_btn)
jobs_button = types.KeyboardButton(jobs_btn)
merch_drawing_button = types.KeyboardButton(merch_drawing_btn)
tresling_button = types.KeyboardButton(trasling_btn)
find_solution_button = types.KeyboardButton(find_solution_btn)
break_system_button = types.KeyboardButton(break_system_btn)
another_spicers_button = types.KeyboardButton(another_speakers_btn)
return_back_to_jobs_button = types.KeyboardButton(return_back_to_jobs_btn)

# Init all Inline keyboard buttons
start_button = types.InlineKeyboardButton(start_btn, 
                                                callback_data=start_btn)
save_contacts_button = types.InlineKeyboardButton(save_contacts_btn,
                                                callback_data=save_contacts_btn)
return_to_menu_button = types.InlineKeyboardButton(return_to_menu_btn, 
                                                callback_data=return_to_menu_btn)
architects_1c_before_zup_button = types.InlineKeyboardButton(architects_1c_before_zup_btn, 
                                                callback_data=architects_1c_before_zup_btn)
developer_1c_button = types.InlineKeyboardButton(developer_1c_btn, 
                                                callback_data=developer_1c_btn)
architects_1c_erp_button = types.InlineKeyboardButton(architects_1c_erp_btn, 
                                                callback_data=architects_1c_erp_btn)
business_analysis_button = types.InlineKeyboardButton(business_analysis_btn, 
                                                callback_data=business_analysis_btn)
developer_1c_erp_button = types.InlineKeyboardButton(developer_1c_erp_btn, 
                                                callback_data=developer_1c_erp_btn)
return_to_menu_button = types.InlineKeyboardButton(return_to_menu_btn, 
                                                callback_data=return_to_menu_btn)
save_contacts_button = types.InlineKeyboardButton(save_contacts_btn, 
                                                callback_data=save_contacts_btn)
next_button = types.InlineKeyboardButton(next_step_btn, 
                                                callback_data=next_step_btn) 
try_again_button = types.InlineKeyboardButton(try_again_btn, 
                                                callback_data=try_again_btn)
save_data_to_db_button = types.InlineKeyboardButton(save_data_to_db_btn, 
                                                callback_data=save_data_to_db_btn)

