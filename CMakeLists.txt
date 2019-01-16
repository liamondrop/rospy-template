cmake_minimum_required(VERSION 2.8.3)
project(rospy_template)

find_package(catkin REQUIRED COMPONENTS
    std_msgs
    message_generation
)

catkin_python_setup()

add_message_files(FILES Message.msg)
generate_messages(DEPENDENCIES std_msgs)
catkin_package(CATKIN_DEPENDS message_runtime)

install(DIRECTORY config launch msg
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

catkin_install_python(PROGRAMS bin/${PROJECT_NAME}_node
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
