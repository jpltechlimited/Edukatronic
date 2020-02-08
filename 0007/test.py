from armToChessBoardInterface import ArmToChessBoardInterface

interface = ArmToChessBoardInterface()
A1 = [interface.BASE_LEFT, 0, interface.ELBOW_UP, 0, interface.SHOULDER_BACK, 3, interface.WRIST_DOWN, 0]
interface.move(A1)
#interface.grab()
#interface.move_back_to_center(A1)
#interface.arm.elbow.down(0.1)
#interface.arm.shoulder.down(0.1)
