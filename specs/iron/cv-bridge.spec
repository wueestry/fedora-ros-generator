# Meta Package
Name:           ros-iron-cv-bridge
Version:        3.5.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/wiki/cv_bridge
Summary:        Meta package for ros2-iron-cv_bridge and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-cv_bridge
Requires:       ros2-iron-cv_bridge-devel

Obsoletes: ros-iron-cv-bridge < 3.5.0-1

%description
This contains CvBridge, which converts between ROS2 Image messages and
OpenCV images.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.3.5.0-1
- Update to latest release
