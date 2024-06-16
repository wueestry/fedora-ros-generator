# Meta Package
Name:           ros-iron-shape-msgs
Version:        5.0.1
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-shape_msgs and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-shape_msgs
Requires:       ros2-iron-shape_msgs-devel

Obsoletes: ros-iron-shape-msgs < 5.0.1-1

%description
A package containing some message definitions which describe geometric
shapes.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.5.0.1-1
- Update to latest release
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.5.0.0-1
- Update to latest release
