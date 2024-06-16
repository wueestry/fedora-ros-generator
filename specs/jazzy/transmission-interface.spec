# Meta Package
Name:           ros-jazzy-transmission-interface
Version:        4.11.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-transmission_interface and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-transmission_interface
Requires:       ros2-jazzy-transmission_interface-devel

Obsoletes: ros-jazzy-transmission-interface < 4.11.0-1

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
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.11.0-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.8.0-1
- Update to latest release
