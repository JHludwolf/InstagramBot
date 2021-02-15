#! python3
# José Luis Lobera del Castillo
# InstagramBot.py Simulates a human interaction with instagram web
# python 3 -i InstagramBot.py
# Start date: 11.10.2020
# End date: 19.10.20
# FORMAT FOR CODYE EVIDENCE:
# Project: Instagram Bot | Simulates a human interaction with instagram web
# *Description* '''
# Day # / 100
# __init__() | Getters & setters | SignUp() LogIn() Search() Follow() Unfollow() GoHome() GoToProfile
# Like() Comment() Share() NextPost() PrevPost() OpenPost() SendDM()

# $$$$$ $   $ $$$$$ $$$$$ $$$$$ $$$$$ $$$$$ $$$$$ $   $     $$$$$ $$$$$ $$$$$
#   $   $$  $ $       $   $   $ $     $   $ $   $ $$ $$     $   $ $   $   $
#   $   $ $ $ $$$$$   $   $$$$$ $$$$$ $$$$  $$$$$ $ $ $     $$$$  $   $   $
#   $   $  $$     $   $   $   $ $   $ $   $ $   $ $   $     $   $ $   $   $
# $$$$$ $   $ $$$$$   $   $   $ $$$$$ $   $ $   $ $   $     $$$$$ $$$$$   $

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

def human_type(text, elem):
    for l in text:
        elem.send_keys(l)
        sleep(.25)

def print_menu():
    print('\n__INSTAGRAM BOT__\n0. ......... EXIT\n-----------------\n1. ....... SignUp\n2. ........ LogIn\n3. ....... Search\n4. ....... Follow\n5. ..... Unfollow\n6. .... Open Post\n7. ...... Send DM\n8. .... Followers\n9. .... Following\n10. . Unfollowers\n')

def print_post_menu():
    print('\n___POST MENU___\n0 ........ EXIT\n---------------\n1. ... (UN)LIKE\n2. .... COMMENT\n3. ...... SHARE\n4. .. NEXT POST\n5. .. PREV POST\n')

