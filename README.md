# map_changer

## run  
```
rosrun map_changer map_changer
```

## call
* load map cit2_1f
```
rosservice call /map_changer/change_map "id: 0"
```

* load map cit2_18f
```
rosservice call /map_changer/change_map "id: 1"
```

## TODO
* more infomation
* add parameter file
* add rviz trigger panel
* **more versatility**
