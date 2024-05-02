# Meta Package
Name:           ros-jazzy-parameter-traits
Version:        0.3.8
Release:        1%{?dist}
License:        BSD-3-Clause
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-parameter_traits and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-parameter_traits
Requires:       ros2-jazzy-parameter_traits-devel

Obsoletes: ros-jazzy-parameter-traits < 0.3.8-1

%description
Functions and types for rclcpp::Parameter

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.3.8-1
- Update to latest release
