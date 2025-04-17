# Meta Package
Name:           ros-jazzy-ur-description
Version:        3.1.0
Release:        1%{?dist}
License:        BSD-3-Clause
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-ur_description and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-ur_description
Requires:       ros2-jazzy-ur_description-devel

Obsoletes: ros-jazzy-ur-description < 3.1.0-1

%description
URDF description for Universal Robots

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Tue Apr 15 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.3.1.0-1
- Update to latest release
