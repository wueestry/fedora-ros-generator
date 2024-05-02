# Meta Package
Name:           ros-jazzy-action-tutorials-interfaces
Version:        0.33.2
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-action_tutorials_interfaces and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-action_tutorials_interfaces
Requires:       ros2-jazzy-action_tutorials_interfaces-devel

Obsoletes: ros-jazzy-action-tutorials-interfaces < 0.33.2-1

%description
Action tutorials action

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.33.2-1
- Update to latest release
