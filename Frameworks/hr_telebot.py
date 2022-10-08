from platform import architecture
import threading
from telebot import types
import telebot
import re
from Frameworks.mysql_schema import *
from Frameworks.init_all_variables import *

class TelegramBot():

    def __init__(self, config) -> None:
        threading.Thread.__init__(self)
        self.config = config
        self.bot = telebot.TeleBot(self.config['TELEGRAM']['token'])


    def run(self) -> None:

        @self.bot.message_handler(commands=['start'])
        def send_welcome(message) -> None:
            __send_message_with_inlinekeyboard(message, start_message, start_button)


        @self.bot.callback_query_handler(func=lambda call: call.data in buttons_for_gemeral_menu)
        def general_menu(call) -> None:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(urlchem_button,
                    project_epr_button,
                    activity_info_button,
                    jobs_button,
                    merch_drawing_button)

            self.bot.send_message(call.message.chat.id,
                                choose_what_do_u_want,
                                allow_sending_without_reply=False,
                                reply_markup=markup,
                                parse_mode='html')


        @self.bot.message_handler(regexp=urlchem_btn)
        def urachem_menu(message) -> None:
            image = open('Files/uralchem.png', 'rb')      
            self.bot.send_photo(message.chat.id, image)
            __send_message_with_inlinekeyboard(message, uralchem_message, save_contacts_button)


        @self.bot.message_handler(regexp=project_epr_btn)
        def project_epr(message) -> None:
            image = open('Files/board.png', 'rb')      
            self.bot.send_photo(message.chat.id, image)
            __send_message_with_inlinekeyboard(message, project_epr_message, save_contacts_button)


        @self.bot.message_handler(regexp=merch_drawing_btn)
        def merch_drawing(message) -> None:
            image = open('Files/merch.jpg', 'rb')      
            self.bot.send_photo(message.chat.id, image)
            __send_message_with_inlinekeyboard(message, merch_drawing_message, save_contacts_button) 


        @self.bot.message_handler(regexp=f"({activity_info_btn}|{return_back_btn})")
        def activity_info(message) -> None:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

            markup.add(tresling_button,
                        find_solution_button,
                        break_system_button,
                        another_spicers_button)
                        
            self.bot.send_message(message.chat.id,
                                activity_info_1_part_message,
                                allow_sending_without_reply=False,
                                reply_markup=markup,
                                parse_mode='html')
            __send_message_with_inlinekeyboard(message, 
                                                activity_info_2_part_message, 
                                                save_contacts_button, return_to_menu_button)


        @self.bot.message_handler(regexp=trasling_btn)
        def trasling(message) -> None:
            __send_message_with_inlinekeyboard(message, 
                                                trasling_message,
                                                save_contacts_button, return_to_menu_button)


        @self.bot.message_handler(regexp=find_solution_btn)
        def find_solution(message) -> None:
            __send_message_with_inlinekeyboard(message, 
                                                find_solution_message,
                                                save_contacts_button, return_to_menu_button)


        @self.bot.message_handler(regexp=break_system_btn)
        def break_system(message) -> None:
            __send_message_with_inlinekeyboard(message, 
                                                break_system_message,
                                                save_contacts_button, return_to_menu_button)                      


        @self.bot.message_handler(regexp=another_speakers_btn)
        def another_spicers(message) -> None:
            __send_message_with_inlinekeyboard(message, 
                                                another_speakers_message,
                                                save_contacts_button, return_to_menu_button)


        @self.bot.message_handler(regexp=f'({jobs_btn})|{return_back_to_jobs_btn}')
        def jobs(message) -> None:
            keyboard = types.InlineKeyboardMarkup()

            keyboard.add(developer_1c_erp_button) \
                    .add(architects_1c_before_zup_button) \
                    .add(developer_1c_button) \
                    .add(architects_1c_erp_button) \
                    .add(business_analysis_button) \
                    .add(save_contacts_button)

            self.bot.send_message(message.chat.id,
                                jobs_message,
                                allow_sending_without_reply=False,
                                reply_markup=keyboard,
                                parse_mode='html')


        @self.bot.callback_query_handler(func=lambda call: call.data in buttons_dict_info_for_job.keys())
        def all_jobs(call) -> None:
            job_message_text = buttons_dict_info_for_job[call.data]
            __send_message_with_inlinekeyboard(call.message, job_message_text, save_contacts_button)


        @self.bot.callback_query_handler(func=lambda call: call.data == save_contacts_btn)
        def save_contacts(call) -> None:
            keyboard = types.InlineKeyboardMarkup()
            keyboard.add(next_button, return_to_menu_button)
            doc = open('Files/Политика конфиденциальности.pdf', 'rb')
            self.bot.send_document(call.message.chat.id, doc)       
            self.bot.send_message(call.message.chat.id,
                                save_contacts_message,
                                allow_sending_without_reply=False,
                                reply_markup=keyboard,
                                parse_mode='html')  


        @self.bot.callback_query_handler(func=lambda call: call.data in [next_step_btn, try_again_btn])
        def next_step_start(call) -> None:
            __print_to_output("start - " + str(call.message.chat.id))
            data_dict[call.message.chat.id] = []
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(return_to_menu_button) 
            self.bot.send_message(call.message.chat.id,
                                write_bio_message,
                                allow_sending_without_reply=False,
                                reply_markup=markup,
                                parse_mode='html') 
            self.bot.register_next_step_handler(call.message, __get_bio, call)


        def __get_bio(message, s_call) -> None:
            pattern = re.compile("[^0-9]+")
            __get_user_input(message, write_title_message, __get_title, s_call, pattern, __get_bio)


        def __get_title(message, s_call) -> None:
            pattern = re.compile(".+")
            __get_user_input(message, write_number_message, __get_number, s_call, pattern, __get_title)


        def __get_number(message, s_call) -> None:
            pattern = re.compile("^(\+7|8)[- _]*\(?[- _]*(\d{3}[- _]*\)?([- _]*\d){7}|\d\d[- _]*\d\d[- _]*\)?([- _]*\d){6})$")
            __get_user_input(message, write_email_message, __get_email, s_call, pattern, __get_number)


        def __get_email(message, s_call) -> None:
            pattern = re.compile("^((([0-9A-Za-z]{1}[-0-9A-z\.]{1,}[0-9A-Za-z]{1})|([0-9А-Яа-я]{1}[-0-9А-я\.]{1,}[0-9А-Яа-я]{1}))@([-A-Za-z]{1,}\.){1,2}[-A-Za-z]{2,})$")
            __get_user_input(message, write_job_interest_message, __get_job_interest, s_call, pattern, __get_email)   


        def __get_job_interest(message, s_call) -> None:
            if message.text == return_to_menu_btn:
                general_menu(s_call)
                return

            data_dict.update({message.chat.id : data_dict[message.chat.id] + [message.text]})

            message_text =  f'''
                Данные верны?
            Имя Фамилия - {data_dict[message.chat.id][0]}
            Должность - {data_dict[message.chat.id][1]}
            Номер - {data_dict[message.chat.id][2]}
            Электронный адрес - {data_dict[message.chat.id][3]}
            Интересующие вакансии - {data_dict[message.chat.id][4]}'''
            keyboard = types.InlineKeyboardMarkup()
            keyboard.add(save_data_to_db_button) \
                    .add(try_again_button) \
                    .add(return_to_menu_button)
                    
            self.bot.send_message(message.chat.id,
                                message_text,
                                allow_sending_without_reply=False,
                                reply_markup=keyboard,
                                parse_mode='html')


        @self.bot.callback_query_handler(func=lambda call: call.data == save_data_to_db_btn)
        def save_data_to_db(call) -> None:
            if len(data_dict[call.message.chat.id]) == 5:
                UserData.create(chat_id=str(call.message.chat.id),
                                bio=data_dict[call.message.chat.id][0], 
                                emp_title=data_dict[call.message.chat.id][1], 
                                emp_number=data_dict[call.message.chat.id][2], 
                                emp_email=data_dict[call.message.chat.id][3],
                                job_interest=data_dict[call.message.chat.id][4])
                __print_to_output("data saved - " + str(call.message.chat.id))                               
                del data_dict[call.message.chat.id]

                __send_message_with_inlinekeyboard(call.message, 
                                                    data_save_successfully_message, 
                                                    try_again_button, return_to_menu_button)
            else:
                __print_to_output("error - " + str(call.message.chat.id))
                __send_message_with_inlinekeyboard(call.message, 
                                                    "Ошибка,  попробуйте добавить даные снова", 
                                                    try_again_button, return_to_menu_button)


        def __get_user_input(message, text, func, s_call, pattern, cur_fun) -> None:
            
            if message.text == return_to_menu_btn:
                general_menu(s_call)
                return
            elif pattern.match(message.text) == None:
                self.bot.send_message(message.chat.id, 'Ввод некорректен, повторите')
                self.bot.register_next_step_handler(message, cur_fun, s_call)
            else:
                data_dict.update({message.chat.id : data_dict[message.chat.id] + [message.text]})
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                markup.add(return_to_menu_button)
                self.bot.send_message(message.chat.id,
                                    text,
                                    allow_sending_without_reply=False,
                                    reply_markup=markup,
                                    parse_mode='html')        
                self.bot.register_next_step_handler(message, func, s_call)


        def __send_message_with_inlinekeyboard(message, message_text, *buttons) -> None:
            keyboard = types.InlineKeyboardMarkup()
            keyboard.add(*buttons)
                    
            self.bot.send_message(message.chat.id,
                                message_text,
                                allow_sending_without_reply=False,
                                reply_markup=keyboard,
                                parse_mode='html')


        def __print_to_output(text) -> None:
            with open('output.txt', 'w') as f:
                f.write(text)


        self.bot.infinity_polling()