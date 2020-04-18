import time
from selenium import webdriver
import os
import click

class Git:
    def __init__(self, repoName, privacy=''):
        #inititalizing object:
        #   repoName = name of repositoriy you want to create
        #   repoLink = name of the link which is created by github
        #   driver = WebDriver
        self.repoName = repoName
        self.repoLink = "https://github.com/rennerluca/" + repoName + ".git"
        self.driver = webdriver.Chrome('chromedriver')
        
        if privacy == 'p':
            self.privacy = True
        else:
            self.privacy = False


    def __signIn(self):
        #this method signs in to github
        self.driver.get('https://github.com/rennerluca')

        #navigates to signIn-page
            #defines fields of webpage
        signIn_btn = self.driver.find_element_by_link_text('Sign in')
            #clicks sign in
        signIn_btn.click()

        #signing in
            #defines fields of webpage
        username_input = self.driver.find_element_by_name('login')
        password_input = self.driver.find_element_by_name('password')
        confirm_btn = self.driver.find_element_by_name('commit')
            #inputs username and password
        username_input.send_keys("rennerluca")
        password_input.send_keys("WK^,XsxfqsafY8cCB:")
            #confirms signIn
        confirm_btn.click()

    def __addLocal(self):
        #this method creates a local folder with the name of "self.repoName" and copies the created git into it

        #changes path to projects folder
        os.chdir('/Users/luca/Documents/projects')

        #creates directory and navigates into it
        os.system('mkdir ' + self.repoName)
        os.chdir('/Users/luca/Documents/projects/' + self.repoName)

        #copies git repo into directory
        os.system('git clone ' + self.repoLink + ' .')


    def createRepo(self):
        #this method creates a repository with the name "self.repoName"

        #signs in
        self.__signIn()

        #change page
        self.driver.get('https://github.com/new')

        #create repository
            #defines fields of webpage 
        repoName_input = self.driver.find_element_by_id('repository_name')
        repoCreate_btn = self.driver.find_element_by_xpath('//*[@id="new_repository"]/div[3]/button')
            #sets name of repository and waits
        repoName_input.send_keys(self.repoName)
        time.sleep(1)
            #checks privacy
        if self.privacy:
            repoPrivacy_radio = self.driver.find_element_by_id('repository_visibility_private')
            repoPrivacy_radio.click()
            #confirms
        repoCreate_btn.click()

        #quit 
        self.driver.quit()

        #creates and adds git to local repository
        self.__addLocal()

        

#making it callable

@click.command()
@click.option('-p',help='declares if repo should be private', is_flag=True)
@click.argument('name')
def create(name, p):

    if p:
        pointer = Git(name, 'p')
    else:
        pointer = Git(name)

    pointer.createRepo()


if __name__ == '__main__':
    create()
