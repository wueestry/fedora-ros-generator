# Meta Package
Name:           ros-jazzy-nav2-mppi-controller
Version:        1.3.2
Release:        1%{?dist}
License:        MIT
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-nav2_mppi_controller and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-nav2_mppi_controller
Requires:       ros2-jazzy-nav2_mppi_controller-devel

Obsoletes: ros-jazzy-nav2-mppi-controller < 1.3.2-1

%description
nav2_mppi_controller

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Mon Aug 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.3.2-1
- Update to latest release
* Thu Jul 11 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.3.1-1
- Update to latest release
