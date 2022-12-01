from Labs.src.tvRemoteFinal.tvController import *

def main():
    app = QApplication([])
    window = Television()

    window.show()
    app.exec_()
    window.show()




if __name__ == '__main__':
    main()
