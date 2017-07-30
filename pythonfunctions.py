def print_msg(msg, error="no error", **kwargs):
    print("log : "+error+":" + msg)
    print(kwargs)


print_msg("This will be logged","File not found",key_1="1,2,3,4")

