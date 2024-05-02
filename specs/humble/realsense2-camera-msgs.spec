# Meta Package
Name:           ros-humble-realsense2-camera-msgs
Version:        4.54.1
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/wiki/RealSense
Summary:        Meta package for ros2-humble-realsense2_camera_msgs and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-realsense2_camera_msgs
Requires:       ros2-humble-realsense2_camera_msgs-devel

Obsoletes: ros-humble-realsense2-camera-msgs < 4.54.1-1

%description
RealSense camera_msgs package containing realsense camera messages
definitions

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Thu Feb 22 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.4.54.1-1
- update to latest release
* Thu May 04 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.4.51.1-2
- use librealsense ysystem dependency
* Tue Apr 25 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.4.51.1-1
- update to latest release
