import controller
import model
import view
from controller.controller import Controller

try:
    if __name__ == '__main__':

        controller = Controller()
        controller()

except Exception as e:
        print(e)