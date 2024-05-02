# Meta Package
Name:           ros-iron-controller-interface
Version:        3.24.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-controller_interface and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-controller_interface
Requires:       ros2-iron-controller_interface-devel

Obsoletes: ros-iron-controller-interface < 3.24.0-1

%description
Description of controller_interface

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.3.24.0-1
- Update to latest release
