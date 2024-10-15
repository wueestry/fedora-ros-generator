# Meta Package
Name:           ros-jazzy-vision-opencv
Version:        4.1.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/wiki/vision_opencv
Summary:        Meta package for ros2-jazzy-vision_opencv and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-vision_opencv
Requires:       ros2-jazzy-vision_opencv-devel

Obsoletes: ros-jazzy-vision-opencv < 4.1.0-1

%description
Packages for interfacing ROS2 with OpenCV, a library of programming
functions for real time computer vision.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Aug 03 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.1.0-1
- Update to latest release
