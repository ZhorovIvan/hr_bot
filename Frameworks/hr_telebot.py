from email import message
from platform import architecture
import threading
from Frameworks.sql_db import MySQLStorage
from telebot import types
import telebot


class TelegramBot():

    start_message = '''
Приветствуем! Здесь ты можешь познакомиться с 
Объединённым центром обслуживания компании 
«Уралхим» и нашими вакансиями. Оставь свои контакты для связи. 
Возможно, сейчас ты не рассматриваешь предложения 
о работе, но полезные контакты никогда не будут лишними.
C 6 по 8 октября мы участвуем в конференции Infostart! 
Изучай наши активности, приходи к 
нам на стенд и участвуй в ежедневном розыгрыше нашего мерча!'''

    uralchem_message = '''
Объединённый центр обслуживания «Уралхим» 
предоставляет услуги по сервисам: IT, HR, 
Финансы, Закупки, - для трёх крупных холдингов: 
«Уралхим», «Уралкалий», «Галополимер». 
<b>Основная задача ОЦО</b> — квалифицированная поддержка 
бизнес-процессов холдинга.
<b>Мы обслуживаем все производственные площадки, 
торговые дома и транспортные компании холдингов. 
В цифрах это:</b> 3 холдинга, 43 организации, более 17 000 человек. 
<b>IT:</b>
- центр компетенций по развитию информационных систем 1С;
- центр роботизации процессов; 
- платформа корпоративных данных и глубокой аналитики;
- направление по цифровизации производственных систем; 
- центр компетенций по развитию инфраструктуры; 
- сервисный офис; 
- управление IT-активами;'''

    project_epr_message = '''
Основная цель проекта – переход с действующих учётных систем на ERP. 
Масштабы проекта – тиражирование решения на 3 холдинга. 
Команды в проекте объединены по основным 
направлениям: финансовое, операционное, интеграции и миграции.'''

    activity_info_message = '''
Приходи к нам на стенд и участвуй в наших активностях.
Выполняй задания и получай стикеры. Набери 6 стикеров и 
стань участником розыгрыша мерча Уралхим: рюкзак, портативное 
зарядное устройство, бутылку для воды.
'''

    trasling_message = '''
«Треслинг» — задорный микс «Тетриса» и армрестлинга. 
Два игрока занимают свои места за игровым столом, чтобы «побороться на руках».
Задача не в том, чтобы положить руку соперника на стол. 
А в том, чтобы лучше оппонента сыграть в «Тетрис» на экране, 
который подключен к игровому столу. 
Ты можешь проверить свои силы в «Треслинге» в течение всего дня.

Победил соперника — получай 3 стикера!    
'''

    find_solution_message = '''
Приходи на стенд в зону магнитной доски, спроектируй 
решение задачи и получи 3 стикера.
'''

    break_system_message = '''
Ты же любишь поломать голову над кодом? 
На нашем стенде ты найдёшь интересные задачки. 
Разомни мозг и получай стикер за каждую головоломку!
'''

    another_speakers_message = '''
1.  Не хватает стикеров?  Просто отправляй нам своё резюме. 
Мы получаем твоё CV, а ты дополнительный шанс на выигрыш. 
Напиши  <a href="https://t.me/HR_CSC_Uralchem">Юле</a> 
2.  Подписывайся на наш телеграм-канал <a href="https://t.me/csc_uralchem">Уралхим | ОЦО</a>
3.  Пройди <a href="https://madte.st/fXbazvZ1">онлайн-викторину</a>
Переходи по ссылке и решай нашу онлайн-викторину. 
Удалось взять 10 из 10, подходи к нам на стенд, показывай результат и получай стикер.
'''

    jobs_message = '''
Выбери направление, которое тебя интересует:
Если есть вопросы, или ты хочешь отправить 
своё резюме, напиши <a href="https://t.me/HR_CSC_Uralchem">Юле</a>
'''
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
Условия очень просты
    1.  Приходи к нам на стенд, выполняй задания и получай стикеры. 
    Набери 6 стикеров, заполни карточку и оставь её нашим кураторам. 
    Каждый день в 17:00 с помощью лототрона будут выбраны 3 случайных 
    победителя, которые получат призы от Уралхима.
    2.  Оставляй свои контакты в боте. Так мы сможем связаться с тобой в случае победы.
Можно участвовать каждый день, можно собирать больше несколько карточек со стикерами.

