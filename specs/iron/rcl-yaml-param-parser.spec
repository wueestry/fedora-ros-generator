# Meta Package
Name:           ros-iron-rcl-yaml-param-parser
Version:        6.0.5
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-rcl_yaml_param_parser and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-rcl_yaml_param_parser
Requires:       ros2-iron-rcl_yaml_param_parser-devel

Obsoletes: ros-iron-rcl-yaml-param-parser < 6.0.5-1

%description
Parse a YAML parameter file and populate the C data structure.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.6.0.5-1
- Update to latest release
