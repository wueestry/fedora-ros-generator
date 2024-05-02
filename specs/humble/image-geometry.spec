# Meta Package
Name:           ros-humble-image-geometry
Version:        3.2.1
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-image_geometry and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-image_geometry
Requires:       ros2-humble-image_geometry-devel

Obsoletes: ros-humble-image-geometry < 3.2.1-1

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
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.3.2.1-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.3.2.1-1
- update to latest upstream release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.3.2.1-1
- Initial humble build
