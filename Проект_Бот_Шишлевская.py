import telebot
from telebot import types
import random

bot = telebot.TeleBot('5663832891:AAEc_3g7Cpk-CH6z43fTLdiBksodOhi3lvc')
partOfTheWorld = [[]]                     
random_index = 0

Mas_Europe = [['Нидерланды', 'Амстердам'], ['Кипр', 'Никосия'], ['Андорра', 'Андорра-ла-Велья'], ['Греция', 'Афины'], ['Сербия', 'Белград'], ['Германия', 'Берлин'], ['Швейцария', 'Берн'], ['Словакия', 'Братислава'], ['Бельгия', 'Брюссель'], ['Венгрия', 'Будапешт'], ['Румыния', 'Бухарест'], ['Лихтенштейн', 'Вадуц'], ['Мальта', 'Валлетта'], ['Польша', 'Варшава'], ['Ватикан', 'Ватикан'], ['Австрия', 'Вена'], ['Литва', 'Вильнюс'], ['Ирландия', 'Дублин'], ['Хорватия', 'Загреб'], ['Украина', 'Киев'], ['Молдавия', 'Кишинев'], ['Дания', 'Копенгаген'], ['Португалия', 'Лиссабон'], ['Великобритания', 'Лондон'], ['Словения', 'Любляна'], ['Люксембург','Люксембург'], ['Испания', 'Мадрид'], ['Беларусь', 'Минск'], ['Монако', 'Монако'], ['Россия', 'Москва'], ['Норвегия', 'Осло'], ['Франция', 'Париж'], ['Черногория', 'Подгорица'], ['Чехия', 'Прага'], ['Исландия', 'Рейкьявик'], ['Латвия', 'Рига'], ['Италия', 'Рим'], ['Сан-Марино', 'Сан-Марино'], ['Босния и Герцеговина', 'Сараево'], ['Северная Македония', 'Скопье'], ['Болгария', 'София'], ['Швеция', 'Стокгольм'], ['Эстония', 'Таллин'], ['Албания', 'Тирана'], ['Финляндия', 'Хельсинки'], ['Косово', 'Приштина']]
Mas_Asia = [['OAЭ', 'Абу-Даби'], ['Иордания', 'Амман'], ['Турция', 'Анкара'], ['Казахстан', 'Астана'], ['Туркменистан', 'Ашхабад'], ['Ирак', 'Багдад'], ['Азербайджан', 'Баку'], ['Таиланд', 'Бангкок'], ['Бруней', 'Бандар-Сери-Бегаван'], ['Ливан', 'Бейрут'], ['Киргизия', 'Бишкек'], ['Лаос', 'Вьентьян'], ['Бангладеш', 'Дакка'], ['Сирия', 'Дамаск'], ['Индия', 'Нью-Дели'], ['Индонезия', 'Джакарта'], ['Восточный Тимор', 'Дили'], ['Катар', 'Доха'], ['Таджикистан', 'Душанбе'], ['Армения', 'Ереван'], ['Израиль', 'Иерусалим'], ['Пакистан', 'Исламабад'], ['Афганистан', 'Кабул'], ['Непал', 'Катманду'], ['Малайзия', 'Куала-Лумпур'], ['Мальдивы', 'Мале'], ['Бахрейн', 'Манама'], ['Филиппины', 'Манила'], ['Оман', 'Маскат'], ['Мьянма', 'Нейпьидо'], ['Китай', 'Пекин'], ['Камбоджа', 'Пномпень'], ['КНДР', 'Пхеньян'], ['Йемен', 'Сана'], ['Республика Корея', 'Сеул'], ['Сингапур', 'Сингапур'], ['Узбекистан', 'Ташкент'], ['Грузия', 'Тбилиси'], ['Иран', 'Тегеран'], ['Япония', 'Токио'], ['Бутан', 'Тхимпху'], ['Монголия', 'Улан-Батор'], ['Вьетнам', 'Ханой'], ['Шри-Ланка', 'Шри-Джаяварденепура-Котте'], ['Кувейт', 'Эль-Кувейт'], ['Саудовская Аравия','Эр–Рияд']]
Mas_Africa = [['Алжир', 'Алжир'], ['Ангола', 'Луанда'], ['Бенин', 'Порто-Ново'], ['Ботсвана', 'Габороне'], ['Буркина-Фасо', 'Уагадугу'], ['Бурунди', 'Гитега'], ['Габон', 'Либревиль'], ['Гамбия', 'Банжул'], ['Гана', 'Аккра'], ['Гвинея', 'Конакри'], ['Гвинея-Бисау', 'Бисау'], ['Демократическая республика Конго', 'Киншаса'], ['Джибути', 'Джибути'], ['Египет', 'Каир'], ['Замбия', 'Лусака'], ['Западная Сахара', 'Эль-Аюн'], ['Зимбабве', 'Хараре'], ['Кабо-Верде', 'Прая'], ['Камерун', 'Яунде'], ['Кения','Найроби'], ['Коморы', 'Морони'], ['Конго', 'Браззавиль'], ['Лесото', 'Масеру'], ['Либерия', 'Монровия'], ['Ливия', 'Триполи'], ['Маврикий', 'Порт-Луи'], ['Мавритания', 'Нуакшот'], ['Мадагаскар', 'Антананариву'], ['Малави', 'Лилонгве'], ['Мали', 'Бамако'], ['Марокко','Рабат'], ['Мозамбик', 'Мапуту'], ['Намибия', 'Виндхук'], ['Нигер', 'Ниамей'], ['Нигерия', 'Абуджа'], ['Остров Святой Елены', 'Джеймстаун'], ['Реюньон', 'Сен-Дени'], ['Руанда', 'Кигали'], ['Сан-Томе и Принсипи', 'Сан-Томе'], ['Эсватини', 'Мбабане'], ['Сейшельские острова', 'Виктория'], ['Сенегал', 'Дакар'], ['Сомали', 'Могадишо'], ['Судан', 'Хартум'], ['Сьерра-Леоне', 'Фритаун'], ['Танзания', 'Додома'], ['Того', 'Ломе'], ['Тунис', 'Тунис'], ['Уганда', 'Кампала'], ['ЦАР', 'Банги'], ['Чад', 'Нджамена'], ['Экваториальная Гвинея', 'Малабо'], ['Эритрея', 'Асмэра'], ['Эфиопия', 'Аддис-Абеба'], ['ЮАР', 'Претория'], ['Южный Судан', 'Джуба']]
Mas_America = [['Парагвай','Асуньсон'], ['Сент-Китс и Невис','Бастер'], ['Белиз', 'Бельмопан'], [ 'Колумбия', 'Богота'], [ 'Бразилия', 'Бразилиа'], [ 'Барбадос', 'Бриджтаун'], ['Аргентина', 'Буэнос-Айрес'], [ 'США', 'Вашингтон'], ['Куба', 'Гавана'], [ 'Гватемала', 'Гватемала'], [ 'Гайана', 'Джорджтаун'], ['Венесуэла', 'Каракас'], ['Сент-Люсия', 'Кастри'], [ 'Сент-Винсент и Гренадин', 'Кингстаун'], [ 'Ямайка', 'Кингстон'], ['Эквадор', 'Кито'], ['Перу', 'Лима'], ['Никарагуа', 'Манагуа'],['Мексика', 'Мехико'], ['Уругвай', 'Монтевидео'], ['Багамские Острова', 'Нассау'], ['Канада', 'Оттава'], ['Панама', 'Панама'],['Суринам' ,'Парамарибо'], ['Гаити', 'Порт-о-Пренс'], ['Тринидад и Тобаго', 'Порт-оф-Спейн'], ['Доминика', 'Розо'], ['Сальвадор', 'Сан-Сальвадор'], ['Коста-Рика', 'Сан-Хосе'],  ['Доминиканская Республика', 'Санто-Доминго'], ['Чили', 'Сантьяго'], ['Антигуа и Барбуда', 'Сент-Джонс'], ['Гренада', 'Сент-Джорджес'], ['Боливия', 'Сукре'], ['Гондурас', 'Тегусигальпа']]
Mas_Australia_Oceania = [['Самоа', 'Апиа'], ['Новая Зеландия', 'Веллингтон'], ['Австралия', 'Канберра'], ['Маршалловы острова', 'Маджуро'], ['Палау', 'Нгерулмуд'], ['Тонга', 'Нукуалофа'], ['Микронезия', 'Паликир'], ['Вануату', 'Порт-Вила'], ['Папуа-Новая Гвинея', 'Порт-Морсби'], ['Фиджи', 'Сува'], ['Тувалу', 'Фунафути'], ['Соломоновы острова', 'Хониара'], ['Кирибати', 'Южная Тарава']]


