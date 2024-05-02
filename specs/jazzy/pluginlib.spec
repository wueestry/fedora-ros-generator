# Meta Package
Name:           ros-jazzy-pluginlib
Version:        5.4.2
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-pluginlib and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-pluginlib
Requires:       ros2-jazzy-pluginlib-devel

Obsoletes: ros-jazzy-pluginlib < 5.4.2-1

%description
The pluginlib package provides tools for writing and dynamically
loading plugins using the ROS build infrastructure. To work, these
tools require plugin providers to register their plugins in the
package.xml of their package.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.5.4.2-1
- Update to latest release
