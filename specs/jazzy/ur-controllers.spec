# Meta Package
Name:           ros-jazzy-ur-controllers
Version:        3.2.0
Release:        1%{?dist}
License:        BSD-3-Clause
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-ur_controllers and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-ur_controllers
Requires:       ros2-jazzy-ur_controllers-devel

Obsoletes: ros-jazzy-ur-controllers < 3.2.0-1

%description
Provides controllers that use the speed scaling interface of Universal
Robots.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Tue Apr 15 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.3.2.0-1
- Update to latest release
