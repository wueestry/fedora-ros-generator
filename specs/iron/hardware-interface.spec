# Meta Package
Name:           ros-iron-hardware-interface
Version:        3.25.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-hardware_interface and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-hardware_interface
Requires:       ros2-iron-hardware_interface-devel

Obsoletes: ros-iron-hardware-interface < 3.25.0-1

%description
ros2_control hardware interface

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.3.25.0-1
- Update to latest release
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.3.24.0-1
- Update to latest release
