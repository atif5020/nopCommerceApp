#  test case can not retrieve data from config.ini file directly...so utility file will retrieve data from config.ini
#  and will pass it to test case
import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")


# for every variable we need to create a method
class ReadConfig():
    @staticmethod  # to access it directly with class name without creating object, so no need to pass 'self'
    def getAppUrl():
        url = config.get('common data', 'baseURL')
        return url

    @staticmethod
    def getUserName():
        username = config.get('common data', 'username')
        return username

    @staticmethod  # to access it directly with class name without creating object
    def getUserPassword():
        password = config.get('common data', 'password')
        return password
