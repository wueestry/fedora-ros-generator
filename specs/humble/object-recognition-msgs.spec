# Meta Package
Name:           ros-humble-object-recognition-msgs
Version:        2.0.0
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-object_recognition_msgs and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-object_recognition_msgs
Requires:       ros2-humble-object_recognition_msgs-devel

Obsoletes: ros-humble-object-recognition-msgs < 2.0.0-1

%description
Object_recognition_msgs contains the ROS message and the actionlib
definition used in object_recognition_core

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Sep 27 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.0.0-1
- update to latest release
* Thu Mar 09 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.0.0-1
- Initial humble build
