# Meta Package
Name:           ros-humble-vision-opencv
Version:        3.2.1
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/wiki/vision_opencv
Summary:        Meta package for ros2-humble-vision_opencv and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-vision_opencv
Requires:       ros2-humble-vision_opencv-devel

Obsoletes: ros-humble-vision-opencv < 3.2.1-1

%description
Packages for interfacing ROS2 with OpenCV, a library of programming
functions for real time computer vision.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Mon Aug 12 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.3.2.1-1
- Update to latest release