@bot.message_handler(commands=['start'])      #как реагировать на команду ....
def start_message(message):
    keyboard = types.InlineKeyboardMarkup() #создали клавиатуру 
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes') #кнопка «Да»    
    keyboard.add(key_yes) #добавляем кнопку в клавиатуру
    key_no= types.InlineKeyboardButton(text='Нет', callback_data='no')
    keyboard.add(key_no)
    question = "Привет, хотите сыграть в игру?"
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)   #отлавливает конкретного пользователя 

@bot.message_handler(commands=['end'])
def end_message(message):
    bot.send_message(message.from_user.id, "Хорошо, если захотите поиграть еще напишите /start")

@bot.callback_query_handler(func=lambda call: True)   #как реагировать на ответ 
def callback_worker(call):
    if call.data == "yes":      
        keyboard = types.InlineKeyboardMarkup()
        key_Europe = types.InlineKeyboardButton(text = "Европа", callback_data='europe')
        keyboard.add(key_Europe)
        key_Asia = types.InlineKeyboardButton(text = "Азия", callback_data='asia')
        keyboard.add(key_Asia)
        key_Africa = types.InlineKeyboardButton(text = "Африка", callback_data='africa')
        keyboard.add(key_Africa)
        key_America = types.InlineKeyboardButton(text = "Америка", callback_data='america')
        keyboard.add(key_America)
        key_Australia = types.InlineKeyboardButton(text = "Австралия и Океания", callback_data='australia')
        keyboard.add(key_Australia)
        question = "Выберите часть света:"
        bot.send_message(call.message.chat.id, text=question, reply_markup=keyboard)
    elif call.data == "no":
        bot.send_message(call.message.chat.id, 'Как хотите. Если вдруг понадоблюсь, напишите: /start')
    elif call.data == "europe":
        global random_index
        global partOfTheWorld
        partOfTheWorld = Mas_Europe
        random_index = random.randint(0, len(partOfTheWorld))      #генерация целых случайных чисел в промежутки 
        question = 'Вы выбрали Европу, если готовы напишите: Поехали'
        bot.send_message(call.message.chat.id, text = question)
    elif call.data == "asia":
        partOfTheWorld = Mas_Asia
        random_index = random.randint(0, len(partOfTheWorld))
        question = 'Вы выбрали Азию, если готовы напишите: Поехали'
        bot.send_message(call.message.chat.id, text = question)
    elif call.data == "africa":
        partOfTheWorld = Mas_Africa
        random_index = random.randint(0, len(partOfTheWorld))
        question = 'Вы выбрали Африку, если готовы напишите: Поехали'
        bot.send_message(call.message.chat.id, text = question)
    elif call.data == "america":
        partOfTheWorld = Mas_America
        random_index = random.randint(0, len(partOfTheWorld))
        question = 'Вы выбрали Америку, если готовы напишите: Поехали'
        bot.send_message(call.message.chat.id, text = question)
    elif call.data == "australia":
        partOfTheWorld = Mas_Australia_Oceania
        random_index = random.randint(0, len(partOfTheWorld))
        question = 'Вы выбрали Австралию и Океанию, если готовы напишите: Поехали'
        bot.send_message(call.message.chat.id, text = question)

