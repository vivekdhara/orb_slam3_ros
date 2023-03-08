
# ORB-SLAM3

# 1. License

ORB-SLAM3 is released under [GPLv3 license](https://github.com/UZ-SLAMLab/ORB_SLAM3/LICENSE). For a list of all code/library dependencies (and associated licenses), please see [Dependencies.md](https://github.com/UZ-SLAMLab/ORB_SLAM3/blob/master/Dependencies.md).

For a closed-source version of ORB-SLAM3 for commercial purposes, please contact the authors: orbslam (at) unizar (dot) es.

If you use ORB-SLAM3 in an academic work, please cite:

    @article{ORBSLAM3_2020,
      title={{ORB-SLAM3}: An Accurate Open-Source Library for Visual, Visual-Inertial 
               and Multi-Map {SLAM}},
      author={Campos, Carlos AND Elvira, Richard AND G\´omez, Juan J. AND Montiel, 
              Jos\'e M. M. AND Tard\'os, Juan D.},
      journal={arXiv preprint arXiv:2007.11898},
      year={2020}
     }

## ROS


# 1. Building ORB-SLAM3 library and examples

Clone the repository:
```
git clone https://github.com/UZ-SLAMLab/ORB_SLAM3.git ORB_SLAM3
cd ORB_SLAM3
chmod +x build.sh
./build.sh
```

# 2. ROS

### Building the nodes 
1. Add the path including *Examples/ROS/ORB_SLAM3* to the ROS_PACKAGE_PATH environment variable. Open .bashrc file:
  ```
  gedit ~/.bashrc
  ```
and add at the end the following line. Replace PATH by the folder where you cloned ORB_SLAM3:

  ```
  export ROS_PACKAGE_PATH=${ROS_PACKAGE_PATH}:PATH/ORB_SLAM3/Examples/ROS
  chmod +x build_ros.sh
  ./build_ros.sh
  ```
  
### Running Stereo-Intertial Node
For a monocular input from topic `/camera/image_raw` run node ORB_SLAM3/Mono. You will need to provide the vocabulary file and a settings file. See the monocular examples above.

  ```
roslaunch orb_slam_3 stereo_d435_inertial.launch
  ```
  
  
  ```
 rosbag play --pause $BAG_NAME 
  rosbag play *.bag
  ```


​
# 3. IMU Topic
The purpose of unite_imu_method in ROS is to publish two separate IMU topics (Gyro and Accel) as a single topic called imu. While using Realsense node:

```
  <arg name="unite_imu_method"    default="linear_interpolation"/> -->

```

Its linear interpolation condition interpolates accel messages matched to the gyro timestamp.

In case data isnt aligned and/or at different rates, this will interpolate accel messages to gyro, exactly as in Realsense
```
python3 final_bag.py DIR_OF_ROSBAG
```
Further orientation filters are optional

# 4. Pose Visualisation
This script is for visualising the pose from KeyFrames.txt. In .yaml file use: 
    
    System.SaveAtlasToFile: "map_total"

    python3 pose.py

# 5. ROS Integration
Published Topics


    /orb_slam3/camera_pose, left camera pose in world frame, published at camera rate
    /orb_slam3/tracking_image, processed image from the left camera with key points and status text
    /orb_slam3/tracked_points, all key points contained in the sliding window
    /orb_slam3/all_points, all key points in the map


# 6. Topics
Subs:
```
     /camera/IMU
     /camera/left_image
     /camera/right_image
```
Pubs:
```
    /orb_slam3/camera_pose, left camera pose in world frame, published at camera rate
    /orb_slam3/all_points, all key points in the map
```
To save the Map, Camera Pose:

```
rosservice call /orb_slam_3/save_map
rosservice call /orb_slam_3/cam_pose_txt
```
![alt text](https://github.com/vivekdhara/ORB_SLAM3/blob/master/Figure_1.png?raw=true)


#  7.Save and load map 

The map file will have `.osa` extension, and is located in the `ROS_HOME` folder (`~/.ros/`)

#### Load map:
- Set the name of the map file to be loaded with `System.LoadAtlasFromFile` param in the settings file (`.yaml`).
#### Save map:
- **Option 1**: If `System.SaveAtlasToFile` is set in the settings file, the map file will be automatically saved when you kill the ros node.
- **Option 2**: You can also call the following ros service at the end of the session

```
rosservice call /orb_slam3/save_map [file_name]
```

# 8.Docker
Provided [Dockerfile](Dockerfile) sets up an image based a ROS noetic environment including RealSense SDK

To access a USB device (such as RealSense camera) inside docker container use:
``` bash
docker run --network host --privileged -v /dev:/dev -it [image_name]
```
