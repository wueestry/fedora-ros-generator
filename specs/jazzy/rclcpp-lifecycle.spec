# Meta Package
Name:           ros-jazzy-rclcpp-lifecycle
Version:        28.1.3
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-rclcpp_lifecycle and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-rclcpp_lifecycle
Requires:       ros2-jazzy-rclcpp_lifecycle-devel

Obsoletes: ros-jazzy-rclcpp-lifecycle < 28.1.3-1

%description
Package containing a prototype for lifecycle implementation

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Thu Jul 11 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.28.1.3-1
- Update to latest release
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.28.1.2-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.28.1.1-1
- Update to latest release
