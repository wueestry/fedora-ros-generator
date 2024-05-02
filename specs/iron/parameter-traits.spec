# Meta Package
Name:           ros-iron-parameter-traits
Version:        0.3.8
Release:        1%{?dist}
License:        BSD-3-Clause
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-parameter_traits and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-parameter_traits
Requires:       ros2-iron-parameter_traits-devel

Obsoletes: ros-iron-parameter-traits < 0.3.8-1

%description
Functions and types for rclcpp::Parameter

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.0.3.8-1
- Update to latest release
