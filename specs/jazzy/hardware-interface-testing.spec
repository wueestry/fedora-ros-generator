# Meta Package
Name:           ros-jazzy-hardware-interface-testing
Version:        4.13.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-hardware_interface_testing and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-hardware_interface_testing
Requires:       ros2-jazzy-hardware_interface_testing-devel

Obsoletes: ros-jazzy-hardware-interface-testing < 4.13.0-1

%description
ros2_control hardware interface testing

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Thu Jul 11 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.13.0-1
- Update to latest release
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.11.0-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.8.0-1
- Update to latest release
