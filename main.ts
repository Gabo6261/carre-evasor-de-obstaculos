let Distancia = 0
basic.showString("Hello!")
basic.showIcon(IconNames.Happy)
basic.forever(function () {
    Distancia = sonar.ping(
    DigitalPin.P14,
    DigitalPin.P15,
    PingUnit.Centimeters
    )
    mbit_Robot.CarCtrl(mbit_Robot.CarState.Car_Back)
    mbit_Robot.CarCtrlSpeed(mbit_Robot.CarState.Car_Right, 70)
    if (Distancia < 10) {
        mbit_Robot.CarCtrl(mbit_Robot.CarState.Car_Stop)
    } else {
        mbit_Robot.CarCtrlSpeed(mbit_Robot.CarState.Car_Run, 90)
    }
})
