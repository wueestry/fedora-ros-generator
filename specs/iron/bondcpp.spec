# Meta Package
Name:           ros-iron-bondcpp
Version:        4.0.0
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/wiki/bondcpp
Summary:        Meta package for ros2-iron-bondcpp and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-bondcpp
Requires:       ros2-iron-bondcpp-devel

Obsoletes: ros-iron-bondcpp < 4.0.0-1

%description
C++ implementation of bond, a mechanism for checking when another
process has terminated.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.4.0.0-1
- Update to latest release
