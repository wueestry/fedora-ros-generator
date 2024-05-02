# Meta Package
Name:           ros-iron-image-geometry
Version:        3.5.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-image_geometry and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-image_geometry
Requires:       ros2-iron-image_geometry-devel

Obsoletes: ros-iron-image-geometry < 3.5.0-1

%description
`image_geometry` contains C++ and Python libraries for interpreting
images geometrically. It interfaces the calibration parameters in
sensor_msgs/CameraInfo messages with OpenCV functions such as image
rectification, much as cv_bridge interfaces ROS sensor_msgs/Image with
OpenCV data types.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.3.5.0-1
- Update to latest release