Присоединяйтесь к активностям. Удачи!
'''

    save_contacts_message = '''
Нажимая «Продолжить», я даю свое согласие на обработку моих 
персональных данных в соответствие с законом №152-ФЗ «О персональных данных»
 от 27.07.2006 и принимаю условия Политики конфиденциальности  
'''

    write_bio_message = 'Давай познакомимся! Напиши свое имя и фамилию:'
    write_title_message = 'Введите свою должность:'
    write_number_message = 'Введите номер телефона:'
    write_email_message = 'Введите адрес электронной почты:'

    #Buttons for main menu
    start_btn = 'Старт'
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
    try_again_btn = 'Повторить ввод данных'
    save_data_to_db_btn = 'Да, сохранить данные'


    data_dict = dict()

    def __init__(self, config) -> None:
        threading.Thread.__init__(self)
        self.config = config
        self.bot = telebot.TeleBot(self.config['TELEGRAM']['token'])
        self.mysql = MySQLStorage(self.config)


    def run(self) -> None:
        @self.bot.message_handler(commands=['start'])
        def send_welcome(message) -> None:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            start_button = types.KeyboardButton(self.start_btn)

            markup.add(start_button)
            self.bot.send_message(message.chat.id,
                                self.start_message,
                                allow_sending_without_reply=False,
                                reply_markup=markup,
                                parse_mode='html')


        @self.bot.message_handler(regexp=f"({self.start_btn}|{self.return_to_menu_btn}|{self.cancel_btn})")
        def general_menu(message) -> None:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            urlchem_button = types.KeyboardButton(self.urlchem_btn)
            project_epr_button = types.KeyboardButton(self.project_epr_btn)
            activity_info_button = types.KeyboardButton(self.activity_info_btn)
            jobs_button = types.KeyboardButton(self.jobs_btn)
            merch_drawing_button = types.KeyboardButton(self.merch_drawing_btn)

            markup.add(urlchem_button,
                    project_epr_button,
                    activity_info_button,
                    jobs_button,
                    merch_drawing_button)

            self.bot.send_message(message.chat.id,
                                "Выберете что вас интересует:",
                                allow_sending_without_reply=False,
                                reply_markup=markup,
                                parse_mode='html')


        @self.bot.message_handler(regexp=self.urlchem_btn)
        def urachem_menu(message) -> None:
            # markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            # return_to_menu_button = types.KeyboardButton(self.return_to_menu_btn)
            # save_contacts_button = types.KeyboardButton(self.save_contacts_btn)
            
            button_foo = types.InlineKeyboardButton('Foo', callback_data='foo')
            button_bar = types.InlineKeyboardButton('Bar', callback_data='bar')

            keyboard = types.InlineKeyboardMarkup()
            keyboard.add(button_foo)
            keyboard.add(button_bar)


            # markup.add(return_to_menu_button,
            #         save_contacts_button)
                    
            self.bot.send_message(message.chat.id,
                                self.uralchem_message,
                                allow_sending_without_reply=False,
                                reply_markup=keyboard,
                                parse_mode='html')


        @self.bot.message_handler(regexp=self.project_epr_btn)
        def project_epr(message) -> None:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            return_to_menu_button = types.KeyboardButton(self.return_to_menu_btn)
            save_contacts_button = types.KeyboardButton(self.save_contacts_btn)
            
            markup.add(return_to_menu_button,
                    save_contacts_button)
                    
            self.bot.send_message(message.chat.id,
                                self.project_epr_message,
                                allow_sending_without_reply=False,
                                reply_markup=markup,
                                parse_mode='html')


        @self.bot.message_handler(regexp=f"({self.activity_info_btn}|{self.return_back_btn})")
        def activity_info(message) -> None:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            tresling_button = types.KeyboardButton(self.trasling_btn)
            find_solution_button = types.KeyboardButton(self.find_solution_btn)
            break_system_button = types.KeyboardButton(self.break_system_btn)
            another_spicers_button = types.KeyboardButton(self.another_speakers_btn)
            return_to_menu_button = types.KeyboardButton(self.return_to_menu_btn)
            save_contacts_button = types.KeyboardButton(self.save_contacts_btn)
            
            markup.add(save_contacts_button,
                    tresling_button,
                    find_solution_button,
                    return_to_menu_button,
                    break_system_button,
                    another_spicers_button)
                    
            self.bot.send_message(message.chat.id,
                                self.activity_info_message,
                                allow_sending_without_reply=False,
                                reply_markup=markup,
                                parse_mode='html')


        @self.bot.message_handler(regexp=self.trasling_btn)
        def trasling(message) -> None:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            return_to_menu_button = types.KeyboardButton(self.return_to_menu_btn)
            return_back_button = types.KeyboardButton(self.return_back_btn)
            save_contacts_button = types.KeyboardButton(self.save_contacts_btn)
            
            markup.add(return_to_menu_button,
                    save_contacts_button,
                    return_back_button)
                    
            self.bot.send_message(message.chat.id,
                                self.trasling_message,
                                allow_sending_without_reply=False,
                                reply_markup=markup,
                                parse_mode='html')


        @self.bot.message_handler(regexp=self.find_solution_btn)
        def find_solution(message) -> None:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            return_to_menu_button = types.KeyboardButton(self.return_to_menu_btn)
            return_back_button = types.KeyboardButton(self.return_back_btn)
            
            markup.add(return_to_menu_button,
                    return_back_button)
                    
            self.bot.send_message(message.chat.id,
                                self.find_solution_message,
                                allow_sending_without_reply=False,
                                reply_markup=markup,
                                parse_mode='html')


        @self.bot.message_handler(regexp=self.break_system_btn)
        def break_system(message) -> None:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            return_to_menu_button = types.KeyboardButton(self.return_to_menu_btn)
            return_back_button = types.KeyboardButton(self.return_back_btn)
            
            markup.add(return_to_menu_button,
                    return_back_button)
                    
            self.bot.send_message(message.chat.id,
                                self.break_system_message,
                                allow_sending_without_reply=False,
                                reply_markup=markup,
                                parse_mode='html')                        


        @self.bot.message_handler(regexp=self.another_speakers_btn)
        def another_spicers(message) -> None:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            return_to_menu_button = types.KeyboardButton(self.return_to_menu_btn)
            return_back_button = types.KeyboardButton(self.return_back_btn)
            
            markup.add(return_to_menu_button,
                    return_back_button)
                    
            self.bot.send_message(message.chat.id,
                                self.another_speakers_message,
                                allow_sending_without_reply=False,
                                reply_markup=markup,
                                parse_mode='html')  


        @self.bot.message_handler(regexp=f'({self.jobs_btn})|{self.return_back_to_jobs_btn}')
        def jobs(message) -> None:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            architects_1c_before_zup_button = types.KeyboardButton(self.architects_1c_before_zup_btn)
            developer_1c_button = types.KeyboardButton(self.developer_1c_btn)
            architects_1c_erp_button = types.KeyboardButton(self.architects_1c_erp_btn)
            business_analysis_button = types.KeyboardButton(self.business_analysis_btn)
            developer_1c_erp_button = types.KeyboardButton(self.developer_1c_erp_btn)
            return_to_menu_button = types.KeyboardButton(self.return_to_menu_btn)
            save_contacts_button = types.KeyboardButton(self.save_contacts_btn)

            markup.add(developer_1c_erp_button,
                    save_contacts_button,
                    architects_1c_before_zup_button,
                    developer_1c_button,
                    architects_1c_erp_button,
                    business_analysis_button,          
                    return_to_menu_button)
                    
            self.bot.send_message(message.chat.id,
                                self.jobs_message,
                                allow_sending_without_reply=False,
                                reply_markup=markup,
                                parse_mode='html')  


        @self.bot.message_handler(regexp=f'({self.architects_1c_before_zup_btn}|' +
                                        f'{self.developer_1c_btn}|' +
                                        f'{self.architects_1c_erp_btn}|' +
                                        f'{self.business_analysis_btn}|' +
                                        f'{self.developer_1c_erp_btn})')

        def all_jobs(message) -> None:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            return_back_to_jobs_button = types.KeyboardButton(self.return_back_to_jobs_btn)
            save_contacts_button = types.KeyboardButton(self.save_contacts_btn)
            markup.add(return_back_to_jobs_button, save_contacts_button)

            if message.text == self.architects_1c_before_zup_btn:
                message_text = self.architects_1c_before_zup_message
            elif message.text == self.developer_1c_btn:
                message_text = self.developer_1c_message
            elif message.text == self.architects_1c_erp_btn:
                message_text = self.architects_1c_erp_message
            elif message.text == self.business_analysis_btn:
                message_text = self.business_analysis_message
            else:
                message_text = self.developer_1c_erp_message    
                    
            self.bot.send_message(message.chat.id,
                                message_text,
                                allow_sending_without_reply=False,
                                reply_markup=markup,
                                parse_mode='html') 


        @self.bot.message_handler(regexp=self.merch_drawing_btn)
        def merch_drawing(message) -> None:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            return_to_menu_button = types.KeyboardButton(self.return_to_menu_btn)
            
            markup.add(return_to_menu_button)
            image = open('Files/merch.jpg', 'rb')      
            self.bot.send_photo(message.chat.id, image)        
            self.bot.send_message(message.chat.id,
                                self.merch_drawing_message,
                                allow_sending_without_reply=False,
                                reply_markup=markup,
                                parse_mode='html')  


        @self.bot.message_handler(regexp=self.save_contacts_btn)
        def save_contacts(message) -> None:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            return_to_menu_button = types.KeyboardButton(self.return_to_menu_btn)
            next_button = types.KeyboardButton(self.next_step_btn)
            markup.add(return_to_menu_button, next_button)
            doc = open('Files/Политика конфиденциальности.pdf', 'rb')
            self.bot.send_document(message.chat.id, doc)       
            self.bot.send_message(message.chat.id,
                                self.save_contacts_message,
                                allow_sending_without_reply=False,
                                reply_markup=markup,
                                parse_mode='html')  


        @self.bot.message_handler(regexp=f'({self.next_step_btn}|{self.try_again_btn})')
        def next_step_start(message) -> None:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            return_to_menu_button = types.KeyboardButton(self.return_to_menu_btn)            
            markup.add(return_to_menu_button)

            self.data_dict[message.chat.id] = []

            self.bot.send_message(message.chat.id,
                                self.write_bio_message,
                                allow_sending_without_reply=False,
                                reply_markup=markup,
                                parse_mode='html')  
            self.bot.register_next_step_handler(message, __get_bio)


        def __get_bio(message) -> None:
            __get_user_input(message, self.write_title_message, __get_title)


        def __get_title(message) -> None:
            __get_user_input(message, self.write_number_message, __get_number)


        def __get_number(message) -> None:
            __get_user_input(message, self.write_email_message, __get_email)            


        def __get_email(message) -> None:

            self.data_dict.update({message.chat.id : self.data_dict[message.chat.id] + [message.text]})
            
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            save_data_to_db_button = types.KeyboardButton(self.save_data_to_db_btn)
            try_again_button = types.KeyboardButton(self.try_again_btn)
            return_to_menu_button = types.KeyboardButton(self.return_to_menu_btn)
            markup.add(save_data_to_db_button, try_again_button,return_to_menu_button)
            self.bot.send_message(message.chat.id,
                                f'''Данные верны?
                                ФИ - {self.data_dict[message.chat.id][0]}
                                Должность - {self.data_dict[message.chat.id][1]}
                                Номер - {self.data_dict[message.chat.id][2]}
                                Электронный адрес - {self.data_dict[message.chat.id][3]}''',
                                allow_sending_without_reply=False,
                                reply_markup=markup,
                                parse_mode='html')


        def __get_user_input(message, text, func) -> None:
            if message.text == self.return_to_menu_btn:
                general_menu(message)
                return
            else:
                self.data_dict.update({message.chat.id : self.data_dict[message.chat.id] + [message.text]})

                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                return_to_menu_button = types.KeyboardButton(self.return_to_menu_btn)
                markup.add(return_to_menu_button)
            
                self.bot.send_message(message.chat.id,
                                    text,
                                    reply_markup=markup,
                                    parse_mode='html')  
            self.bot.register_next_step_handler(message, func)


        @self.bot.message_handler(regexp=self.save_data_to_db_btn)
        def save_data_to_db(message) -> None:

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            try_again_button = types.KeyboardButton(self.try_again_btn)
            return_to_menu_button = types.KeyboardButton(self.return_to_menu_btn)
            markup.add(try_again_button,return_to_menu_button)

            result = self.mysql.insert([self.data_dict[message.chat.id][0],
                                        self.data_dict[message.chat.id][1],
                                        self.data_dict[message.chat.id][2],
                                        self.data_dict[message.chat.id][3]])
            message_text = "Данные успешно сохраненны" if  result else "Ошибка, повторите ввод данных"             
            self.bot.send_message(message.chat.id,
                                message_text,
                                allow_sending_without_reply=False,
                                reply_markup=markup,
                                parse_mode='html')    


        self.bot.infinity_polling()