# Meta Package
Name:           ros-iron-transmission-interface
Version:        3.25.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-transmission_interface and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-transmission_interface
Requires:       ros2-iron-transmission_interface-devel

Obsoletes: ros-iron-transmission-interface < 3.25.0-1

%description
transmission_interface contains data structures for representing
mechanical transmissions, methods for propagating values between
actuator and joint spaces and tooling to support this.

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
