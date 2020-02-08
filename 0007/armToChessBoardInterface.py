from roboarm import Arm
import time


class ArmToChessBoardInterface:
    def __init__(self):
        self.arm = Arm()
        self.vendor = 0x1267
        self.bmRequestType = 0x40
        self.bRequest = 6
        self.wValue = 0x100
        self.wIndex = 0
        self.sleep_time = 1
        self.BASE_RIGHT = 1,
        self.BASE_LEFT = 2,
        self.ELBOW_UP = 3,
        self.ELBOW_DOWN = 4,
        self.SHOULDER_FRONT = 5,
        self.SHOULDER_BACK = 6,
        self.WRIST_UP = 7,
        self.WRIST_DOWN = 8

    def __move_shoulder_down__(self, time_to_move):
        if time_to_move != 0:
            self.arm.shoulder.down(time_to_move)
            time.sleep(self.sleep_time)

    def __move_shoulder_up__(self, time_to_move):
        if time_to_move != 0:
            additional_time = time_to_move / 14
            self.arm.shoulder.up(time_to_move + additional_time)
            time.sleep(self.sleep_time)

    def __move_elbow_down__(self, time_to_move):
        if time_to_move != 0:
            self.arm.elbow.down(time_to_move)
            time.sleep(self.sleep_time)

    def __move_elbow_up__(self, time_to_move):
        if time_to_move != 0:
            additional_time = time_to_move / 10
            self.arm.elbow.up(time_to_move + additional_time)
            time.sleep(self.sleep_time)

    def __move_left__(self, time_to_move):
        if time_to_move != 0:
            self.arm.base.rotate_clock(time_to_move)
            time.sleep(self.sleep_time)

    def __move_right__(self, time_to_move):
        if time_to_move != 0:
            self.arm.base.rotate_counter(time_to_move)
            time.sleep(self.sleep_time)

    def __move_wrist_up__(self, time_to_move):
        if time_to_move != 0:
            self.arm.wrist.up(time_to_move)
            time.sleep(self.sleep_time)

    def __move_wrist_down__(self, time_to_move):
        if time_to_move != 0:
            self.arm.wrist.down(time_to_move)
            time.sleep(self.sleep_time)

    def grab(self):
        self.arm.grips.close(0.2)
        time.sleep(self.sleep_time)

    def ungrab(self):
        self.arm.grips.open(0.2)
        time.sleep(self.sleep_time)

    def move(self, move_coordinates):
        if move_coordinates[0] == self.BASE_RIGHT:
            self.__move_right__(move_coordinates[1])
        if move_coordinates[0] == self.BASE_LEFT:
            self.__move_left__(move_coordinates[1])
        if move_coordinates[2] == self.ELBOW_DOWN:
            self.__move_elbow_down__(move_coordinates[3])
        if move_coordinates[2] == self.ELBOW_UP:
            self.__move_elbow_up__(move_coordinates[3])
        if move_coordinates[4] == self.SHOULDER_BACK:
            self.__move_shoulder_up__(move_coordinates[5])
        if move_coordinates[4] == self.SHOULDER_FRONT:
            self.__move_shoulder_down__(move_coordinates[5])
        if move_coordinates[6] == self.WRIST_UP:
            self.__move_wrist_up__(move_coordinates[7])
        if move_coordinates[6] == self.WRIST_DOWN:
            self.__move_wrist_down__(move_coordinates[7])

    def move_back_to_center(self, move_coordinates):
        if move_coordinates[4] == self.SHOULDER_BACK:
            self.__move_shoulder_down__(move_coordinates[5])
        if move_coordinates[4] == self.SHOULDER_FRONT:
            self.__move_shoulder_up__(move_coordinates[5])
        if move_coordinates[2] == self.ELBOW_DOWN:
            self.__move_elbow_up__(move_coordinates[3])
        if move_coordinates[2] == self.ELBOW_UP:
            self.__move_elbow_down__(move_coordinates[3])
        if move_coordinates[0] == self.BASE_RIGHT:
            self.__move_left__(move_coordinates[1])
        if move_coordinates[0] == self.BASE_LEFT:
            self.__move_right__(move_coordinates[1])
        if move_coordinates[6] == self.WRIST_UP:
            self.__move_wrist_down__(move_coordinates[7])
        if move_coordinates[6] == self.WRIST_DOWN:
            self.__move_wrist_up__(move_coordinates[7])

