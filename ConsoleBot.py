import time

class UsernameError(LookupError):
    '''Username not found!'''
class CommandError(LookupError):
    '''Undefined command'''
def input_error(handler: tuple) -> str:
    '''Return input error'''
    errors = {
        1: 'Enter valid command!',
        2: 'Username not found',
        3: 'Enter valid username and phone (phone must contain only digits)',
        4: 'Enter username',
    }
    def trying(user_input: tuple[str]) -> str:
        try:
            answer = handler(user_input)
        except UsernameError:
            return errors[2]
        except ValueError:
            return errors[3]
        except IndexError:
            return errors[3]
        except CommandError:
            return errors[1]
        except KeyError:
            return errors[2]
        return answer
    return trying

@input_error
def handler(user_input: tuple[str]) -> str:
    '''Handle commands'''
    global database

    def greet():
        return 'Hello!\nHow can I help you?'


    def add(user_input: tuple[str]) -> str:
        '''Add user number into database'''
        if user_input[1] in database:
            return 'User already exist'
        if user_input[2].isnumeric():
            database[user_input[1]] = user_input[2]
            return 'Done'
        
        raise ValueError


    def change(user_input: tuple[str]) -> str:
        '''Change user number'''

        if user_input[1] not in database:
            raise UsernameError
        if user_input[2].isnumeric():
            database[user_input[1]] = user_input[2]
            return 'Done'
        
        raise UsernameError

    def show(user_input: tuple[str]) -> str:
        '''Show User phone.\n
        If key: 'all' - show all contacts'''

        # if not database:
        #     return 'Database is empty!'
        if user_input[1] == 'all':
            title = '|{:^15}|{:^15}|\n'.format('Username', 'Phone')
            for username, phone in database.items():
                title += '|{:^15}|{:^15}|\n'.format(username, phone)
            return title
        
        return f'{user_input[1]}: {database[user_input[1]]}'
    
    if user_input[0] == 'hello':
        return greet()
    elif user_input[0] == 'add':
        return add(user_input)
    elif user_input[0] == 'change':
        return change(user_input)
    elif user_input[0] == 'phone':
        return show(user_input)
    elif user_input[0] == 'show':
        return show(user_input)
    raise CommandError
    
    

def parser(raw_input: str) -> str|tuple[str]:
    
    if raw_input == 'good bye' or\
       raw_input == 'close' or\
       raw_input == 'exit' or\
       raw_input == 'quit':
        print('Good bye!')
        time.sleep(3)
        return 'break'
    
    user_input = raw_input.split(' ')

    return tuple(user_input)

def main() -> None:
    """Main cycle"""
    while True:
        command = parser(input().lower())
        if command == 'break':
            break
        print(handler(command))



if __name__ == '__main__':
    
    database = {}
    main()
