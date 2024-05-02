# Meta Package
Name:           ros-humble-cv-bridge
Version:        3.2.1
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/wiki/cv_bridge
Summary:        Meta package for ros2-humble-cv_bridge and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-cv_bridge
Requires:       ros2-humble-cv_bridge-devel

Obsoletes: ros-humble-cv-bridge < 3.2.1-1

%description
This contains CvBridge, which converts between ROS2 Image messages and
OpenCV images.

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
* Mon Mar 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.3.2.1-1
- update to latest release
* Mon Mar 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - noetic.1.16.2-1
- update to latest release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.3.2.1-1
- Initial humble build