@bot.message_handler(content_types=['text'])  #Как реагировать на тип: текстовое сообщение 
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу вам помочь?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Если Вы хотите завершить игру напишите /end, чтобы начать сначала /start. Если хотите увидеть правильный ответ напишите: Помоги")
    elif message.text.lower() == "поехали":     
        Country(message)
    else:
        bot.send_message(message.from_user.id, "Я вас не понимаю. Напишите /help.")

def Country(message):
    global random_index
    global partOfTheWorld
    question = "Какая столица у этой страны: " + partOfTheWorld[random_index][0] + "?"
    bot.send_message(message.from_user.id, text = question)
    bot.register_next_step_handler(message, Capital)   #чтобы отлавливал Capital, иначе отлавливать будет def get_text_messages

def Help(message):
    bot.send_message(message.from_user.id, text = partOfTheWorld[random_index][1]) 
    bot.register_next_step_handler(message, Country)

def Capital(message):
    global random_index
    global partOfTheWorld
    if message.text.lower() == partOfTheWorld[random_index][1].lower():
        bot.send_message(message.from_user.id, "Правильно! Давайте дальше)")
        random_index = random.randint(0, len(partOfTheWorld))
        Country(message)
    elif message.text == "/end":
        end_message(message)
    elif message.text == "Помоги":
        Help(message)
    else:
        bot.send_message(message.from_user.id, "Неверно. Попробуйте еще раз!")
            films_list = ['https://st.peopletalk.ru/wp-content/uploads/2021/12/kotjonok-iz-multfilma-shrek-ishchet-khozyaev-v-velikom-novgorode-2-1.jpeg', 'https://s3-eu-central-1.amazonaws.com/jazzpeople/wp-content/uploads/2015/11/12083404/Blue-Cat-Blues.jpg', 'https://vsememy.ru/wp-content/uploads/2022/09/8c810f1c1420c7c56192de0804d03b00.jpg' , 'https://papik.pro/uploads/posts/2021-11/1637131289_27-papik-pro-p-grustnii-skvidvard-risunok-30.jpg' , 'https://papik.pro/uploads/posts/2021-11/1637115154_54-papik-pro-p-risunki-grustnie-iz-multikov-55.jpg']
        URL = random.choice(films_list)
        bot.send_photo(message.from_user.id, photo = URL)
        Country(message)
        

        
        


bot.polling(none_stop=True, interval=0)    #Связь с bot father через longpoll ("Мне кто-то написал?" Интервал: как часто спрашивает)