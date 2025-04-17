# Meta Package
Name:           ros-jazzy-ur-calibration
Version:        3.2.0
Release:        1%{?dist}
License:        BSD-3-Clause
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-ur_calibration and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-ur_calibration
Requires:       ros2-jazzy-ur_calibration-devel

Obsoletes: ros-jazzy-ur-calibration < 3.2.0-1

%description
Package for extracting the factory calibration from a UR robot and
change it such that it can be used by ur_description to gain a correct
URDF

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Tue Apr 15 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.3.2.0-1
- Update to latest release
