# Meta Package
Name:           ros-iron-pluginlib
Version:        5.2.2
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-pluginlib and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-pluginlib
Requires:       ros2-iron-pluginlib-devel

Obsoletes: ros-iron-pluginlib < 5.2.2-1

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
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.5.2.2-1
- Update to latest release
