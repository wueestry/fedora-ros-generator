# Meta Package
Name:           ros-jazzy-tricycle-controller
Version:        4.9.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-tricycle_controller and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-tricycle_controller
Requires:       ros2-jazzy-tricycle_controller-devel

Obsoletes: ros-jazzy-tricycle-controller < 4.9.0-1

%description
Controller for a tricycle drive mobile base

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Jun 05 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.9.0-1
- Update to latest release
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.8.0-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.7.0-1
- Update to latest release
