# TODO MAKE COMPATIBLE WITH WINDOWS (gekodriver path)

## some library
## start firefox
from selenium import webdriver
## for enter
from selenium.webdriver.common.keys import Keys
## for waits and time
import time
## for store information
import json
## for password
import hashlib
## for check the email
from validate_email import validate_email
## for crypting
from cryptography.fernet import Fernet
## for config file
from configparser import ConfigParser
## for random tag
import random


## for bypass
bypass = '0'

Debug = 0



## global variable

uff_tags = ['citazione','amore','solitudine']

stand_data = \
    {
        'email' : 'alessandro.condello.email@gmail.com',
        'password' : 'prova_tumblr'
    }

## dati

dati = \
    [

    ]

## possibility
possibility = \
    [
        'p',
        'r',
        'l'
    ]


## count
num = 0

## tag

tag = []

## time

time_post = []

## list time + what they do

lista = []

## dictionary

dati_url = ConfigParser()

## account

## functions

## load data

def load():
    ## open and read
    global dati_url
    ## load json on the dictionary
    dati_url.read('dati.data')
    ## for account
    global account_exist
    ## load crypt
    with open('crypt.data', 'r') as f:
        ## if it's empty
        if len(f.read()) == 0:
            account_exist = 0
            ## make it different
            passw = 0
            passw2 = 1
            while passw != passw2:
                ## insert password
                passw = input('insert a password (you can disable it after this message)')
                passw2 = input('re-insert the password')
                ## confront if arent the same
                if passw != passw2:
                    print('passwords are not the same')
            ## remove?
            if input('do you want remove the password? (y/n)')[0] == 'y':
                bypass = 'this_is_a_secret'
            ## add password to file
            with open('crypt.data', 'w') as r:
                ## add the key for the crypt
                r.write('{},{}\n{}'.format(hashlib.sha256(str.encode(passw2)).hexdigest(), bypass, Fernet.generate_key()))
        ## controll the password
        else:
            account_exist = 1
            ## open the file for save the data
            with open('crypt.data', 'r') as t:
                ## read password and bypass
                provaaa = t.readline().split(',')
                password_hash = provaaa[0]
                bypass = provaaa[1].replace('\n','')
                ## read crypt
                key = t.readline()
                global _Crypt
                ## make it byte + fernet
                _Crypt = Fernet(_Cryptogr.f_str_b(key))
            ## controll if the sha of Bypass isnt the same of the key
            if hashlib.sha256(str.encode(bypass)).hexdigest() != '06282fd37afcaf863d4b8d5d00141d71094b92cc730fdc030376ae95eacf0866':
                ## load password from file
                choose = '0'
                ## continue util choose == password
                while choose != password_hash:
                    ## take an input and transform in his sha
                    choose = hashlib.sha256(str.encode(input('insert the password'))).hexdigest()
                    ## controll if arent the same
                    if choose != password_hash:
                        print('password wrong, please wait')
                        waits(3)
                    else:
                        print('password is correct')
    ## dati (tag, time, accounts)
    with open('dati_pers.data', 'r') as ra:
        empty = ra.read()
    ## controll if isnt empty
    if empty != '':
        with open('dati_pers.data','r') as r_a:
            ## controll tag
            prova = r_a.readline().split()
            global tag
            tag = [_Cryptogr.f_b_str(i) for i in prova]
            ## controll time
            prova = r_a.readline().split()
            global time_post
            time_post = [_Cryptogr.f_b_str(i) for i in prova]
            ## controll lista
            global lista
            prova = r_a.readline().split()
            lista = [_Cryptogr.f_b_str(i) for i in prova]
            ## controll dati
            global dati
            dati = []
            prova = r_a.readline().split()
            ind = 0
            for i in range(len(prova)):
                if i % 2 == 0:
                    dati.append({})
                    dati[ind]['email'] = _Cryptogr.f_b_str(prova[i])
                else:
                    dati[ind]['password'] =_Cryptogr.f_b_str(prova[i])
                    ind += 1



## function input with range
def rich_num(sentec, max):
    ## initialization num1
    num1 = 0
    ## if < or > (range)
    while num1 < 1 or num1 > max:
        num1 = round(int(input(sentec)),0)
        if num1 < 1 or num1 > max:
            print("invalid number (1-{})".format(max))
    return num1

