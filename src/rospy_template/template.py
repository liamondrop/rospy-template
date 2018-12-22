import rospy
import rospy_template.msg

class TemplateException(Exception):
    pass


class Template:
    def __init__(self):
        if not rospy.has_param('template_config'):
            raise TemplateException('No template configuration found')
        self.config = rospy.get_param('template_config')

        # initiate subscribers
        rospy.Subscriber('template_msg', rospy_template.msg.Message,
                         self.message_callback)

    def message_callback(self, msg):
        """
        Callback function for the template_msg topic.

        Test that it works with the following on the command line:
        rostopic pub /template_msg rospy_template/Message "test message"

        NOTE: be sure to run the setup.bash script first or ROS will not know
        you have built the message yet
        """
        rospy.loginfo('Message received: {}'.format(msg.value))
