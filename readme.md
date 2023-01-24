This project uses the `pupil-apriltags` library to recognize AprilTags and identify their pose cross-platform using Python. The goal of this project is to open a camera connected to a Raspberry Pi, and, with minimal latency, recognize the pose of AprilTags in frame, and send the data to a connected client (ex. RoboRiO) via NetworkTables or WebSockets.

#Requirements
- `pupil-apriltags`
- `python3`
- `opencv2`
- `cmake`
- `numpy`