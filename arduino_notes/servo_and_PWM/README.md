# Arduino pwm输出函数以及舵机响应记录

## 成品接收机输出参数：

于4号通道测得方波周期15ms（66.7hz），高电平电压3v，占空比约为高：低=2/25 到 2/15(1100us-1500us-1950us)

## Arduino 输出参数：

`analogWrite()`

输出值根据板型与引脚不同而不同。arduino uno pin3输出测量值约500hz（查询文档得输出频率490hz）

`Servo.write()`

于arduino UNO pin3测得周期为20ms（50hz）

`Servo.writeMicroseconds()`

同上条件，周期为20ms。个人理解与write不同之处在于该函数参数控制高电平时长，write参数控制角度。

[更详细的PWM控制说明](https://www.arduino.cc/en/Tutorial/SecretsOfArduinoPWM)

[arduino定时中断的使用](https://www.instructables.com/id/Arduino-Timer-Interrupts/)

[atmega328p数据手册](https://www.microchip.com/wwwproducts/en/ATMEGA328P)

### 舵机：

粗略查找资料得舵机响应角度由高电平持续时长决定，而非占空比。未进行深入研究。

圆周舵机输入pwm信号控制旋转方向及转速，常规舵机控制角度。

