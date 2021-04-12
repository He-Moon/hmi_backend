import rospy


def getRostopics():
    rostopics = rospy.get_published_topics()
    return rostopics
