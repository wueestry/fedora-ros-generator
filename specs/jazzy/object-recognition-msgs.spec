# Meta Package
Name:           ros-jazzy-object-recognition-msgs
Version:        2.0.0
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-object_recognition_msgs and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-object_recognition_msgs
Requires:       ros2-jazzy-object_recognition_msgs-devel

Obsoletes: ros-jazzy-object-recognition-msgs < 2.0.0-1

%description
Object_recognition_msgs contains the ROS message and the actionlib
definition used in object_recognition_core

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.2.0.0-1
- Update to latest release
