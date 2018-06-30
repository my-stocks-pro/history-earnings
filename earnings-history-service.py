from classServerAPI import ServerAPI


def main():
    #TODO query url date

    server = ServerAPI()
    server.init_routing()

    server.api.run(host='0.0.0.0', port=8003)

    pass

if __name__ == '__main__':
    main()
