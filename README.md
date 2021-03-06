# turtle-follower
ROS educational project

## Описание launch-файла
### Список аргументов
1. `turtle1_name` - имя первой (преследуемой) черепахи. Используется для изменения топика позиции при помощи remap в ноде listener, которая отвечает за логику следования второй черепахи за первой. Значение по-умолчанию: `turtle1`
2. `turtle2_name` - имя второй черепахи. Используется при создании в качестве параметра в ноде spawner, которая отвечает за создание второй черепахи, и для изменения топиков позиции и перемещния при помощи remap в ноде listener. Значение по-умолчанию: `turtle2`
### Список запускаемых нод
1. `turtlesim_node` - базовая нода с рабочей средой.
2. `spawner` (spawner.py) - нода для создания второй черепахи в рабойчей среде
3. `turtle_teleop_key` - нода для управления первой черепахой при помощи клавиатуры
4. `listener` (follower.py) - нода, отвечающая за следование второй черепахи за первой

## Логика движения
При изменении положения первой черепахи подписчик `pose_sub_1` вызывает рассчет направления движения для второй черепахи относительно её текущего положения, которое берется из переменной, обновляемой подписчиком `pose_sub_2`, и отправляется сообщение в топик движения второй черепахи для следования.

## Демонстрация работы
![](https://github.com/BassinD/turtle-follower/blob/main/turtle_demo.gif)
