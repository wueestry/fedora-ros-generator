# Meta Package
Name:           ros-iron-realsense2-description
Version:        4.55.1
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/wiki/RealSense
Summary:        Meta package for ros2-iron-realsense2_description and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-realsense2_description
Requires:       ros2-iron-realsense2_description-devel

Obsoletes: ros-iron-realsense2-description < 4.55.1-1

%description
RealSense description package for Intel 3D D400 cameras

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Jun 05 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.4.55.1-1
- Update to latest release
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.4.54.1-1
- Update to latest release
