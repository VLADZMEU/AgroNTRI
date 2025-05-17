# AgroNTRI 
По умолчанию при старте raspberry попытается подключиться к WiFi точке доступа с параметрами

SSID: TurtleBro
Pass: turtlew001
или

SSID: TurtleBro5G
Pass: turtlew001

Подключение по SSH:
ssh pi@turtlebroNN.local  NN-номер  ssh pi@192.168.0.11  - по IP  пороль brobro

rostopic bw     Показать занимаемый сетевой канал  
rostopic echo   Вывести сообщения на экран  
rostopic find   Поиск топика по типу  
rostopic hz     Показать частоту обновления топика  
rostopic info   Показать информацию о топике  
rostopic list   Показать список существующий топиков  
rostopic pub    Опубликовать данные в топик  
rostopic type   Показать тип сообщения для топика  

Вывести сообщения из топика topic_name:   rostopic echo /topic_name

4)  ```
    ssh pi@turtlebroNN.local
    ```
    password: brobro
    ```
    rostopic list
    ```
5) ```
   rostopic echo /odom
   ```
6) ```
   rostopic info /cmd_vel
   ```
7) Сначала определим тип сообщения, публикуемого в топик /cmd_vel:
   ```
    rostopic type /cmd_vel
    ```
   Вывод:```geometry_msgs/Twist```
    ```
    rosmsg show geometry_msgs/Twist
    ```
    ```
    rostopic echo /cmd_vel
    ```

8) ```
   ifconfig
   ```
   wlan0: -> inet -> IP

   http://docs.voltbro.ru/starting-ros/messaging/rabota-s-topic.html
