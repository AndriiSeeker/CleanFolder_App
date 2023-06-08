from app_design import start_app

if __name__ == '__main__':
    try:
        start_app()
    except Exception as err:
        print(err)
