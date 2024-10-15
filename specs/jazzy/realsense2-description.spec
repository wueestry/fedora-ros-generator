# Meta Package
Name:           ros-jazzy-realsense2-description
Version:        4.55.1
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/wiki/RealSense
Summary:        Meta package for ros2-jazzy-realsense2_description and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-realsense2_description
Requires:       ros2-jazzy-realsense2_description-devel

Obsoletes: ros-jazzy-realsense2-description < 4.55.1-1

%description
RealSense description package for Intel 3D D400 cameras

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Thu Jul 11 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.55.1-1
- Update to latest release
