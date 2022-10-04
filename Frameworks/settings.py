import configparser as cp

def read_config() -> cp.ConfigParser:
    '''
    Read config.ini file
    '''
    config = cp.ConfigParser()
    config.read('config.ini')
    return config
