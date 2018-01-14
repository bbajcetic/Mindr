# mindr

mindr is a cross-platform emotion monitoring app, essential for every smart home. The app
is tailored to provide an unintrusive and private solution to keep track of a child's well-being during all those times we can't be with them.

## How it works

The emotion monitoring happens on a device—a laptop, or any IoT device that supports
a camera—locally. Each frame from the camera is processed for emotional content
and severely emotional distress. The emotion processing is facilitated using
OpenCV, TensorFlow, and was trained using a convolutional neural network within
TFLearn. All of the image data is stored locally, to protect a parent's privacy.

The emotional data is then sent to a Django backend web-server where it is parsed
into a PostgreSQL database. The Django web-server then serves analytical data to
a React/Redux single-page web app which provides parents with a clean interface
for tracking their child's emotional behavior through time. Distressing emotional
events are expedited to the parent by sending notifications through SMS or email.
