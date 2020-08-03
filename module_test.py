import status_module.status_module as status

def test_status_module():
    status.init()
    status.save("霊媒師","OCしてる",1)
    print(status.load("霊媒師","OCしてる"))
    
if __name__ == "__main__":
    test_status_module()