# Meta Package
Name:           ros-jazzy-image-geometry
Version:        4.1.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-image_geometry and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-image_geometry
Requires:       ros2-jazzy-image_geometry-devel

Obsoletes: ros-jazzy-image-geometry < 4.1.0-1

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
* Thu Jul 11 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.1.0-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.0.0-1
- Update to latest release