class send:
## click enter
    def enter(path):
        ## click enter on path
        path.send_keys(Keys.RETURN)

    ## send_text
    def text(path,text):
        ## left click on path
        path.send_keys(text)

## waits
def waits(seconds):
    time.sleep(seconds)

## menu

class menu:

    def first():
        return rich_num("1) start bot\n2) add/remove tags\n3) set time\n4) settings\n5) save\n6) quit",6)

    def timer():
        return input('choose when it will post and when it will like/reblog some post. write \'no\' for dont reset previusly settings (1 p / 1 l / 1 r / no)\ninsert x for exit').split()

    def settings():
        return rich_num('1) go to post settings\n2) list of all accounts\n3) quit',3)

    def account():
        return rich_num('1) add account\n2) remove an account\n3) quit',3)

    def bot_m():
        return rich_num('1) like post\n2) reblog\n3) time post\n4) automac bot\n5) post',5)


## classes

## control date
class contr_date():
    def first(date):
        if str.isnumeric(date[0]):
            ## check lenght
            first = date.split(':')[0]
            if len(date) == 5:
                second = date.split(':')[1]
            elif len(date) == 2:
                second = '00'
            if len(first) == 2 and len(second) == 2:
                ## check if it exist
                if int(first) >= 0 and int(first) <= 24 and int(second) >= 0 and int(second) <= 60:
                    return 1
                else:
                    ## error date dont exist
                    print('date must be >= 1 and <= 24 (hour) 60 (minute)')
            else:
                ## error lenght
                print('date must be length 2/4 (yes 16:00 no 1600:0)')
        else:
            ## error letter
            print('date cannot be componed by some letter! ')
        return 0

    def after(date,lenght):
        if str.isnumeric(date[0]):
            ## check lenght
            first = date.split(':')[0]
            if len(date) == 5:
                second = date.split(':')[1]
            elif len(date) == 2:
                second = '00'
            ## remove
            elif len(first) == 1:
                if int(date) > lenght:
                    print('number is too big (max {})'.format(lenght))
                    return 0
                elif int(date) < 1:
                    print('number is too small (min 1)')
                    return 0
                else:
                    return 2
            else:
                print('date must be lenght 2/4 (yes 16:00 no 1600:0)')
                return 0
            # check if it exist
            if int(first) >= 0 and int(first) <= 24 and int(second) >= 0 and int(second) <= 60:
                return 1
            else:
                ## error date dont exist
                print('date must be >= 1 and <= 24 (hour) 60 (minute)')
        else:
            print('date cannot be componed by some letter! ')
        return 0

## now time
def now_time():
    now = time.asctime().split()[3].split(':')
    print("now it's {}:{}".format(now[0], now[1]))

## crypt help class

class _Cryptogr:
    def f_str_b(sents):
        return bytes(sents[sents.find('\'')+1:-1],'utf-8')
    def str_b_f(sents):
        return str(_Crypt.encrypt(bytes(sents, 'utf-8')))
    def f_b_str(sents):
        sent = str(_Crypt.decrypt(_Cryptogr.f_str_b(sents)))
        return sent[sent.find('\'')+1:-1]

## input time
class input_time:
    def first():
        ## remove all duplicate + input
        return input('choose when the bot will go (ex 15:30 10:00) ').split()
    ## input other time
    def other():
        return list(set(input('choose when the bot will go (ex 15:30 10:00) and for remove some time, just write his number (5 12:12) -> 5 ').split()))



