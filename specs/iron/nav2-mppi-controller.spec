# Meta Package
Name:           ros-iron-nav2-mppi-controller
Version:        1.2.9
Release:        1%{?dist}
License:        MIT
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-nav2_mppi_controller and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-nav2_mppi_controller
Requires:       ros2-iron-nav2_mppi_controller-devel

Obsoletes: ros-iron-nav2-mppi-controller < 1.2.9-1

%description
nav2_mppi_controller

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Jun 05 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.1.2.9-1
- Update to latest release
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.1.2.8-1
- Update to latest release
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.1.2.7-1
- Update to latest release
