import getpass
import vk


APP_ID = 5625108


def get_user_login():
    user_login = input("Введите логин Вконтакте:")
    return user_login


def get_user_password():
    user_password = getpass.getpass()
    return user_password


def get_online_friends(login, password):
    online_friends_id = []
    online_friends = []
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope="friends"
    )
    api = vk.API(session)
    online_friends_id = api.friends.getOnline()
    online_friends = api.users.get(user_ids=online_friends_id)
    return online_friends


def output_friends_to_console(friends_online):
    print('Твои друзья онлайн:')
    for friend in friends_online:
        print("%s %s" % (friend.get('first_name'), friend.get('last_name')))

if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