class TumblrBot:
    ## initialization
    def __init__(self):
        ## load data
        load()
        ## start firefox
        self.bot = webdriver.Firefox(executable_path = '/usr/local/bin/geckodriver')
        ## se non ci sta nessuna email
        self.num = account_exist
        ## se dati[0] è soltanto {}
        if not bool(dati[0]):
            ## chiedere quante email
            self.num = rich_num("how many email do you want? ", 5)
        ## inizio loop aggiunta
            for i in range(self.num):
                ## aggiungere dizionari
                if i != 0:
                    dati.append({})
                ## inserire gli input
                dati[i]['email'],dati[i]['password'] = TumblrBot.Settings_main.req_account(self)
        self.Start_main.start(self)

    class Start_main():

        ## start iniziale
        def start(self):
            self.bot.get(dati_url['url']['login'])
            time.sleep(3)
            if self.bot.current_url == dati_url['url']['login']:
                TumblrBot.Start_main.login(self)
            else:
                TumblrBot.inizio(self)

        ## function login
        def login(self):
            ## for make less length
            bot = self.bot
            ## initializazion choose
            choose = 0
            ## check if there are more than 1 email
            if self.num > 1:
                print("which email would you use?, \nemails are these:")
                ## print all the email
                for i in range(self.num):
                    print("n^{} {}".format(i+1,dati[i]['email']))
                choose = rich_num("decide which email use ",self.num)-1
            else:
                scelte = 1
            ## send_enter path in email e password
            email_ins = dati[choose]['email']
            passw_ins = dati[choose]['password']
            ## entering date
            email_path = bot.find_element_by_id(dati_url['id_login']['email'])
            ## clear
            email_path.clear()
            ## start email
            ## insert email in path
            send.text(email_path,email_ins)
            ## press enter
            send.enter(email_path)
            ## loading
            waits(2)
            ## remove 2 process (magic link)
            proc2 = bot.find_element_by_class_name(dati_url['id_login']['go_password'])
            proc2.click()
            ## loading
            waits(2)
            ## password
            ## same for email
            password_path = bot.find_element_by_id(dati_url['id_login']['password'])
            password_path.clear()
            send.text(password_path,passw_ins)
            send.enter(password_path)
            ## change page
            time.sleep(3)
            ## check for the captcha
            if(bot.current_url == dati_url['url']['captcha']):
                self.captcha()
            else:
                TumblrBot.inizio(self)

        def captcha(self,passw_ins):
            ## same of precedent
            password_path = self.bot.find_element_by_id(dati_url['id_login']['password'])
            password_path.clear()
            send.text(password_path,passw_ins)
            password_path.send_keys(data['password'])
            print("completare il captcha")
            ## wait util url change
            TumblrBot.waiting(self)
            TumblrBot.inizio(self)




    ## start with bot
    def inizio(self):
        ## print
        choose = 0
        while not choose == 6:
            print(lista)
            choose = menu.first()
            ## start bot
            if choose == 1:
                # TODO add a start of the bot
                TumblrBot.Bot_Class(self.bot)
                pass
            ## add tag
            elif choose == 2:
                TumblrBot.tags(self)
            ## time
            elif choose == 3:
                TumblrBot.timer(self)
            ## setting
            elif choose == 4:
                TumblrBot.Settings_main.menu(self)
            ## save
            elif choose == 5:
                TumblrBot.save(self)
            ## quit
            elif choose == 6:
                TumblrBot.save(self)
                if Debug == 0:
                    self.bot.close()
            print(lista)

    def timer(self):
        global time_post
        ## add a new time
        if not time_post:
            choose = print("there arent any timer, please add some timer")
            now_time()
            ## input
            time_text = input_time.first()
            a = set(time_text)
            print(list(a))

            ## analyze + add
            time_post = [time_text[i] for i in range(len(time_text)) if contr_date.first(time_text[i])]

        else:
            print('all timer: ')
            for i in range(len(time_post)):
                print('{} {}'.format(i+1,time_post[i]))
            now_time()
            ## input
            time_text = input_time.other()
            ## analyze
            for i in range(len(time_text)):
                choose = contr_date.after(time_text[i],len(time_post))
                ## if time exist
                if choose == 1:
                    ## add / remove possible duplicate
                    time_post = list(set(time_post) | set([time_text[i]]))
                ## remove from time_post
                elif choose == 2:
                    time_post.pop(int(time_text[i])-1)



    ## settings main

    class Settings_main:

        def menu(self):

            ## choose
            choose = menu.settings()
            ## settings time
            if choose == 1:
                TumblrBot.Settings_main.timer(self)
            ## settings account
            elif choose == 2:
                TumblrBot.Settings_main.account(self)
        ## settings account
        def account(self):
            ## make global the account ist
            print('list account:')
            ## print al accounts
            for i in range(len(dati)):
                print('{} {} {}'.format(i+1, dati[i]['email'],dati[i]['password']))
            ## input
            choose = menu.account()
            ## add an account
            if choose == 1:
                ## request email+password
                email,password = TumblrBot.Settings_main.req_account(self)
                ## adding email+password
                dati.append({'email': email, 'password': password})
            elif choose == 2:
                ## check if the len of account list is > 1
                if len(dati) > 1:
                    print('list: ')
                    ## stamp all the accounts
                    for i in range(len(dati)):
                        print('{} {} {}'.format(i + 1, dati[i]['email'], dati[i]['password']))
                    ## input the numbers
                    choose_2 = rich_num('write the number of the email you would remove',len(dati))
                    ## analyze
                    for i in range(choose_2):
                        if len(dati) > 1:
                            ## if choose is <= len(account_list) for dont go overflow
                            if choose_2[i] <= len(dati):
                                dati.pop(i-1)






        ## settings post timer
        def timer(self):
            a = 0
            global tag
            global time_post
            ## check if time and tags are created
            if not tag:
                print('the tags havent been made')
                a += 1
            if not time_post:
                print('the timers havent been made')
                a += 1
            ## if they have been created
            if not a:
                ## print all time
                for i in range(len(time_post)):
                    print('{} {}'.format(i+1, time_post[i]))
                ## n^even number input
                choose = menu.timer()

                ## for finish
                global finish__
                finish__ = 0
                ## for after number
                global number__
                number__ = 0
                global prev__
                ## global
                len_max = len(time_post)
                global lista

                for i in range(len(choose)):
                    ## if it doesn't ever encountered 'no'
                    if finish__ == 0:
                        decision = TumblrBot.Settings_main.analyze(self, choose[i],len_max,i)



        ## analyze the choose
        def analyze(self, sent,len_max,cont):
            global number__
            global finish__
            global prev__
            global possibility
            global lista
            ## finish
            if sent == 'no' or sent=='x':
                finish = 1
            else:
                ## control if is a number
                if str.isnumeric(sent):
                    ## if yes
                    if int(sent) >= 1 and int(sent) <= len_max:
                        ## for the next round
                        number__ = 1
                        prev__ = time_post[int(sent)-1].split(',')[0]
                        print(prev__)
                    else:
                        ## error number
                        print('{} is too big'.format(sent))
                ## if isnt a number and previously there is a number
                elif number__:
                    ## check if the letter exist
                    if sent[0] in possibility:
                        ## if yes
                        ## if list isnt empty
                        if lista:
                            ## control if the number exist
                            i = 0
                            fine_ck = 0
                            ## while i < lenght of list and 'if' has never been opened
                            while i < len(lista) and not fine_ck:
                                print('a')
                                ## control if exist
                                if lista[i].split(',')[0] == prev__:
                                    ## if yes remove
                                    lista.pop(i)
                                    fine_ck = 1


                                i = i + 1
                            lista.append(prev__ + ',' + sent)
                        ## append to list
                        else:
                            lista.append(str(time_post[cont] + ',' + sent))
                    else:
                        print('{} dont exist'.format(sent))


        def req_account(self):
            a = 1
            while a:
                email = input('insert an email')
                ## check if the email exist
                if validate_email(email,check_mx=True):
                    a = 0
                else:
                    print('email dont exist')
            password = input('insert a password')
            return email,password











    def tags(self):
        ## check if tag directory is empty
        global tag
        if not tag:
            tag_contr = input('there arent any tag, please add some tag').split()
            first = 0
            for i in range(len(tag_contr)):
                ## check if contain a number
                if str.isnumeric(tag_contr[i]):
                    print('number cant be added!')
                ## else add to directory
                else:
                    if first == 0:
                        tag.append(tag_contr[0])
                        first += 1
                    else:
                        tag.append(tag_contr[i])
                        tag = list(set(tag))
                        print(tag)
        else:
            ## print all tags
            for i in range(len(tag)):
                print('{} {}'.format(i + 1, tag[i]))
            ## input
            tag_contr = input("for remove some tag, write his number\nfor add, just write the tag ").split()
            ## inspect
            for i in range(len(tag_contr)):
                ## remove
                if str.isnumeric(tag_contr[i][0]):
                    ## control the lenght
                    if int(tag_contr[i][0]) > len(tag):
                        print("{} contain a number too big".format(i + 1))
                    ## if it's ok
                    else:
                        tag.pop(int(tag_contr[i][0]) - 1)
                ## add
                else:
                    tag.append(tag_contr[i])
                    tag = list(set(tag))
    ## save tag, time, accounts
    def save(self):
        ## first tag, after time and after accounts
        with open('dati_pers.data', 'w') as file_w:
            ## first line
            for i in tag:
                file_w.write(_Cryptogr.str_b_f(i))
                file_w.write(' ')
            file_w.write('\n')
            ## second line
            for i in time_post:
                file_w.write(_Cryptogr.str_b_f(i))
                file_w.write(' ')
            file_w.write('\n')
            ## third line
            for i in lista:
                file_w.write(_Cryptogr.str_b_f(i))
                file_w.write(' ')
            file_w.write('\n')
            ## final line
            for i in range(len(dati)):
                file_w.write(_Cryptogr.str_b_f(dati[i]['email']))
                file_w.write(' ')
                file_w.write(_Cryptogr.str_b_f(dati[i]['password']))
                file_w.write(' ')



    ## wait util url change
    def waiting(self):
        start_url = self.bot.current_url
        while start_url == self.bot.current_url:
            time.sleep(1)

    class Bot_Class:
        def __init__(self,bot):
            self.bot = bot
            ## controll tag and time_post
            if time_post and tag:
                ## input the choose
                choose = menu.bot_m()
                ## analyze choose
                if choose == 1:
                    ## start like
                    TumblrBot.Bot_Class.like(self)
                elif choose == 2:
                    ## start reblog
                    TumblrBot.Bot_Class.reblog(self)
                elif choose == 3:
                    ## settings time_post
                    TumblrBot.Settings_main.timer(self)
                elif choose == 4:
                    ## automatic bot
                    TumblrBot.Bot_Class.automatic_bot_start(self)
                elif choose == 5:
                    ## post
                    TumblrBot.Bot_Class.post_create(self)




            ## error tag + time post == NULL
            else:
                print('make some tags and time')

        ## automatic bot
        def automatic_bot_start(self):
            print('prova')
            ## create time
            time_now = ':'.join(time.asctime().split()[3].split(':')[:2])
            ## controll

            while self.bot.current_url.__contains__('tumblr'):
                time_now = ':'.join(time.asctime().split()[3].split(':')[:2])
                ## controll all time
                for i in lista:
                    if time_now in i.split(',')[0]:
                        choose_ = i.split(',')[1]
                        ## analyze
                        if choose_ == 'l':
                            TumblrBot.Bot_Class.like(self)
                        elif choose_ == 'r':
                            TumblrBot.Bot_Class.reblog(self)
                        elif choose_ == 'p':
                            pass
                print('waiting..')
                waits(45)

            self.bot.get(dati_url['url']['dashboard'])



        ## bot like
        def like(self):
            ## create link
            TumblrBot.Bot_Class.page_tag(self)
            ## like
            TumblrBot.Bot_Class.make(self,'like')

        ## bot reblog
        def reblog(self):
            ## create link
            TumblrBot.Bot_Class.page_tag(self)
            #reblog
            TumblrBot.Bot_Class.make(self,'reblog')

        ## create link page
        def page_tag(self):
            ## create link + go to link
            link = dati_url['url']['search'] + tag[random.randint(0,len(tag)-1)] + dati_url['url']['search2']
            self.bot.get(link)
            waits(1)

        def make(self,option):
            ## get all post
            all_post = self.bot.find_elements_by_class_name(dati_url['id_login'][option])[:int(dati_url['config'][option + '_pass']) * 2]
            i = 0
            end = 0
            ## while util finish
            while end != int(dati_url['config'][option + '_pass']):
                ## controll if liked/reblogged
                if all_post[i].get_attribute('class') == dati_url['class'][option]:
                    all_post[i].click()
                    end += 1
                    ## for reblog
                    if option == 'reblog':
                        waits(2)
                        self.bot.find_element_by_class_name(dati_url['id_login']['reblog_button']).click()

                    waits(int(dati_url['config']['delay']))
                i += 1
        ## add a post
        def post_create(self):
            ## create post
            ## click post
            self.bot.find_element_by_class_name(dati_url['id_login']['post_create']).click()
            waits(1)
            ## click citation
            self.bot.find_element_by_class_name(dati_url['id_login']['post_button_cit']).click()
            waits(1)
            ## send text
            text = 'aaa'
            send.text(self.bot.find_element_by_class_name(dati_url['id_login']['post_text']),text)
            ## create tags
            global uff_tags
            for i in uff_tags:
                ## take the path
                path_ = self.bot.find_elements_by_class_name('editor.editor-plaintext')
                ## send text and load it
                send.text(path_[2],i)
                waits(0.2)
                send.enter(path_[2])
                waits(0.2)
            ## post it
            self.bot.find_element_by_class_name(dati_url['id_login']['post_button']).click()









def main():
    inizio = TumblrBot()
if Debug != 1:
    main()
else:
    load()
    TumblrBot.inizio(1)
