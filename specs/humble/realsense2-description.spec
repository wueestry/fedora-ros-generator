# Meta Package
Name:           ros-humble-realsense2-description
Version:        4.54.1
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/wiki/RealSense
Summary:        Meta package for ros2-humble-realsense2_description and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-realsense2_description
Requires:       ros2-humble-realsense2_description-devel

Obsoletes: ros-humble-realsense2-description < 4.54.1-1

%description
RealSense description package for Intel 3D D400 cameras

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Thu Feb 22 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.4.54.1-1
- update to latest release