class Bot:
    def __init__(self, username = None, password = None, name = None, email = None):
        self.__name = name
        self.__email = email
        self.__username = username
        self.__password = password
        self.browser = webdriver.Chrome()
    
    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, new_username):
        if isinstance(new_username, str):
            self.__username = new_username
        else:
            print('Username not a "str"')

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, new_password):
        if isinstance(new_password, str):
            self.__password = new_password
        else:
            print('Password not a "str"')
    
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str):
            self.__name = new_name
        else:
            print('name not a "str"')

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, new_email):
        if isinstance(new_email, str):
            self.__email = new_email
        else:
            print('Email not a "str"')

    def openInstagram(self):
        self.browser.get(r'https://www.instagram.com')
        sleep(2)
    
    def signUp(self):
        try:
            print('Signing up . . .')
            self.openInstagram()
            self.browser.find_element_by_class_name('_7UhW9.xLCgt.qyrsm.gtFbE.se6yk').click()
            sleep(2)

            human_type(self.email, self.browser.find_element_by_name('emailOrPhone'))

            human_type(self.name, self.browser.find_element_by_name('fullName'))

            human_type(self.username, self.browser.find_element_by_name('username')) 

            human_type(self.password, self.browser.find_element_by_name('password'))

            self.browser.find_element_by_class_name('sqdOP.L3NKy.y3zKF').click()
            sleep(2)

            self.browser.find_element_by_class_name('_2iem').click()
            sleep(2)

            print('Signed up succesfully!')
        except Exception as e:
            print('Could not sign in:',e)
        
    def logIn(self):
        print("Logging In . . .")
        try:
            self.openInstagram()
            human_type(self.username, self.browser.find_element_by_name('username')) 

            human_type(self.password, self.browser.find_element_by_name('password'))

            self.browser.find_element_by_class_name('sqdOP.L3NKy.y3zKF').click()
            sleep(4)

            self.browser.find_element_by_class_name('sqdOP.yWX7d.y3zKF').click()
            sleep(2)

            self.browser.find_element_by_class_name('aOOlW.HoLwm').click()
            sleep(2)

            print('Logged in succesfully!')
        except Exception as e:
            print('Could not Log In:', e)
    
    def goHome(self):
        self.browser.find_element_by_class_name('s4Iyt').click()

    def goToProfile(self):
        self.goHome()
        self.browser.find_element_by_class_name('_2dbep.qNELH').click()

    def search(self, to_search = None):
        self.goHome()
        to_search = to_search if to_search is not None else input("Search: ")
        print('Searching . . .')
        try:
            searchFieldElem = self.browser.find_element_by_class_name('XTCLo.x3qfX')
            searchFieldElem.clear()
            human_type(to_search, searchFieldElem)
            sleep(4)

            searchResults = self.browser.find_elements_by_class_name('yCE8d')
            if len(searchResults) == 0:
                print('No results.')
                return

            elemsIndex = 5 if len(searchResults) > 5 else len(searchResults)
            for i in range(elemsIndex):
                print(i+1,searchResults[i].find_element_by_class_name('Ap253').text)
            
            x = int(input('Select the profile you want to visit: '))
            searchResults[x-1].click()
            
            print('Search completed!')
        except Exception as e:
            print('Could not search:',e)

    def follow(self, username = None):
        self.goHome()
        username = username if username is not None else input("Username: ")
        print("Following . . .")
        try:
            searchFieldElem = self.browser.find_element_by_class_name('XTCLo.x3qfX')
            searchFieldElem.clear()
            human_type(username, searchFieldElem)
            sleep(4)

            searchResults = self.browser.find_elements_by_class_name('yCE8d')
            if len(searchResults) == 0:
                print('No results.')
                return

            searchResults[0].click()
            sleep(2)
            try:
                self.browser.find_element_by_class_name('_5f5mN.jIbKX._6VtSN.yZn4P').click()
                print(username,'followed succesfully!')
            except:
                self.browser.find_element_by_class_name('sqdOP.L3NKy.y3zKF').click()
                print('Follow request succesfully sent to',username,'!')
            
        except Exception as e:
            print('Could not follow:',e)

    def unfollow(self, username = None):
        self.goHome()
        username = username if username is not None else input("Username: ")
        print("Unfollowing . . .")
        try:
            searchFieldElem = self.browser.find_element_by_class_name('XTCLo.x3qfX')
            searchFieldElem.clear()
            human_type(username, searchFieldElem)
            sleep(4)

            searchResults = self.browser.find_elements_by_class_name('yCE8d')
            if len(searchResults) == 0:
                print('No results.')
                return

            searchResults[0].click()
            sleep(2)

            self.browser.find_element_by_class_name('_5f5mN.-fzfL._6VtSN.yZn4P').click()
            sleep(2)
            self.browser.find_element_by_class_name('aOOlW.-Cab_').click()

            print(username,'unfollowed succesfully!')
        except Exception as e:
            print('Could not unfollow:',e)

    def like(self):
        print('(Un)liking post . . .')
        try:
            self.browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button').click()
            print('Post (un)liked succesfully!')
        except Exception as e:
            print('Could not (un)like post:',e)

    def comment(self, comment = None):
        comment = comment if comment is not None else input("Comment: ")
        print("Commenting . . .")
        try:
            self.browser.find_element_by_class_name('Ypffh').click()
            human_type(comment, self.browser.find_element_by_class_name('Ypffh'))
            self.browser.find_element_by_class_name('Ypffh').send_keys(Keys.ENTER)
            print('Post commented succesfully!')
        except Exception as e:
            print('Could not comment:',e)        

    def share(self, username = None):
        username = username if username is not None else input("Username: ")
        print('Sharing . . .')
        try:
            self.browser.find_elements_by_class_name('wpO6b')[4].click()
            sleep(2)
            self.browser.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div/div[1]/div/div').click()
            sleep(2)
            human_type(username, self.browser.find_element_by_class_name('j_2Hd.uMkC7.M5V28'))
            sleep(2)
            self.browser.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/div[2]/div/div/div[3]/button').click()
            sleep(2)
            self.browser.find_element_by_class_name('sqdOP.yWX7d.y3zKF.cB_4K').click()
            print('Post shared succesfully!')
        except Exception as e:
            print('Could not share:',e)

    def nextPost(self):
        print('Going to next post . . .')
        try:
            self.browser.find_element_by_class_name('_65Bje.coreSpriteRightPaginationArrow').click()
            print('In next post!')
        except Exception as e:
            print('Could not go to next post:',e)

    def prevPost(self):
        print('Going to prev post . . .')
        try:
            self.browser.find_element_by_class_name('ITLxV.coreSpriteLeftPaginationArrow').click()
            print('In prev post!')
        except Exception as e:
            print('Could not go to prev post:',e)

    def openPost(self):
        numberOfPosts = self.browser.find_element_by_class_name('g47SY').text
        postIndex = int(input('Select one of the {} posts: '.format(numberOfPosts)))

        try:
            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(3)
            self.browser.find_elements_by_class_name('v1Nh3.kIKUG._bz0w')[postIndex-1].click()
            
            x = -1
            while x != 0:
                print_post_menu()
                x = int(input('Input: '))
                switcher = {
                    1: self.like,
                    2: self.comment,
                    3: self.share,
                    4: self.nextPost,
                    5: self.prevPost
                }
                func = switcher.get(x, lambda: "Invalid option")
                func()
            print('Closing Post . . .')
            self.browser.find_element_by_xpath('/html/body/div[4]/div[3]/button').click()
            print('Post closed succesfully!')
            
        except Exception as e:
            print('Could not search:',e)

    def sendDM(self, username = None):
        username = username if username is not None else input("Username: ")
        try:
            self.goHome()
            self.browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[2]/a').click()
            sleep(2)
            self.browser.find_element_by_class_name('wpO6b.ZQScA').click()
            sleep(2)
            human_type(username, self.browser.find_element_by_class_name('j_2Hd.uMkC7.M5V28'))
            sleep(2)
            self.browser.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div[2]/div[1]/div/div[3]/button').click()
            sleep(2)
            self.browser.find_element_by_class_name('sqdOP.yWX7d.y3zKF.cB_4K').click()
            sleep(2)
            x=-1
            while x != 0:
                message = input('Message: ')
                human_type(message, self.browser.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea'))
                self.browser.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
                print('Message sent succesfully!')
                x = int(input('Send another message?\n0.\tNO\n1.\tYES\n'))
        except Exception as e:
            print('Could not send message:',e)

    def _get_names(self,numUsers):
        try:
            print('Getting names . . .')
            sleep(4)
            scroll_box = self.browser.find_element_by_css_selector("div[class='isgrP']")
            
            loadUsers = len(scroll_box.find_elements_by_tag_name('li'))
            while loadUsers >= numUsers-10:
                self.browser.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',scroll_box)
                sleep(1)
                loadUsers = len(scroll_box.find_elements_by_tag_name('li'))
            print('Names load succesfully! Creating names list . . .')
            names = [name.text for name in scroll_box.find_elements_by_tag_name('a') if name.text != '']

            self.browser.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div/div[2]/button").click()
            print('List returned succesfully!')
            return names
        except Exception as e:
            print('Could not get users:',e)

    def followers(self):
        print('Checking followers . . .')
        try:
            username = self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/h2').text
            self.browser.find_element_by_xpath("//a[contains(@href,'/followers')]").click()
            followers = self._get_names(int(self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span').text.replace(',','')))
            
            followersFile = open(username + '-FOLLOWERS.txt','w')
            followersFile.write('\n'.join(followers))
            followersFile.close()
            print('Followers checked succesfully!')
        except Exception as e:
            print('Could not list followers:',e)

    def following(self):
        print('Checking following . . .')
        try:
            username = self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/h2').text
            self.browser.find_element_by_xpath("//a[contains(@href,'/following')]").click()
            following = self._get_names(int(self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a/span').text.replace(',','')))
            
            followingFile = open(username + '-FOLLOWING.txt','w')
            followingFile.write('\n'.join(following))
            followingFile.close()
            print('Following checked succesfully!')
        except Exception as e:
            print('Could not list following:',e)

    def unfollowers(self):
        print('Checking unfollowers . . .')
        try:
            username = self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/h2').text

            self.browser.find_element_by_xpath("//a[contains(@href,'/followers')]").click()
            followers = self._get_names(int(self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span').text.replace(',','')))
            print('Followers listed!')
            self.browser.find_element_by_xpath("//a[contains(@href,'/following')]").click()
            following = self._get_names(int(self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a/span').text.replace(',','')))
            print('Following listed!')
            unfollowers = [user for user in following if user not in followers]

            print(username,'unfollowers:')
            print(unfollowers)
        except Exception as e:
            print('Could not get unfollowers:',e)

    def menu(self):
        x = -1
        while x != 0:
            try:
                print_menu()
                x = int(input('Input: '))
                switcher = {
                    1: self.signUp,
                    2: self.logIn,
                    3: self.search,
                    4: self.follow,
                    5: self.unfollow,
                    6: self.openPost,
                    7: self.sendDM,
                    8: self.followers,
                    9: self.following,
                    10: self.unfollowers,
                }
                func = switcher.get(x, lambda: "Invalid option")
                func()
            except Exception as e:
                print('ERROR:',e)
        self.browser.quit()
        print('Goodbye!')
        

if __name__ == "__main__":
    myBot = Bot('luisfabianzunigabasurto', 'flzb69420', 'Fabian Luis Zuñiga Basurto','fabianluiszunigabasurto@gmail.com')
    myBot.menu()
    
