# Meta Package
Name:           ros-humble-hardware-interface-testing
Version:        2.41.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-hardware_interface_testing and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-hardware_interface_testing
Requires:       ros2-humble-hardware_interface_testing-devel

Obsoletes: ros-humble-hardware-interface-testing < 2.41.0-1

%description
ros2_control hardware interface testing

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.41.0-1
- Update to latest release
* Wed Mar 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.40.0-1
- update to latest release
* Mon Feb 19 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.39.1-1
- Update to latest release
