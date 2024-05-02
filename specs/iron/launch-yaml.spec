# Meta Package
Name:           ros-iron-launch-yaml
Version:        2.0.3
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-launch_yaml and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-launch_yaml
Requires:       ros2-iron-launch_yaml-devel

Obsoletes: ros-iron-launch-yaml < 2.0.3-1

%description
YAML frontend for the launch package.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.2.0.3-1
- Update to latest release
