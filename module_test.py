import module.status_module as status
import module.io_module as io

def test_status_module():
    status.init()
    status.save("霊媒師","OCしてる",1)
    print(status.load("霊媒師","OCしてる"))

def test_io_module():
    io.csv_read("sample/wolf/village_g21.csv")
    print(io.csv_terget("sample/wolf/village_g21.csv"))
    
if __name__ == "__main__":
    # test_status_module()
    test_io_module()