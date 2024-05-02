# Meta Package
Name:           ros-iron-action-tutorials-interfaces
Version:        0.27.1
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-action_tutorials_interfaces and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-action_tutorials_interfaces
Requires:       ros2-iron-action_tutorials_interfaces-devel

Obsoletes: ros-iron-action-tutorials-interfaces < 0.27.1-1

%description
Action tutorials action

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.0.27.1-1
- Update to latest release
