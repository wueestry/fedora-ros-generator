# Meta Package
Name:           ros-jazzy-rcl-yaml-param-parser
Version:        9.2.2
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-rcl_yaml_param_parser and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-rcl_yaml_param_parser
Requires:       ros2-jazzy-rcl_yaml_param_parser-devel

Obsoletes: ros-jazzy-rcl-yaml-param-parser < 9.2.2-1

%description
Parse a YAML parameter file and populate the C data structure.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.9.2.2-1
- Update to latest release
